"""
AVAGuard Security AI - Token Usage Tracker
Tracks API usage per provider with JSON persistence, multi-account rotation, and alerts.
"""

import os
import json
import time
import logging
from pathlib import Path
from datetime import datetime, timezone
from typing import Optional

from synthetic_data_generator.config import API_PROVIDERS, TOKEN_STATE_FILE, get_api_key, get_api_keys

logger = logging.getLogger("avaguard.token_manager")


class TokenTracker:
    """
    Tracks token usage across all API providers.
    Persists state to JSON file so progress survives restarts.
    
    Usage:
        tracker = TokenTracker()
        provider = tracker.get_best_provider()
        tracker.track(provider, tokens_used=500)
        tracker.print_status()
    """

    def __init__(self, state_file: Optional[Path] = None):
        self.state_file = state_file or TOKEN_STATE_FILE
        self.state_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Load limits from config
        self.limits = {}
        for provider, cfg in API_PROVIDERS.items():
            self.limits[provider] = cfg.get("free_tier_limit", 0)

        self.usage = self._load_state()
        self.session_start = datetime.now(timezone.utc).isoformat()

        # Track providers that fail with permanent errors (e.g., 402, credit exhausted)
        self._disabled_providers: set = set()

    def _load_state(self) -> dict:
        """Load previous usage state or initialize fresh."""
        if self.state_file.exists():
            try:
                with open(self.state_file, "r") as f:
                    data = json.load(f)
                logger.info(f"📂 Loaded token usage from {self.state_file}")
                return data
            except (json.JSONDecodeError, IOError):
                logger.warning("⚠️  Could not load token state, starting fresh")
        
        return self._fresh_state()

    def _fresh_state(self) -> dict:
        """Create fresh usage tracking state."""
        return {
            "providers": {p: {"tokens_used": 0, "calls": 0, "errors": 0, "last_used": None}
                          for p in API_PROVIDERS},
            "daily_usage": {},
            "session_stats": {
                "started_at": datetime.now(timezone.utc).isoformat(),
                "total_tokens": 0,
                "total_calls": 0,
                "total_qa_generated": 0
            }
        }

    def _save_state(self):
        """Persist usage to disk."""
        try:
            with open(self.state_file, "w") as f:
                json.dump(self.usage, f, indent=2, default=str)
        except IOError as e:
            logger.error(f"Could not save token state: {e}")

    def track(self, provider: str, tokens: int, is_error: bool = False):
        """
        Record token usage for a provider.
        
        Args:
            provider: Provider name (e.g., 'gemini')
            tokens: Number of tokens used (approximate)
            is_error: Whether this call resulted in an error
        """
        if provider not in self.usage["providers"]:
            self.usage["providers"][provider] = {
                "tokens_used": 0, "calls": 0, "errors": 0, "last_used": None
            }

        p = self.usage["providers"][provider]
        p["tokens_used"] += int(tokens)
        p["calls"] += 1
        if is_error:
            p["errors"] += 1
        p["last_used"] = datetime.now(timezone.utc).isoformat()

        # Update session totals
        self.usage["session_stats"]["total_tokens"] += int(tokens)
        self.usage["session_stats"]["total_calls"] += 1

        # Track daily usage
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        if today not in self.usage["daily_usage"]:
            self.usage["daily_usage"][today] = {}
        if provider not in self.usage["daily_usage"][today]:
            self.usage["daily_usage"][today][provider] = 0
        self.usage["daily_usage"][today][provider] += int(tokens)

        self._save_state()

        # Check limits
        self._check_limits(provider)

    def increment_qa_count(self, count: int = 1):
        """Increment the total Q&A pairs generated counter."""
        self.usage["session_stats"]["total_qa_generated"] += count
        self._save_state()

    def _check_limits(self, provider: str):
        """Warn if approaching usage limits."""
        limit = self.limits.get(provider, float('inf'))
        if limit == float('inf'):
            return

        used = self.usage["providers"][provider]["tokens_used"]
        pct = (used / limit) * 100

        if pct >= 95:
            logger.critical(
                f"🔴 CRITICAL: {provider.upper()} at {pct:.1f}% — "
                f"{used:,}/{limit:,} tokens. SWITCH PROVIDER!"
            )
        elif pct >= 80:
            logger.warning(
                f"🟡 WARNING: {provider.upper()} at {pct:.1f}% — "
                f"{used:,}/{limit:,} tokens"
            )

    def get_best_provider(self) -> Optional[str]:
        """
        Round-robin provider selection: picks the provider that was used
        least recently. This distributes load across Gemini, Groq, Mistral, etc.
        
        Returns the provider name, or None if all are exhausted.
        """
        available = []
        for provider, limit in self.limits.items():
            # Skip disabled (permanently failed) providers
            if provider in self._disabled_providers:
                continue
            # Must have an API key (multi-key aware)
            if not get_api_keys(provider):
                continue

            used = self.usage["providers"].get(provider, {}).get("tokens_used", 0)

            if limit == float('inf') or limit >= 10_000_000:
                available.append(provider)
            else:
                remaining = max(0, limit - used)
                if remaining > 0:
                    available.append(provider)

        if not available:
            logger.error("❌ All providers exhausted! Add more API keys.")
            return None

        # Round-robin: sort by last_used timestamp (None/oldest first)
        def last_used_key(p):
            ts = self.usage["providers"].get(p, {}).get("last_used")
            return ts or "0"
        
        return sorted(available, key=last_used_key)[0]

    def get_verification_provider(self, exclude: str) -> Optional[str]:
        """
        Get a DIFFERENT provider for cross-verification.
        Used to verify answers generated by another provider.
        
        Args:
            exclude: Provider that generated the answer (don't use same one)
            
        Returns:
            Provider name different from exclude, or None
        """
        available = []
        for provider, limit in self.limits.items():
            if provider == exclude:
                continue
            if provider in self._disabled_providers:
                continue
            if not get_api_keys(provider):
                continue

            used = self.usage["providers"].get(provider, {}).get("tokens_used", 0)
            if limit == float('inf') or limit >= 10_000_000:
                available.append(provider)
            else:
                remaining = max(0, limit - used)
                if remaining > 0:
                    available.append(provider)

        if not available:
            logger.debug("No alternative provider for verification, skipping")
            return None

        # Pick least recently used that isn't the excluded one
        def last_used_key(p):
            ts = self.usage["providers"].get(p, {}).get("last_used")
            return ts or "0"
        
        return sorted(available, key=last_used_key)[0]

    def disable_provider(self, provider: str, reason: str = ""):
        """Disable a provider for this session (e.g., credits exhausted)."""
        self._disabled_providers.add(provider)
        logger.warning(f"🚫 Disabled {provider.upper()} for this session: {reason}")

    def get_disabled_providers(self) -> set:
        """Get the set of disabled providers."""
        return self._disabled_providers.copy()

    def get_status(self) -> dict:
        """Get complete usage status for all providers."""
        status = {}
        for provider, limit in self.limits.items():
            used = self.usage["providers"].get(provider, {}).get("tokens_used", 0)
            calls = self.usage["providers"].get(provider, {}).get("calls", 0)
            errors = self.usage["providers"].get(provider, {}).get("errors", 0)
            has_key = bool(get_api_key(provider))

            if limit == float('inf') or limit >= 10_000_000:
                remaining = "unlimited"
                pct = 0
            else:
                remaining = max(0, limit - used)
                pct = (used / limit) * 100 if limit > 0 else 0

            status[provider] = {
                "tokens_used": used,
                "tokens_limit": limit,
                "tokens_remaining": remaining,
                "percentage_used": round(pct, 1),
                "api_calls": calls,
                "errors": errors,
                "has_key": has_key,
                "status_icon": self._status_icon(pct, has_key)
            }

        return status

    def _status_icon(self, pct: float, has_key: bool) -> str:
        if not has_key:
            return "⚪ No Key"
        if pct >= 90:
            return "🔴 Critical"
        elif pct >= 75:
            return "🟡 Warning"
        elif pct > 0:
            return "🟢 Active"
        else:
            return "🟢 Full"

    def get_session_stats(self) -> dict:
        """Get current session statistics."""
        return self.usage["session_stats"]

    def print_status(self):
        """Print formatted usage status to console."""
        print("\n" + "=" * 72)
        print(" AVAGuard API Usage Status")
        print("=" * 72)

        status = self.get_status()
        for provider, info in sorted(status.items(), key=lambda x: API_PROVIDERS.get(x[0], {}).get("priority", 99)):
            icon = info["status_icon"]
            used = info["tokens_used"]
            limit = info["tokens_limit"]
            remaining = info["tokens_remaining"]

            print(f"\n  {icon} {provider.upper()}")
            print(f"     Model: {API_PROVIDERS.get(provider, {}).get('model', 'N/A')}")
            print(f"     Used: {used:,} tokens | Calls: {info['api_calls']} | Errors: {info['errors']}")
            if isinstance(remaining, str):
                print(f"     Remaining: {remaining}")
            else:
                print(f"     Remaining: {remaining:,} / {limit:,} ({info['percentage_used']}%)")

        stats = self.get_session_stats()
        print(f"\n{'─' * 72}")
        print(f"  Session: {stats['total_calls']} calls | {stats['total_tokens']:,} tokens | {stats['total_qa_generated']} Q&A pairs")
        print("=" * 72 + "\n")

    def reset_usage(self, provider: Optional[str] = None):
        """Reset usage counters (for new billing period)."""
        if provider:
            if provider in self.usage["providers"]:
                self.usage["providers"][provider] = {
                    "tokens_used": 0, "calls": 0, "errors": 0, "last_used": None
                }
        else:
            self.usage = self._fresh_state()
        self._save_state()
        logger.info(f"🔄 Reset usage for {'all providers' if not provider else provider}")

    def export_for_dashboard(self) -> dict:
        """Export data formatted for the Gradio dashboard."""
        status = self.get_status()
        session = self.get_session_stats()

        # Build chart data
        providers_data = []
        for name, info in status.items():
            providers_data.append({
                "Provider": name.upper(),
                "Used (%)": info["percentage_used"],
                "Tokens Used": info["tokens_used"],
                "Status": info["status_icon"],
                "API Calls": info["api_calls"]
            })

        return {
            "providers": providers_data,
            "session": session,
            "daily": self.usage.get("daily_usage", {})
        }
