"""
AVAGuard AI Operations — LLM Generation Service

Modular provider architecture supporting automatic failover,
strict abstraction, and non-RAG contexts.
"""

import time
import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional, Dict, Any

logger = logging.getLogger(__name__)

# Server-side only grounding prompt for RAG.
GROUNDING_PROMPT = """You are a compliance assistant for AVAGuard. Answer the user's question using ONLY the provided context. If the context does not contain enough information to answer the question, say "I don't have enough information to answer this question based on the available compliance documents."

Do not use any external knowledge. Do not make up information. Cite the source document filenames when possible.

Context:
{context}

Question: {query}"""

# Server-side prompt for finding remediation (Phase 5A + 5B RAG-enhanced)
FINDING_ASSISTANT_PROMPT = """You are an expert AVAGuard Security Engineer. Analyze the provided security finding, its associated evidence, and the relevant compliance corpus documents, then provide a clear, actionable remediation plan.

Rules:
1. Provide concrete, step-by-step instructions.
2. If the evidence contains configurations, reference them specifically but safely.
3. When compliance corpus documents are provided, reference their filenames as sources for your recommendations.
4. Be concise and professional.
5. Do not output markdown code blocks unless providing a command or config snippet.
6. Do NOT hallucinate. Rely strictly on the provided context.

Finding Context:
Title: {title}
Status: {status}
Category: {category}
Why It Matters: {why_it_matters}
Current Remediation Advice: {remediation}

Scrubbed Evidence:
{evidence}

Relevant Compliance Corpus Documents:
{corpus_context}

Question: {query}"""


@dataclass
class GenerationResult:
    """Result from LLM generation."""
    text: str
    model: str
    token_count: int = 0
    latency_ms: float = 0.0
    success: bool = True
    error: str = ''
    is_fallback: bool = False
    provider_used: str = ''


