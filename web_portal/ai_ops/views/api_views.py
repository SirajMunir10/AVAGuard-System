from pathlib import Path
"""
AVAGuard AI Operations — REST API Views
"""

import time
import hashlib
import logging

from django.conf import settings
from django.core.cache import cache
from django.utils import timezone
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from ..models import AIQueryLog, AISettings, AIQueryFeedback
from ..serializers import (
    AIQueryRequestSerializer,
    AIQueryResponseSerializer,
    AIQueryLogSerializer,
    AIAskFindingRequestSerializer,
)
from ..safety import sanitize_query, validate_response, scrub_payload
from ..retrieval import ComplianceRetriever, MockRetriever
from ..llm_service import LLMService, MockLLMService, FINDING_ASSISTANT_PROMPT
from core.models import AuditLog, ScanResult

logger = logging.getLogger(__name__)

# Module-level retriever instance — loaded once, reused across requests.
_retriever = None
_retriever_mtime = None


def _get_retriever():
    """Lazy-load the retriever singleton, reloading if index on disk has updated."""
    global _retriever, _retriever_mtime

    index_dir = getattr(settings, 'AI_INDEX_DIR', None)
    if not index_dir:
        logger.info("AI_INDEX_DIR not configured, using MockRetriever")
        _retriever = MockRetriever()
        _retriever_mtime = None
        return _retriever

    from pathlib import Path
    index_path = Path(index_dir)
    meta_file = index_path / "meta.pkl"

    if not index_path.exists() or not meta_file.exists():
        logger.warning(f"AI_INDEX_DIR {index_dir} or meta.pkl does not exist, using MockRetriever")
        _retriever = MockRetriever()
        _retriever_mtime = None
        return _retriever

    # Check modification time of meta.pkl on disk
    try:
        current_mtime = meta_file.stat().st_mtime
    except Exception as e:
        logger.warning(f"Failed to stat meta.pkl: {e}")
        current_mtime = None

    if _retriever is not None and not isinstance(_retriever, MockRetriever):
        if _retriever_mtime == current_mtime:
            return _retriever
        else:
            logger.info("FAISS index files updated on disk. Reloading ComplianceRetriever...")

    retriever = ComplianceRetriever(index_dir=index_path)
    if retriever.load():
        _retriever = retriever
        _retriever_mtime = current_mtime
    else:
        logger.warning("Failed to load FAISS index, falling back to MockRetriever")
        _retriever = MockRetriever()
        _retriever_mtime = None

    return _retriever


def _get_llm_service(ai_settings: AISettings):
    """Get the appropriate LLM service based on org settings."""
    provider = ai_settings.llm_provider

    if provider == 'mock':
        return MockLLMService()

    api_key = getattr(settings, 'AI_LLM_API_KEY', '')
    if not api_key:
        logger.warning("AI_LLM_API_KEY not set, falling back to MockLLMService")
        return MockLLMService()

    return LLMService(api_key=api_key, provider=provider)


def _get_ai_settings(user):
    """Get or create AI settings for the user's organization."""
    org = getattr(user, 'organization', None)
    if not org:
        return None

    try:
        return AISettings.objects.get(organization=org)
    except AISettings.DoesNotExist:
        return None


