"""
AVAGuard Security AI - Multi-LLM API Client
Unified wrapper for 10 LLM providers with automatic failover, retry, and multi-key rotation.
"""

import os
import time
import json
import logging
from typing import Optional

from synthetic_data_generator.config import (
    API_PROVIDERS, get_api_key, get_api_keys, get_available_providers,
    GENERATION_CONFIG
)

logger = logging.getLogger("avaguard.api_clients")


class MultiLLMClient:
    """
    Unified client for ALL free LLM APIs with automatic failover and multi-key rotation.
    
    Features:
        - Automatic failover: if one provider fails, tries the next
        - Multi-key rotation: cycle through multiple API keys per provider
        - Smart retry with exponential backoff
    
    Usage:
        client = MultiLLMClient()
        response = client.call("gemini", "What is Azure AD?", system_prompt="You are an expert.")
    """

    def __init__(self, tracker=None):
        self.clients = {}
        self._tracker = tracker  # Optional: for auto-disabling failed providers
        self._init_all_providers()

    def _init_all_providers(self):
        """Initialize all providers that have API keys set."""
        available = get_available_providers()
        
        if not available:
            logger.warning("⚠️  No API keys configured! Copy config/.env.example to config/.env and add your keys.")
            return

        for provider in available:
            try:
                self._init_provider(provider)
                keys = get_api_keys(provider)
                key_info = f" ({len(keys)} keys)" if len(keys) > 1 else ""
                logger.info(f"✅ {provider.upper()} initialized ({API_PROVIDERS[provider]['model']}){key_info}")
            except Exception as e:
                logger.warning(f"⚠️  {provider.upper()} init failed: {e}")

    def _init_provider(self, provider: str):
        """Initialize a specific provider client."""
        config = API_PROVIDERS[provider]
        keys = get_api_keys(provider)
        
        if not keys:
            raise ValueError(f"No API key for {provider}")

        ptype = config["type"]
        api_key = keys[0]  # Use first key for initialization

        if ptype == "google":
            from google import genai
            # Store all keys for rotation
            self.clients[provider] = {
                "type": "google",
                "keys": keys,
                "current_key_idx": 0,
                "model_name": config["model"]
            }

        elif ptype == "anthropic":
            from anthropic import Anthropic
            client = Anthropic(api_key=api_key)
            self.clients[provider] = {
                "type": "anthropic",
                "client": client,
                "keys": keys,
                "current_key_idx": 0,
                "model_name": config["model"]
            }

        elif ptype == "openai_native":
            from openai import OpenAI
            client = OpenAI(api_key=api_key)
            self.clients[provider] = {
                "type": "openai",
                "client": client,
                "keys": keys,
                "current_key_idx": 0,
                "model_name": config["model"]
            }

        elif ptype == "openai_compatible":
            from openai import OpenAI
            client = OpenAI(
                api_key=api_key,
                base_url=config.get("base_url", "")
            )
            self.clients[provider] = {
                "type": "openai",
                "client": client,
                "base_url": config.get("base_url", ""),
                "keys": keys,
                "current_key_idx": 0,
                "model_name": config["model"]
            }

        elif ptype == "cohere":
            try:
                import cohere
                client = cohere.ClientV2(api_key=api_key)
                self.clients[provider] = {
                    "type": "cohere",
                    "client": client,
                    "keys": keys,
                    "current_key_idx": 0,
                    "model_name": config["model"]
                }
            except ImportError:
                logger.warning("Cohere SDK not installed. Run: pip install cohere")

    def _rotate_key(self, provider: str) -> bool:
        """Rotate to the next available API key for a provider.
        
        Returns True if a new key was selected, False if we've cycled through all keys.
        """
        info = self.clients[provider]
        keys = info.get("keys", [])
        if len(keys) <= 1:
            return False
        
        old_idx = info["current_key_idx"]
        new_idx = (old_idx + 1) % len(keys)
        
        if new_idx == 0:
            # We've cycled through all keys
            return False
        
        info["current_key_idx"] = new_idx
        new_key = keys[new_idx]
        ptype = info["type"]
        
        logger.info(f"🔄 {provider.upper()} rotating to key #{new_idx + 1}/{len(keys)}")
        
        # Re-initialize client with new key
        if ptype == "google":
            pass  # Google genai uses key per-call, handled in _call_google
        elif ptype == "openai":
            from openai import OpenAI
            base_url = info.get("base_url")
            if base_url:
                info["client"] = OpenAI(api_key=new_key, base_url=base_url)
            else:
                info["client"] = OpenAI(api_key=new_key)
        elif ptype == "anthropic":
            from anthropic import Anthropic
            info["client"] = Anthropic(api_key=new_key)
        elif ptype == "cohere":
            import cohere
            info["client"] = cohere.ClientV2(api_key=new_key)
        
        return True

    def call(
        self,
        provider: str,
        prompt: str,
        system_prompt: str = "",
        temperature: float = 0.7,
        max_tokens: int = 2000
    ) -> Optional[str]:
        """
        Call a specific provider with automatic fallback and key rotation.
        
        Args:
            provider: Primary provider to use (e.g., 'gemini', 'deepseek')
            prompt: User message / prompt
            system_prompt: System instruction
            temperature: Creativity (0.0 - 1.0)
            max_tokens: Maximum response length
            
        Returns:
            Generated text response, or None if all providers fail
        """
        # Build fallback chain
        fallback_chain = [provider]
        for p in sorted(API_PROVIDERS.keys(), key=lambda x: API_PROVIDERS[x]["priority"]):
            if p != provider and p in self.clients:
                fallback_chain.append(p)

        last_error = None
        for attempt_provider in fallback_chain:
            if attempt_provider not in self.clients:
                continue

            # Reset key index for each provider attempt
            self.clients[attempt_provider]["current_key_idx"] = 0

            for attempt in range(GENERATION_CONFIG["retry_attempts"]):
                try:
                    result = self._call_provider(
                        attempt_provider, prompt, system_prompt,
                        temperature, max_tokens
                    )
                    if result and result.strip():
                        if attempt_provider != provider:
                            logger.info(f"   ↪ Used fallback: {attempt_provider}")
                        return result
                except Exception as e:
                    last_error = e
                    error_str = str(e).lower()
                    
                    # Check if this is a PERMANENT error (no credits, account issue)
                    is_permanent = any(kw in error_str for kw in [
                        "insufficient balance", "payment required", "402",
                        "credit balance is too low", "billing",
                        "account_deactivated", "authentication_error"
                    ])
                    
                    if is_permanent:
                        logger.warning(f"🚫 {attempt_provider}: Permanent error detected. Skipping.")
                        if self._tracker:
                            self._tracker.disable_provider(attempt_provider, str(e)[:100])
                        break  # Move to next provider immediately
                    
                    # Check if error is quota/rate-limit related → try key rotation
                    is_quota_error = any(kw in error_str for kw in [
                        "quota", "rate_limit", "429", "too many", "exceeded", "resource_exhausted"
                    ])
                    
                    if is_quota_error and self._rotate_key(attempt_provider):
                        logger.info(f"   ↪ Retrying with rotated key...")
                        continue
                    
                    delay = GENERATION_CONFIG["retry_delay_base"] ** (attempt + 1)
                    logger.warning(
                        f"⚠️  {attempt_provider} attempt {attempt+1} failed: {e}. "
                        f"Retrying in {delay}s..."
                    )
                    time.sleep(delay)

        logger.error(f"❌ All providers failed. Last error: {last_error}")
        return None

    def _call_provider(
        self, provider: str, prompt: str,
        system_prompt: str, temperature: float, max_tokens: int
    ) -> str:
        """Route to the correct provider handler."""
        info = self.clients[provider]
        ptype = info["type"]

        if ptype == "google":
            return self._call_google(info, prompt, system_prompt, temperature, max_tokens)
        elif ptype == "anthropic":
            return self._call_anthropic(info, prompt, system_prompt, temperature, max_tokens)
        elif ptype == "openai":
            return self._call_openai(info, prompt, system_prompt, temperature, max_tokens)
        elif ptype == "cohere":
            return self._call_cohere(info, prompt, system_prompt, temperature, max_tokens)
        else:
            raise ValueError(f"Unknown provider type: {ptype}")

    # ── Provider-Specific Handlers ──────────────────────────────────

    def _call_google(self, info, prompt, system_prompt, temperature, max_tokens):
        """Call Google Gemini API using the new google.genai SDK."""
        from google import genai
        from google.genai import types
        
        # Use current key from rotation
        current_key = info["keys"][info["current_key_idx"]]
        client = genai.Client(api_key=current_key)
        model_name = info["model_name"]

        config = types.GenerateContentConfig(
            temperature=temperature,
            max_output_tokens=max_tokens,
        )
        if system_prompt:
            config.system_instruction = system_prompt

        response = client.models.generate_content(
            model=model_name,
            contents=prompt,
            config=config
        )
        return response.text

    def _call_anthropic(self, info, prompt, system_prompt, temperature, max_tokens):
        """Call Anthropic Claude API."""
        client = info["client"]
        response = client.messages.create(
            model=info["model_name"],
            max_tokens=max_tokens,
            temperature=temperature,
            system=system_prompt if system_prompt else "You are a helpful cybersecurity expert.",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text

    def _call_openai(self, info, prompt, system_prompt, temperature, max_tokens):
        """Call OpenAI-compatible API (OpenAI, DeepSeek, Groq, Together, Mistral, OpenRouter, HuggingFace)."""
        client = info["client"]
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        response = client.chat.completions.create(
            model=info["model_name"],
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            timeout=60.0
        )
        
        # Store usage for tracking
        if hasattr(response, 'usage') and response.usage:
            self.last_usage = {
                "prompt_tokens": getattr(response.usage, 'prompt_tokens', 0),
                "completion_tokens": getattr(response.usage, 'completion_tokens', 0),
                "total_tokens": getattr(response.usage, 'total_tokens', 0)
            }
            
        return response.choices[0].message.content

    def _call_cohere(self, info, prompt, system_prompt, temperature, max_tokens):
        """Call Cohere API."""
        client = info["client"]
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        response = client.chat(
            model=info["model_name"],
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.message.content[0].text

    # ── Utility Methods ─────────────────────────────────────────────

    def get_initialized_providers(self) -> list[str]:
        """Return list of successfully initialized providers."""
        return list(self.clients.keys())

    def test_provider(self, provider: str) -> dict:
        """Test a specific provider with a simple prompt."""
        start = time.time()
        try:
            result = self._call_provider(
                provider,
                "Say 'API test successful' in exactly those words.",
                "", 0.1, 50
            )
            elapsed = time.time() - start
            return {
                "provider": provider,
                "status": "✅ Working",
                "response_time": f"{elapsed:.2f}s",
                "response_preview": (result or "")[:100],
                "num_keys": len(self.clients[provider].get("keys", []))
            }
        except Exception as e:
            elapsed = time.time() - start
            return {
                "provider": provider,
                "status": f"❌ Failed: {e}",
                "response_time": f"{elapsed:.2f}s",
                "response_preview": "",
                "num_keys": len(self.clients[provider].get("keys", []))
            }

    def test_all_providers(self) -> list[dict]:
        """Test all initialized providers."""
        results = []
        for provider in self.clients:
            logger.info(f"Testing {provider}...")
            results.append(self.test_provider(provider))
        return results