class BaseLLMProvider(ABC):
    """Abstract base class for all LLM providers."""
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Provider identifier (e.g., 'deepseek', 'grok')"""
        pass

    @abstractmethod
    def generate(self, prompt: str, model_name: str, max_tokens: int, temperature: float) -> GenerationResult:
        """Execute the prompt and return the result."""
        pass


class DeepSeekProvider(BaseLLMProvider):
    def __init__(self, api_key: str, timeout: int = 30):
        self.api_key = api_key
        self.timeout = timeout

    @property
    def name(self) -> str:
        return 'deepseek'

    def generate(self, prompt: str, model_name: str, max_tokens: int, temperature: float) -> GenerationResult:
        try:
            from openai import OpenAI
        except ImportError:
            return GenerationResult(text='', model=model_name, success=False, error='openai package missing', provider_used=self.name)

        if not self.api_key:
            return GenerationResult(text='', model=model_name, success=False, error='Missing API key', provider_used=self.name)

        start = time.perf_counter()
        try:
            client = OpenAI(api_key=self.api_key, base_url='https://api.deepseek.com', timeout=self.timeout)
            response = client.chat.completions.create(
                model=model_name,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=temperature,
            )
            latency = (time.perf_counter() - start) * 1000
            return GenerationResult(
                text=response.choices[0].message.content or '',
                model=model_name,
                token_count=response.usage.completion_tokens if response.usage else 0,
                latency_ms=latency,
                success=True,
                provider_used=self.name
            )
        except Exception as e:
            latency = (time.perf_counter() - start) * 1000
            return GenerationResult(text='', model=model_name, latency_ms=latency, success=False, error=str(e), provider_used=self.name)


class GrokProvider(BaseLLMProvider):
    def __init__(self, api_key: str, timeout: int = 30):
        self.api_key = api_key
        self.timeout = timeout

    @property
    def name(self) -> str:
        return 'grok'

    def generate(self, prompt: str, model_name: str, max_tokens: int, temperature: float) -> GenerationResult:
        try:
            from openai import OpenAI
        except ImportError:
            return GenerationResult(text='', model=model_name, success=False, error='openai package missing', provider_used=self.name)

        if not self.api_key:
            return GenerationResult(text='', model=model_name, success=False, error='Missing API key', provider_used=self.name)

        start = time.perf_counter()
        try:
            client = OpenAI(api_key=self.api_key, base_url='https://api.x.ai/v1', timeout=self.timeout)
            response = client.chat.completions.create(
                model=model_name,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=temperature,
            )
            latency = (time.perf_counter() - start) * 1000
            return GenerationResult(
                text=response.choices[0].message.content or '',
                model=model_name,
                token_count=response.usage.completion_tokens if response.usage else 0,
                latency_ms=latency,
                success=True,
                provider_used=self.name
            )
        except Exception as e:
            latency = (time.perf_counter() - start) * 1000
            return GenerationResult(text='', model=model_name, latency_ms=latency, success=False, error=str(e), provider_used=self.name)


class MockProvider(BaseLLMProvider):
    @property
    def name(self) -> str:
        return 'mock'

    def generate(self, prompt: str, model_name: str, max_tokens: int, temperature: float) -> GenerationResult:
        start = time.perf_counter()
        time.sleep(0.01) # Simulate latency
        latency = (time.perf_counter() - start) * 1000
        
        answer = "This is a deterministic response from the MockProvider. The system successfully failed over to this provider, maintaining uptime and stability."
        
        return GenerationResult(
            text=answer,
            model='mock',
            token_count=len(answer.split()),
            latency_ms=latency,
            success=True,
            is_fallback=True,
            provider_used=self.name
        )


class LLMOrchestrator:
    """
    Central entry point for all LLM interactions.
    Handles cascading provider failover automatically.
    """
    def __init__(self, providers: List[BaseLLMProvider]):
        self.providers = providers

    def execute_prompt(self, prompt: str, model_name: str = 'deepseek-chat', max_tokens: int = 1024, temperature: float = 0.1) -> GenerationResult:
        """Execute a raw prompt, failing over sequentially if needed."""
        last_error = "No providers configured."
        
        for provider in self.providers:
            # Overwrite model name for Grok to ensure compatibility if falling back from DeepSeek
            current_model = model_name
            if provider.name == 'grok' and 'deepseek' in current_model:
                current_model = 'grok-beta'
                
            logger.info(f"Attempting generation with provider: {provider.name}")
            result = provider.generate(prompt, current_model, max_tokens, temperature)
            
            if result.success:
                return result
            
            logger.warning(f"Provider {provider.name} failed: {result.error}. Failing over...")
            last_error = result.error
            
        return GenerationResult(
            text='',
            model=model_name,
            success=False,
            error=f"All configured providers failed. Last error: {last_error}",
            provider_used='none'
        )

    # ── Compatibility layer for existing RAG calls ──
    def generate(self, query: str, context_chunks: List[str], model_name: str = 'gpt-4o-mini', max_tokens: int = 1024, temperature: float = 0.1) -> GenerationResult:
        context_text = "\n\n---\n\n".join(context_chunks)
        prompt = GROUNDING_PROMPT.format(context=context_text, query=query)
        return self.execute_prompt(prompt, model_name, max_tokens, temperature)


class ProviderFactory:
    """Dynamically instantiates providers based on strings to decouple views from classes."""
    _registry = {
        'deepseek': DeepSeekProvider,
        'grok': GrokProvider,
        'mock': MockProvider,
    }

    @classmethod
    def get_orchestrator(cls, provider_names: List[str], api_keys: Dict[str, str] = None) -> LLMOrchestrator:
        api_keys = api_keys or {}
        providers = []
        for name in provider_names:
            if name in cls._registry:
                # Provide api key if the constructor takes it
                if name == 'mock':
                    providers.append(cls._registry[name]())
                else:
                    key = api_keys.get(name, '')
                    providers.append(cls._registry[name](api_key=key))
        return LLMOrchestrator(providers)


# =====================================================================
# Legacy Compatibility Wrappers (Do Not Remove)
# These prevent ImportError in api_views.py for existing RAG pipelines
# =====================================================================

class LLMService:
    """Compatibility Wrapper for legacy api_views.py that expects the old LLMService signature."""
    def __init__(self, api_key: str, provider: str = 'deepseek', timeout: int = 30):
        # We wrap the requested provider in an orchestrator chain
        # If the requested provider fails, it will automatically fallback to mock
        chain = [provider, 'mock']
        api_keys = {provider: api_key}
        self.orchestrator = ProviderFactory.get_orchestrator(chain, api_keys)

    def generate(self, query: str, context_chunks: List[str], model_name: str = 'gpt-4o-mini', max_tokens: int = 1024, temperature: float = 0.1) -> GenerationResult:
        """Transparently pass the call to the Orchestrator's compatibility method."""
        return self.orchestrator.generate(query, context_chunks, model_name, max_tokens, temperature)


class MockLLMService:
    """Compatibility Wrapper for legacy api_views.py that expects the old MockLLMService signature."""
    def __init__(self):
        pass

    def generate(self, query: str, context_chunks: List[str], model_name: str = 'mock', max_tokens: int = 1024, temperature: float = 0.1) -> GenerationResult:
        """Legacy mock implementation to satisfy test suite."""
        start = time.perf_counter()
        time.sleep(0.01)
        latency = (time.perf_counter() - start) * 1000
        
        if not context_chunks:
            answer = "I don't have enough information to answer this question based on the available compliance documents."
        else:
            answer = f"This is a mock answer based on the provided context. Evaluated query: {query}"
            
        return GenerationResult(
            text=answer,
            model='mock',
            token_count=len(answer.split()),
            latency_ms=latency,
            success=True,
            provider_used='mock',
            is_fallback=True
        )