class AIQueryView(APIView):
    """
    POST /api/ai/query/

    Accepts a natural language compliance question, retrieves relevant
    documents from the FAISS index, generates a grounded answer via LLM,
    and returns the answer with source citations.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # 1. Validate request
        serializer = AIQueryRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        raw_query = serializer.validated_data['query']
        top_k = serializer.validated_data.get('top_k', 5)
        framework_filter = serializer.validated_data.get('framework', '').strip() or None
        total_start = time.perf_counter()

        # 2. Check AI settings
        ai_settings = _get_ai_settings(request.user)
        if ai_settings is None:
            return Response(
                {'error': 'AI features are not configured for your organization.'},
                status=status.HTTP_403_FORBIDDEN
            )

        if not ai_settings.is_enabled:
            return Response(
                {'error': 'AI features are disabled for your organization.'},
                status=status.HTTP_403_FORBIDDEN
            )

        # 3. Per-user rate limit (10 queries per minute)
        user_rate_key = f'ai_query_rate_{request.user.id}'
        user_rate = cache.get(user_rate_key, 0)
        if user_rate >= 10:
            return Response(
                {'error': 'Rate limit exceeded. Please wait before submitting another query.'},
                status=status.HTTP_429_TOO_MANY_REQUESTS
            )
        cache.set(user_rate_key, user_rate + 1, 60)  # 60 second window

        # 4. Check daily query limit (org-wide)
        today_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        query_count_today = AIQueryLog.objects.filter(
            organization=request.user.organization,
            created_at__gte=today_start,
        ).count()

        if query_count_today >= ai_settings.daily_query_limit:
            return Response(
                {'error': f'Daily query limit reached ({ai_settings.daily_query_limit}).'},
                status=status.HTTP_429_TOO_MANY_REQUESTS
            )

        # 4. Sanitize query
        sanitized = sanitize_query(raw_query)

        if not sanitized.is_safe:
            # Log the flagged query and return error
            AIQueryLog.objects.create(
                user=request.user,
                organization=request.user.organization,
                query_text=raw_query,
                sanitized_query=sanitized.text,
                response_text='',
                model_used='blocked',
                flagged=True,
                flag_reason=sanitized.flag_reason,
                latency_ms=(time.perf_counter() - total_start) * 1000,
            )
            return Response(
                {'error': 'Your query was flagged by our safety filters. Please rephrase your question.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        from ..mock_service import MockResponseService

        mode = request.session.get('ai_mode', 'ai')

        if mode == 'mock':
            mock_start = time.perf_counter()
            mock_result = MockResponseService.get_response(sanitized.text)
            
            total_ms = (time.perf_counter() - total_start) * 1000
            retrieval_ms = (time.perf_counter() - mock_start) * 1000
            
            # Log it
            log_entry = AIQueryLog.objects.create(
                user=request.user,
                organization=request.user.organization,
                query_text=raw_query,
                sanitized_query=sanitized.text,
                retrieved_sources=mock_result['sources'],
                response_text=mock_result['answer'],
                model_used='mock',
                provider_used='mock',
                is_fallback=True,
                source_count=mock_result['chunks_retrieved'],
                chunks_retrieved=mock_result['chunks_retrieved'],
                latency_ms=total_ms,
                response_time_ms=int(total_ms),
                retrieval_ms=retrieval_ms,
                token_count=0,
                flagged=False,
                mode='mock',
                status='success'
            )
            
            response_data = {
                'answer': mock_result['answer'],
                'sources': mock_result['sources'],
                'query_id': str(log_entry.id),
                'model_used': 'mock',
                'latency_ms': round(total_ms, 2),
                'retrieval_ms': round(retrieval_ms, 2),
                'mode': 'mock',
                'confidence': mock_result['confidence']
            }
            return Response(response_data, status=status.HTTP_200_OK)

        # 5. Query cache check (skip for framework-filtered queries)
        cache_key = None
        if not framework_filter:
            cache_key = f"ai_query:{hashlib.sha256(sanitized.text.encode()).hexdigest()}"
            cached = cache.get(cache_key)
            if cached:
                # Log as cache hit
                log_entry = AIQueryLog.objects.create(
                    user=request.user,
                    organization=request.user.organization,
                    query_text=raw_query,
                    sanitized_query=sanitized.text,
                    retrieved_sources=cached.get('sources', []),
                    response_text=cached.get('answer', ''),
                    model_used=cached.get('model_used', 'cached'),
                    provider_used=ai_settings.llm_provider,
                    is_fallback=False,
                    source_count=len(cached.get('sources', [])),
                    chunks_retrieved=len(cached.get('sources', [])),
                    latency_ms=(time.perf_counter() - total_start) * 1000,
                    response_time_ms=int((time.perf_counter() - total_start) * 1000),
                    retrieval_ms=0,
                    token_count=0,
                    flagged=False,
                    mode='ai',
                    status='success',
                    retrieval_method='cache',
                    confidence_level=cached.get('confidence', 'none'),
                )
                cached_response = dict(cached)
                cached_response['query_id'] = str(log_entry.id)
                cached_response['latency_ms'] = round(
                    (time.perf_counter() - total_start) * 1000, 2
                )
                cached_response['retrieval_method'] = 'cache'
                return Response(cached_response, status=status.HTTP_200_OK)

        # 6. Full retrieval pipeline (BM25 + FAISS + RRF + Cross-Encoder)
        retriever = _get_retriever()
        search_result = retriever.search(
            sanitized.text, top_k=top_k,
            framework_filter=framework_filter,
        )

        retrieval_ms = search_result.retrieval_ms
        rerank_ms = search_result.rerank_ms
        results = search_result.results
        confidence = search_result.confidence

        query_status = 'success'
        error_msg = ''

        if not results:
            answer_text = (
                "I don't have sufficient information in my knowledge base "
                "to answer this question confidently. Please add relevant "
                "documents to the corpus or rephrase your question."
            )
            sources = []
            model_used = 'none'
            is_fallback = True
            token_count = 0
            confidence = 'none'
        else:
            # 6. LLM generation
            llm = _get_llm_service(ai_settings)
            context_chunks = [r.text for r in results if r.text]

            generation = llm.generate(
                query=sanitized.text,
                context_chunks=context_chunks,
                model_name=ai_settings.model_name,
                max_tokens=ai_settings.max_tokens,
                temperature=ai_settings.temperature,
            )

            # 7. Validate response + handle LLM failure gracefully
            if generation.success:
                answer_text = validate_response(generation.text)
            else:
                logger.error(
                    f"LLM generation failed for user {request.user.email}: "
                    f"{generation.error}"
                )
                answer_text = (
                    'I was unable to generate an answer at this time. '
                    'Please try again later.'
                )
                query_status = 'error'
                error_msg = generation.error

            sources = [
                {
                    'filename': r.filename,
                    'relative_path': r.relative_path,
                    'score': round(r.reranker_score, 4),
                    'text': r.text,
                    'snippet': (r.text[:200] + '...') if len(r.text) > 200 else r.text,
                    'reranker_score': round(r.reranker_score, 4),
                    'hybrid_rank': r.hybrid_rank,
                    'final_rank': r.final_rank,
                    'metadata': r.metadata,
                }
                for r in results
            ]
            model_used = generation.model
            is_fallback = generation.is_fallback
            token_count = generation.token_count

        total_ms = (time.perf_counter() - total_start) * 1000

        # 9. Log everything with full retrieval instrumentation
        log_entry = AIQueryLog.objects.create(
            user=request.user,
            organization=request.user.organization,
            query_text=raw_query,
            sanitized_query=sanitized.text,
            retrieved_sources=sources,
            response_text=answer_text,
            model_used=model_used,
            provider_used=ai_settings.llm_provider,
            is_fallback=is_fallback,
            source_count=len(sources),
            chunks_retrieved=len(sources),
            latency_ms=total_ms,
            response_time_ms=int(total_ms),
            retrieval_ms=retrieval_ms,
            token_count=token_count,
            flagged=False,
            mode='ai',
            status=query_status,
            error_message=error_msg,
            # Phase 1 fields
            retrieval_method='hybrid',
            rerank_latency_ms=rerank_ms,
            average_similarity_score=search_result.avg_reranker_score,
            top_similarity_score=search_result.top_reranker_score,
            confidence_level=confidence,
            retrieved_document_count=len(results),
            reranker_scores=search_result.reranker_details,
        )

        # 10. Return response
        response_data = {
            'answer': answer_text,
            'sources': sources,
            'query_id': str(log_entry.id),
            'model_used': model_used,
            'latency_ms': round(total_ms, 2),
            'retrieval_ms': round(retrieval_ms, 2),
            'rerank_ms': round(rerank_ms, 2),
            'mode': 'ai',
            'confidence': confidence,
            'framework_filter': framework_filter or '',
        }

        # 11. Cache successful responses for future identical queries
        if cache_key and query_status == 'success' and results:
            cache.set(cache_key, response_data, timeout=3600)  # 1 hour TTL

        return Response(response_data, status=status.HTTP_200_OK)


class AIAskFindingView(APIView):
    """
    POST /api/ai/ask-finding/<uuid:result_id>/

    Accepts a question about a specific finding.
    Applies ContextualScrubber to the finding evidence before sending to the LLM.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, result_id):
        # 1. Validate request
        serializer = AIAskFindingRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        raw_query = serializer.validated_data['query']
        total_start = time.perf_counter()

        # 2. Check AI settings
        ai_settings = _get_ai_settings(request.user)
        if ai_settings is None or not ai_settings.is_enabled:
            return Response(
                {'error': 'AI features are disabled or not configured for your organization.'},
                status=status.HTTP_403_FORBIDDEN
            )

        # 3. Rate Limits
        user_rate_key = f'ai_query_rate_{request.user.id}'
        user_rate = cache.get(user_rate_key, 0)
        if user_rate >= 10:
            return Response(
                {'error': 'Rate limit exceeded. Please wait before submitting another query.'},
                status=status.HTTP_429_TOO_MANY_REQUESTS
            )
        cache.set(user_rate_key, user_rate + 1, 60)

        today_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        query_count_today = AIQueryLog.objects.filter(
            organization=request.user.organization,
            created_at__gte=today_start,
        ).count()

        if query_count_today >= ai_settings.daily_query_limit:
            return Response(
                {'error': f'Daily query limit reached ({ai_settings.daily_query_limit}).'},
                status=status.HTTP_429_TOO_MANY_REQUESTS
            )

        # 4. Tenant Isolation & Fetch Finding
        try:
            finding = ScanResult.objects.get(id=result_id, scan__organization=request.user.organization)
        except ScanResult.DoesNotExist:
            return Response({'error': 'Finding not found or access denied.'}, status=status.HTTP_404_NOT_FOUND)

        # 5. Sanitize user query
        sanitized = sanitize_query(raw_query)
        if not sanitized.is_safe:
            AIQueryLog.objects.create(
                user=request.user,
                organization=request.user.organization,
                query_text=raw_query,
                sanitized_query=sanitized.text,
                model_used='blocked',
                flagged=True,
                flag_reason=sanitized.flag_reason,
                latency_ms=(time.perf_counter() - total_start) * 1000,
                context_reference=str(finding.id)
            )
            return Response(
                {'error': 'Your query was flagged by our safety filters. Please rephrase your question.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 6. Apply ContextualScrubber to Evidence
        from ..safety import ContextualScrubber
        scrubber = ContextualScrubber()
        
        # We recursively scrub the evidence dict
        from ..safety import _recursive_scrub
        scrubbed_evidence = _recursive_scrub(finding.evidence, scrubber)
        
        # 6b. Query RAG retriever for relevant compliance corpus documents
        # Build search query from finding metadata for best relevance
        corpus_search_query = f"{finding.title} {finding.category}"
        corpus_results = []
        corpus_context_text = "No relevant compliance corpus documents were found for this finding."
        
        mode = request.session.get('ai_mode', 'ai')
        
        if mode != 'mock':
            try:
                retriever = _get_retriever()
                if retriever and retriever.is_ready():
                    corpus_search = retriever.search(corpus_search_query, top_k=3)
                    corpus_results = corpus_search.results
                    if corpus_results:
                        corpus_sections = []
                        for i, r in enumerate(corpus_results, 1):
                            corpus_sections.append(
                                f"[Source {i}: {r.filename}]\n{r.text[:800]}"
                            )
                        corpus_context_text = "\n\n".join(corpus_sections)
            except Exception as e:
                logger.warning(f"RAG retrieval failed for finding {finding.id}: {e}")

        # 7. Construct LLM Prompt (now with corpus context)
        import json
        prompt = FINDING_ASSISTANT_PROMPT.format(
            title=finding.title,
            status=finding.status,
            category=finding.category,
            why_it_matters=finding.why_it_matters or "N/A",
            remediation=finding.remediation or "N/A",
            evidence=json.dumps(scrubbed_evidence, indent=2),
            corpus_context=corpus_context_text,
            query=sanitized.text
        )

        # 8. Generation
        if mode == 'mock':
            from ..mock_service import MockResponseService
            mock_start = time.perf_counter()
            time.sleep(0.01) # Simulate LLM
            # Build a more contextual mock response using the finding and corpus
            corpus_hint = ""
            if corpus_results:
                corpus_hint = f"\n\nRelevant compliance sources consulted:\n" + "\n".join(
                    f"- **{r.filename}**: {r.text[:120]}..." for r in corpus_results
                )
            answer_text = (
                f"**Mock Remediation Guide for: {finding.title}**\n\n"
                f"**Root Cause:** This finding indicates a configuration gap in `{finding.category}` controls.\n\n"
                f"**Step-by-step Remediation:**\n"
                f"1. Review the scrubbed evidence provided above.\n"
                f"2. Apply the recommended configuration changes per CIS/NIST guidelines.\n"
                f"3. Validate the fix using your organization's change management process.\n"
                f"4. Re-run the AVAGuard scan to confirm resolution.\n"
                + corpus_hint
            )
            model_used = 'mock'
            is_fallback = True
            token_count = 80
            query_status = 'success'
            error_msg = ''
            provider_used = 'mock'
        else:
            # Full generation
            llm = _get_llm_service(ai_settings)
            
            # Since LLMService is a wrapper around orchestrator, we can access it directly.
            if hasattr(llm, 'orchestrator'):
                generation = llm.orchestrator.execute_prompt(
                    prompt=prompt,
                    model_name=ai_settings.model_name,
                    max_tokens=ai_settings.max_tokens,
                    temperature=ai_settings.temperature
                )
            else:
                # MockLLMService
                generation = llm.generate(sanitized.text, [prompt]) # Fallback behavior

            if generation.success:
                answer_text = validate_response(generation.text)
                query_status = 'success'
                error_msg = ''
            else:
                logger.error(f"Ask AI generation failed for {request.user.email}: {generation.error}")
                answer_text = 'I was unable to generate an answer at this time. Please try again later.'
                query_status = 'error'
                error_msg = generation.error

            model_used = generation.model
            is_fallback = getattr(generation, 'is_fallback', False)
            provider_used = getattr(generation, 'provider_used', 'unknown')
            token_count = getattr(generation, 'token_count', 0)

        # Build sources list from retrieved corpus results (same format as AIQueryView)
        sources = [
            {
                'filename': r.filename,
                'relative_path': r.relative_path,
                'score': round(r.reranker_score, 4),
                'text': r.text,
                'snippet': (r.text[:200] + '...') if len(r.text) > 200 else r.text,
                'reranker_score': round(r.reranker_score, 4),
                'hybrid_rank': r.hybrid_rank,
                'final_rank': i + 1,
                'metadata': r.metadata,
            }
            for i, r in enumerate(corpus_results)
        ]

        total_ms = (time.perf_counter() - total_start) * 1000

        # 9. Log Query
        log_entry = AIQueryLog.objects.create(
            user=request.user,
            organization=request.user.organization,
            query_text=raw_query,
            sanitized_query=sanitized.text,
            response_text=answer_text,
            model_used=model_used,
            provider_used=provider_used,
            is_fallback=is_fallback,
            latency_ms=total_ms,
            response_time_ms=int(total_ms),
            token_count=token_count,
            flagged=False,
            mode=mode,
            status=query_status,
            error_message=error_msg,
            context_reference=str(finding.id),
            transformation_metadata=scrubber.ip_map,
            retrieved_sources=sources,
            source_count=len(sources),
            chunks_retrieved=len(sources),
        )

        response_data = {
            'answer': answer_text,
            'sources': sources,
            'query_id': str(log_entry.id),
            'model_used': model_used,
            'latency_ms': round(total_ms, 2),
            'mode': mode,
        }

        return Response(response_data, status=status.HTTP_200_OK if query_status == 'success' else status.HTTP_500_INTERNAL_SERVER_ERROR)



class AIQueryHistoryPagination(PageNumberPagination):
    page_size = 20
    max_page_size = 100


class AIQueryHistoryView(APIView):
    """
    GET /api/ai/history/

    Returns the authenticated user's past AI queries, paginated.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = AIQueryLog.objects.filter(user=request.user).order_by('-created_at')

        paginator = AIQueryHistoryPagination()
        page = paginator.paginate_queryset(queryset, request)

        serializer = AIQueryLogSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)


# =====================================================================
# SuperAdmin AI Operational & Audit APIs (RBAC)
# =====================================================================

class IsSuperAdmin(IsAuthenticated):
    """Permission check: user must be authenticated AND have SUPER_ADMIN role."""

    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False
        return getattr(request.user, 'role', '') == 'SUPER_ADMIN'


class IsSuperAdminOrITAdmin(IsAuthenticated):
    """Permission check: SUPER_ADMIN or IT_ADMIN."""

    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False
        return getattr(request.user, 'role', '') in ('SUPER_ADMIN', 'IT_ADMIN')


class AISettingsView(APIView):
    """
    GET  /api/ai/admin/settings/  — View current AI settings for the user's org
    PUT  /api/ai/admin/settings/  — Update AI settings (SUPER_ADMIN only)
    """
    permission_classes = [IsSuperAdminOrITAdmin]

    def get(self, request):
        org = request.user.organization
        if not org:
            return Response({'error': 'No organization.'}, status=status.HTTP_403_FORBIDDEN)

        settings_obj, _ = AISettings.objects.get_or_create(organization=org)

        return Response({
            'is_enabled': settings_obj.is_enabled,
            'llm_provider': settings_obj.llm_provider,
            'model_name': settings_obj.model_name,
            'max_tokens': settings_obj.max_tokens,
            'temperature': settings_obj.temperature,
            'top_k_results': settings_obj.top_k_results,
            'daily_query_limit': settings_obj.daily_query_limit,
            'provider_choices': [
                {'value': c[0], 'label': c[1]}
                for c in AISettings.LLM_PROVIDER_CHOICES
            ],
            'updated_at': settings_obj.updated_at,
        })

    def put(self, request):
        # Write access is SUPER_ADMIN only
        if getattr(request.user, 'role', '') != 'SUPER_ADMIN':
            return Response(
                {'error': 'Only Super Administrators can modify AI settings.'},
                status=status.HTTP_403_FORBIDDEN
            )

        org = request.user.organization
        if not org:
            return Response({'error': 'No organization.'}, status=status.HTTP_403_FORBIDDEN)

        settings_obj, _ = AISettings.objects.get_or_create(organization=org)

        # Whitelist of updatable fields with validation
        ALLOWED_FIELDS = {
            'is_enabled': (bool,),
            'llm_provider': (str,),
            'model_name': (str,),
            'max_tokens': (int,),
            'temperature': (float, int),
            'top_k_results': (int,),
            'daily_query_limit': (int,),
        }

        changes = []
        for field, allowed_types in ALLOWED_FIELDS.items():
            if field in request.data:
                value = request.data[field]
                if not isinstance(value, allowed_types):
                    return Response(
                        {'error': f'Invalid type for {field}.'},
                        status=status.HTTP_400_BAD_REQUEST
                    )

                # Validate specific constraints
                if field == 'llm_provider':
                    valid_providers = [c[0] for c in AISettings.LLM_PROVIDER_CHOICES]
                    if value not in valid_providers:
                        return Response(
                            {'error': f'Invalid provider. Must be one of: {valid_providers}'},
                            status=status.HTTP_400_BAD_REQUEST
                        )
                elif field == 'max_tokens' and not (64 <= value <= 4096):
                    return Response(
                        {'error': 'max_tokens must be between 64 and 4096.'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                elif field == 'temperature' and not (0.0 <= float(value) <= 1.0):
                    return Response(
                        {'error': 'temperature must be between 0.0 and 1.0.'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                elif field == 'top_k_results' and not (1 <= value <= 20):
                    return Response(
                        {'error': 'top_k_results must be between 1 and 20.'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                elif field == 'daily_query_limit' and not (1 <= value <= 10000):
                    return Response(
                        {'error': 'daily_query_limit must be between 1 and 10000.'},
                        status=status.HTTP_400_BAD_REQUEST
                    )

                old_value = getattr(settings_obj, field)
                if old_value != value:
                    setattr(settings_obj, field, value)
                    changes.append(f'{field}: {old_value} → {value}')

        if changes:
            settings_obj.save()

            # Audit log the change
            AuditLog.log(
                action='POLICY_UPDATED',
                user=request.user,
                organization=org,
                details=f'AI settings updated: {"; ".join(changes)}',
            )

            logger.info(f"AI settings updated by {request.user.email}: {'; '.join(changes)}")

        return Response({
            'success': True,
            'changes': changes,
            'settings': {
                'is_enabled': settings_obj.is_enabled,
                'llm_provider': settings_obj.llm_provider,
                'model_name': settings_obj.model_name,
                'max_tokens': settings_obj.max_tokens,
                'temperature': settings_obj.temperature,
                'top_k_results': settings_obj.top_k_results,
                'daily_query_limit': settings_obj.daily_query_limit,
            }
        })


class AIAuditLogPagination(PageNumberPagination):
    page_size = 50
    max_page_size = 200


class AIAuditLogView(APIView):
    """
    GET /api/ai/admin/audit/

    View AI query audit logs for the organization. Read-only.
    Available to SUPER_ADMIN and IT_ADMIN.
    """
    permission_classes = [IsSuperAdminOrITAdmin]

    def get(self, request):
        org = request.user.organization
        if not org:
            return Response({'error': 'No organization.'}, status=status.HTTP_403_FORBIDDEN)

        queryset = AIQueryLog.objects.filter(
            organization=org
        ).select_related('user').order_by('-created_at')

        # Filtering
        flagged_only = request.query_params.get('flagged', '').lower() == 'true'
        if flagged_only:
            queryset = queryset.filter(flagged=True)

        user_email = request.query_params.get('user', '')
        if user_email:
            queryset = queryset.filter(user__email__icontains=user_email)

        mode = request.query_params.get('mode', '')
        if mode:
            queryset = queryset.filter(mode=mode)

        confidence = request.query_params.get('confidence', '')
        if confidence:
            queryset = queryset.filter(confidence_level=confidence)

        paginator = AIAuditLogPagination()
        page = paginator.paginate_queryset(queryset, request)

        results = []
        for log in page:
            results.append({
                'id': str(log.id),
                'user_email': log.user.email if log.user else 'unknown',
                'query_text': log.query_text,
                'response_text': log.response_text[:200] + '...' if len(log.response_text) > 200 else log.response_text,
                'model_used': log.model_used,
                'latency_ms': round(log.latency_ms, 2),
                'retrieval_ms': round(log.retrieval_ms, 2),
                'token_count': log.token_count,
                'sources_count': len(log.retrieved_sources) if isinstance(log.retrieved_sources, list) else 0,
                'flagged': log.flagged,
                'flag_reason': log.flag_reason,
                'mode': log.mode,
                'confidence_level': log.confidence_level,
                'created_at': log.created_at.isoformat(),
            })

        return paginator.get_paginated_response(results)


class AIStatsView(APIView):
    """
    GET /api/ai/admin/stats/

    Summary statistics for the AI system. Read-only.
    Includes health-check status for retriever and LLM provider.
    Available to SUPER_ADMIN and IT_ADMIN.
    """
    permission_classes = [IsSuperAdminOrITAdmin]

    def get(self, request):
        from django.conf import settings as django_settings

        org = request.user.organization
        if not org:
            return Response({'error': 'No organization.'}, status=status.HTTP_403_FORBIDDEN)

        today_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        org_logs = AIQueryLog.objects.filter(organization=org)

        total_queries = org_logs.count()
        queries_today = org_logs.filter(created_at__gte=today_start).count()
        flagged_queries = org_logs.filter(flagged=True, created_at__gte=today_start).count()
        fallback_queries = org_logs.filter(is_fallback=True, created_at__gte=today_start).count()

        # Average latency (last 100 queries)
        recent_latencies = org_logs.order_by('-created_at').values_list('latency_ms', flat=True)[:100]
        avg_latency = sum(recent_latencies) / len(recent_latencies) if recent_latencies else 0

        # AI settings
        try:
            ai_settings = AISettings.objects.get(organization=org)
            is_enabled = ai_settings.is_enabled
            daily_limit = ai_settings.daily_query_limit
            provider = ai_settings.llm_provider
            model_name = ai_settings.model_name
        except AISettings.DoesNotExist:
            is_enabled = False
            daily_limit = 0
            provider = 'unconfigured'
            model_name = ''

        # Health checks
        retriever = _get_retriever()
        retriever_ready = retriever.is_ready()
        retriever_type = 'mock' if isinstance(retriever, MockRetriever) else 'faiss'
        retriever_doc_count = retriever.document_count()

        api_key_present = bool(getattr(django_settings, 'AI_LLM_API_KEY', ''))

        # Confidence distribution
        confidence_distribution = {
            'high': org_logs.filter(confidence_level='high').count(),
            'medium': org_logs.filter(confidence_level='medium').count(),
            'low': org_logs.filter(confidence_level='low').count(),
            'none': org_logs.filter(confidence_level='none').count(),
        }

        # Empty retrieval rate / count
        empty_retrieval_count = org_logs.filter(retrieved_document_count=0).count()

        # Average reranker / similarity scores (last 100 queries)
        recent_scores = org_logs.filter(average_similarity_score__isnull=False).order_by('-created_at').values_list('average_similarity_score', flat=True)[:100]
        avg_reranker_score = sum(recent_scores) / len(recent_scores) if recent_scores else 0.0

        recent_top_scores = org_logs.filter(top_similarity_score__isnull=False).order_by('-created_at').values_list('top_similarity_score', flat=True)[:100]
        avg_retrieval_score = sum(recent_top_scores) / len(recent_top_scores) if recent_top_scores else 0.0

        # Success rate
        retrieval_success_rate = 100.0
        if total_queries > 0:
            retrieval_success_rate = round(((total_queries - empty_retrieval_count) / total_queries) * 100, 2)

        # Corpus stats from retriever
        corpus_stats = {}
        if retriever_ready:
            metadata = retriever.index_metadata()
            corpus_stats = {
                'total_documents': metadata.get('total_documents', 0),
                'total_chunks': metadata.get('total_chunks', 0),
                'model_name': metadata.get('model_name', ''),
                'chunk_size': metadata.get('chunk_size', 0),
                'chunk_overlap': metadata.get('chunk_overlap', 0),
                'files_by_framework': metadata.get('files_by_framework', {}),
            }

        # Feedback metrics
        feedback_total = AIQueryFeedback.objects.filter(
            query_log__organization=org
        ).count()
        feedback_up = AIQueryFeedback.objects.filter(
            query_log__organization=org, rating='up'
        ).count()
        feedback_down = feedback_total - feedback_up
        avg_feedback = round((feedback_up / feedback_total * 100), 1) if feedback_total > 0 else 0.0

        # Cache hit rate
        cache_hits = org_logs.filter(retrieval_method='cache').count()
        cache_hit_rate = round((cache_hits / total_queries * 100), 1) if total_queries > 0 else 0.0

        # Available frameworks
        available_frameworks = []
        if retriever_ready and hasattr(retriever, 'available_frameworks'):
            available_frameworks = retriever.available_frameworks()

        return Response({
            'total_queries': total_queries,
            'queries_today': queries_today,
            'daily_limit': daily_limit,
            'flagged_queries': flagged_queries,
            'fallback_queries': fallback_queries,
            'avg_latency_ms': round(avg_latency, 2),
            'is_enabled': is_enabled,
            'confidence_distribution': confidence_distribution,
            'empty_retrieval_count': empty_retrieval_count,
            'avg_retrieval_score': round(avg_retrieval_score, 4),
            'avg_reranker_score': round(avg_reranker_score, 4),
            'retrieval_success_rate': retrieval_success_rate,
            'corpus_stats': corpus_stats,
            'available_frameworks': available_frameworks,
            'feedback': {
                'total': feedback_total,
                'up': feedback_up,
                'down': feedback_down,
                'avg_rating': avg_feedback,
            },
            'cache_hit_rate': cache_hit_rate,
            'health': {
                'retriever_status': 'ready' if retriever_ready else 'unavailable',
                'retriever_type': retriever_type,
                'retriever_doc_count': retriever_doc_count,
                'llm_provider': provider,
                'llm_model': model_name,
                'api_key_configured': api_key_present,
            },
        })

class SetAIModeView(APIView):
    """
    POST /api/ai/set-mode/
    Toggles the user session between 'mock' and 'ai' modes.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        mode = request.data.get('mode')
        if mode not in ['mock', 'ai']:
            return Response(
                {'error': 'Invalid mode. Must be "mock" or "ai".'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        request.session['ai_mode'] = mode
        return Response({'status': 'ok', 'mode': mode})


class AIRetrievalInspectView(APIView):
    """
    POST /api/ai/admin/inspect/

    Runs a query through the full retrieval pipeline and returns
    detailed instrumentation WITHOUT logging it as a real query.
    Used by the Retrieval Inspector debug page.
    """
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsSuperAdminOrITAdmin()]

    def post(self, request):
        query = request.data.get('query', '').strip()
        if not query:
            return Response(
                {'error': 'Query is required.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        from ..safety import sanitize_query
        sanitized = sanitize_query(query)

        retriever = _get_retriever()
        if not retriever.is_ready():
            return Response(
                {'error': 'Retriever is not ready. Build the FAISS index first.'},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )

        # Run full pipeline with optional framework filter
        framework_filter = request.data.get('framework', '').strip() or None
        search_result = retriever.search(
            sanitized.text, top_k=10,
            framework_filter=framework_filter,
        )

        # Build detailed response
        chunks_detail = []
        for r in search_result.results:
            chunks_detail.append({
                'filename': r.filename,
                'relative_path': r.relative_path,
                'word_count': r.word_count,
                'hybrid_rank': r.hybrid_rank,
                'reranker_score': round(r.reranker_score, 4),
                'final_rank': r.final_rank,
                'snippet': r.text[:300] + '...' if len(r.text) > 300 else r.text,
                'metadata': r.metadata,
            })

        return Response({
            'query': query,
            'sanitized_query': sanitized.text,
            'is_safe': sanitized.is_safe,
            'confidence': search_result.confidence,
            'retrieval_ms': round(search_result.retrieval_ms, 2),
            'rerank_ms': round(search_result.rerank_ms, 2),
            'total_candidates': search_result.total_candidates,
            'avg_reranker_score': search_result.avg_reranker_score,
            'top_reranker_score': search_result.top_reranker_score,
            'framework_filter': framework_filter or '',
            'chunks': chunks_detail,
        })

    def get(self, request):
        """Load a historical query by ID for inspection."""
        query_id = request.query_params.get('query_id')
        if not query_id:
            return Response(
                {'error': 'query_id parameter required.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            log = AIQueryLog.objects.get(id=query_id)
        except AIQueryLog.DoesNotExist:
            return Response(
                {'error': 'Query not found.'},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Security check: check access based on user roles
        user_role = getattr(request.user, 'role', '')
        if user_role == 'SUPER_ADMIN':
            pass
        elif user_role == 'IT_ADMIN':
            if log.organization != request.user.organization:
                return Response(
                    {'error': 'Unauthorized to inspect this query.'},
                    status=status.HTTP_403_FORBIDDEN,
                )
        else:
            if log.user != request.user:
                return Response(
                    {'error': 'Unauthorized to inspect this query.'},
                    status=status.HTTP_403_FORBIDDEN,
                )

        return Response({
            'query': log.query_text,
            'sanitized_query': log.sanitized_query,
            'response_text': log.response_text,
            'answer': log.response_text,  # Compatibility alias
            'model_used': log.model_used,
            'mode': log.mode,
            'confidence': log.confidence_level,
            'retrieval_ms': round(log.retrieval_ms, 2),
            'rerank_ms': round(log.rerank_latency_ms or 0, 2),
            'latency_ms': round(log.latency_ms, 2),
            'token_count': log.token_count,
            'sources': log.retrieved_sources,
            'reranker_scores': log.reranker_scores,
            'avg_reranker_score': log.average_similarity_score,
            'top_reranker_score': log.top_similarity_score,
            'created_at': log.created_at.isoformat(),
            'flagged': log.flagged,
            'flag_reason': log.flag_reason,
        })


class AIFeedbackView(APIView):
    """
    POST /api/ai/feedback/

    Submit thumbs-up/down feedback on a query response.
    Links to AIQueryFeedback model (OneToOne with AIQueryLog).
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        query_id = request.data.get('query_id')
        rating = request.data.get('rating')
        comment = request.data.get('comment', '')

        if not query_id or rating not in ('up', 'down'):
            return Response(
                {'error': 'query_id and rating (up/down) are required.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            log = AIQueryLog.objects.get(id=query_id)
        except AIQueryLog.DoesNotExist:
            return Response(
                {'error': 'Query not found.'},
                status=status.HTTP_404_NOT_FOUND,
            )

        needs_review = (rating == 'down' and bool(comment.strip()))

        feedback, created = AIQueryFeedback.objects.update_or_create(
            query_log=log,
            defaults={
                'rating': rating,
                'comment': comment,
                'needs_review': needs_review,
                'submitted_by': request.user,
            }
        )

        return Response({
            'status': 'ok',
            'created': created,
            'rating': rating,
            'needs_review': needs_review,
        })


class AIFeedbackResolveView(APIView):
    """
    POST /api/ai/admin/feedback/resolve/

    Mark a negative feedback query log as resolved (sets needs_review=False).
    SuperAdmin and ITAdmin only.
    """
    permission_classes = [IsSuperAdminOrITAdmin]

    def post(self, request):
        feedback_id = request.data.get('feedback_id')
        if not feedback_id:
            return Response(
                {'error': 'feedback_id is required.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            feedback = AIQueryFeedback.objects.get(id=feedback_id)
        except AIQueryFeedback.DoesNotExist:
            return Response(
                {'error': 'Feedback not found.'},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Scope check: IT_ADMIN can only resolve feedback for their own organization.
        # SUPER_ADMIN can resolve feedback globally.
        if getattr(request.user, 'role', '') != 'SUPER_ADMIN':
            org = request.user.organization
            if feedback.query_log.organization != org:
                return Response(
                    {'error': 'Unauthorized to resolve this feedback.'},
                    status=status.HTTP_403_FORBIDDEN,
                )

        feedback.needs_review = False
        feedback.save()

        # Audit log the resolution
        AuditLog.log(
            action='POLICY_UPDATED',
            user=request.user,
            organization=feedback.query_log.organization,
            details=f'AI feedback resolve: {feedback_id} resolved.',
        )

        return Response({
            'status': 'ok',
            'feedback_id': feedback_id,
            'needs_review': False,
        })


class AIDocumentContentView(APIView):
    """
    GET /api/ai/document/content/

    Returns the full text of a raw corpus document from disk.
    Accessible to all authenticated users.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        relative_path = request.query_params.get('relative_path', '').strip()
        if not relative_path:
            return Response(
                {'error': 'relative_path parameter required.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Normalize paths
        relative_path = relative_path.replace('\\', '/')
        corpus_dir = Path(settings.AI_CORPUS_DIR)
        fpath = (corpus_dir / relative_path).resolve()

        # Security check: check path traversal
        if not str(fpath).startswith(str(corpus_dir.resolve())):
            return Response(
                {'error': 'Unauthorized file path access.'},
                status=status.HTTP_403_FORBIDDEN,
            )

        if not fpath.exists():
            return Response(
                {'error': 'Document not found.'},
                status=status.HTTP_404_NOT_FOUND,
            )

        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            return Response({'content': content})
        except Exception as e:
            return Response(
                {'error': f'Failed to read document: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class AIClearCacheView(APIView):
    """
    POST /api/ai/admin/clear-cache/

    Clears the global Django cache (which caches AI query responses).
    Available to SuperAdmins and ITAdmins.
    """
    permission_classes = [IsSuperAdminOrITAdmin]

    def post(self, request):
        from django.core.cache import cache
        try:
            cache.clear()
            # Log audit trail
            AuditLog.log(
                action='POLICY_UPDATED',
                user=request.user,
                organization=request.user.organization,
                details='AI query cache cleared manually.',
            )
            return Response({'status': 'ok', 'message': 'Query cache cleared successfully.'})
        except Exception as e:
            return Response(
                {'error': f'Failed to clear cache: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


