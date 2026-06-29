"""
AVAGuard AI Operations — User UI Views
"""

from pathlib import Path
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from ..models import AISettings, AIQueryLog


@login_required
def ai_query(request):
    """
    Renders the interactive AI Compliance Q&A console.
    Uses ai_query.html — full interface with mode toggle, framework filter,
    source cards, feedback, and query history sidebar.
    """
    from ..views.api_views import _get_retriever
    org = request.user.organization
    ai_settings = None
    if org:
        ai_settings, _ = AISettings.objects.get_or_create(organization=org)

    # Get current mode from session (default to 'ai')
    mode = request.session.get('ai_mode', 'ai')

    # Get available frameworks from the retriever for the dropdown
    available_frameworks = []
    try:
        retriever = _get_retriever()
        if retriever and retriever.is_ready():
            available_frameworks = retriever.available_frameworks()
    except Exception:
        pass

    # Recent queries for the history sidebar (last 10)
    recent_queries = AIQueryLog.objects.filter(
        user=request.user
    ).order_by('-created_at')[:10]

    context = {
        'active_page': 'ai_query',
        'ai_settings': ai_settings,
        'mode': mode,
        'available_frameworks': available_frameworks,
        'recent_queries': recent_queries,
    }
    return render(request, 'ai_ops/ai_query.html', context)


@login_required
def ai_history(request):
    """
    Renders the authenticated user's personal query history page.
    """
    # Fetch initial page size, but Javascript pagination will fetch complete details.
    logs = AIQueryLog.objects.filter(user=request.user).order_by('-created_at')[:20]

    context = {
        'active_page': 'ai_history',
        'initial_logs': logs,
    }
    return render(request, 'ai_ops/history.html', context)


@login_required
def ai_rag_status(request):
    """
    Renders the RAG System Health page.
    Shows index file inventory, corpus coverage, model config, and build commands.
    SUPER_ADMIN and IT_ADMIN only.
    """
    from core.admin_views import role_required
    from ..views.api_views import _get_retriever
    import os

    # Role check inline (avoids circular import with decorator)
    user_role = getattr(request.user, 'role', '')
    if user_role not in ('SUPER_ADMIN', 'IT_ADMIN'):
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden('Restricted to SUPER_ADMIN and IT_ADMIN.')

    index_dir_setting = getattr(settings, 'AI_INDEX_DIR', None)
    if not index_dir_setting:
        project_root = getattr(settings, 'PROJECT_ROOT', Path('.'))
        index_dir = Path(project_root) / 'rag-train' / 'll-finetuning' / 'rag' / 'faiss_index'
    else:
        index_dir = Path(index_dir_setting)

    # Index file inventory
    file_defs = [
        ('faiss.index',          'FAISS vector index — dense search'),
        ('meta.pkl',             'Metadata store — documents, texts, framework tags'),
        ('bm25.pkl',             'Serialised BM25 index — keyword search (fast startup)'),
        ('incremental_cache.pkl','Incremental build cache — SHA-256 hashes per file'),
    ]
    index_files = []
    max_size = 1
    for fname, purpose in file_defs:
        fpath = index_dir / fname
        size = fpath.stat().st_size if fpath.exists() else 0
        if size > max_size:
            max_size = size
        index_files.append({
            'name': fname, 'purpose': purpose,
            'exists': fpath.exists(),
            'size_bytes': size,
            'size_human': _human_size(size),
            'bar_width': 0,  # Will be computed after max_size is known
        })
    # Compute proportional bar widths (max 180px)
    for f in index_files:
        f['bar_width'] = int((f['size_bytes'] / max_size) * 180) if max_size > 0 else 0

    # Retriever state
    retriever_ready = False
    corpus_stats = {}
    bm25_source = None
    built_at_display = 'Unknown'
    try:
        retriever = _get_retriever()
        if retriever and retriever.is_ready():
            retriever_ready = True
            corpus_stats = retriever.index_metadata()
            built_at = corpus_stats.get('built_at', '')
            if built_at:
                from datetime import datetime
                try:
                    dt = datetime.fromisoformat(str(built_at))
                    built_at_display = dt.strftime('%d %b %Y %H:%M')
                except Exception:
                    built_at_display = str(built_at)[:16]
            bm25_source = 'disk' if (index_dir / 'bm25.pkl').exists() else 'memory'
    except Exception:
        pass

    reranker_model = getattr(settings, 'AI_RERANKER_MODEL', 'cross-encoder/ms-marco-MiniLM-L-6-v2')

    context = {
        'active_page': 'ai_rag_status',
        'retriever_ready': retriever_ready,
        'corpus_stats': corpus_stats,
        'index_files': index_files,
        'bm25_source': bm25_source,
        'built_at_display': built_at_display,
        'reranker_model': reranker_model,
    }
    return render(request, 'ai_ops/rag_status.html', context)


def _human_size(size_bytes):
    """Human-readable file size."""
    for unit in ('B', 'KB', 'MB', 'GB'):
        if size_bytes < 1024:
            return f'{size_bytes:.0f} {unit}'
        size_bytes /= 1024
    return f'{size_bytes:.1f} GB'


@login_required
def ai_document_view(request, relative_path):
    """
    Renders a dedicated page for viewing raw corpus document contents and metadata.
    """
    # Normalize path separators
    relative_path = relative_path.replace('\\', '/')
    corpus_dir = Path(settings.AI_CORPUS_DIR)
    fpath = (corpus_dir / relative_path).resolve()

    # Security: check path traversal
    if not str(fpath).startswith(str(corpus_dir.resolve())):
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden("Access Denied")

    if not fpath.exists():
        from django.http import Http404
        raise Http404("Document not found")

    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        content = f"Failed to read document content: {str(e)}"

    # Get metadata if index is loaded
    from ..views.api_views import _get_retriever
    doc_metadata = {}
    total_matching_chunks = 0
    try:
        retriever = _get_retriever()
        if retriever and retriever.is_ready():
            documents = retriever._metadata.get('documents', [])
            matching_chunks = [
                doc for doc in documents 
                if doc.get('relative_path') == relative_path
            ]
            if matching_chunks:
                # Merge or take first
                doc_metadata = matching_chunks[0]
                total_matching_chunks = len(matching_chunks)
    except Exception:
        pass

    context = {
        'active_page': 'ai_query',  # keep active nav item
        'filename': fpath.name,
        'relative_path': relative_path,
        'content': content,
        'metadata': doc_metadata,
        'total_matching_chunks': total_matching_chunks,
    }
    return render(request, 'ai_ops/document_view.html', context)
