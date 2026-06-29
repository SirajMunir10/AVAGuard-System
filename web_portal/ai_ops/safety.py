"""
AVAGuard AI Operations — Prompt Safety

Deterministic input sanitization and output validation for AI queries.
No ML classifiers — simple, auditable rules that are easy to reason about.
"""

import re
import logging
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger(__name__)

# Maximum allowed query length (characters)
MAX_QUERY_LENGTH = 2000

# Maximum allowed response length (characters)
MAX_RESPONSE_LENGTH = 4000

# Patterns that indicate prompt injection attempts.
# These are checked case-insensitively against the sanitized query.
_INJECTION_PATTERNS = [
    r'ignore\s+(all\s+)?previous\s+instructions',
    r'ignore\s+(all\s+)?prior\s+instructions',
    r'disregard\s+(all\s+)?(previous|prior|above)',
    r'forget\s+(all\s+)?(previous|prior|above)',
    r'you\s+are\s+now\s+',
    r'act\s+as\s+(a\s+)?',
    r'pretend\s+(you\s+are|to\s+be)',
    r'system\s*:\s*',
    r'<\|system\|>',
    r'<\|assistant\|>',
    r'\[\s*INST\s*\]',
    r'###\s*(system|instruction|prompt)',
    r'new\s+instructions?\s*:',
    r'override\s+(system|safety|instructions?)',
    r'jailbreak',
    r'do\s+anything\s+now',
    r'DAN\s+mode',
]

_COMPILED_PATTERNS = [re.compile(p, re.IGNORECASE) for p in _INJECTION_PATTERNS]

# Fragments that should never appear in LLM responses (leaked system prompt)
_SYSTEM_LEAK_MARKERS = [
    'You are a compliance assistant for AVAGuard',
    'Answer the user\'s question using ONLY the provided context',
    'Do not use any external knowledge',
]


@dataclass
class SanitizedQuery:
    """Result of query sanitization."""
    text: str               # Cleaned query text
    is_safe: bool           # True if query passed all checks
    flag_reason: str = ''   # Reason for flagging, if any
    original_length: int = 0


def sanitize_query(raw_query: str) -> SanitizedQuery:
    """
    Sanitize a user query before processing.

    Applies:
    - Null byte and control character stripping
    - Whitespace normalization
    - Length enforcement
    - Prompt injection pattern detection
    """
    if not raw_query or not raw_query.strip():
        return SanitizedQuery(
            text='',
            is_safe=False,
            flag_reason='Empty query',
            original_length=0
        )

    original_length = len(raw_query)

    # 1. Strip null bytes and control characters (keep newlines and tabs)
    cleaned = raw_query.replace('\x00', '')
    cleaned = re.sub(r'[\x01-\x08\x0b\x0c\x0e-\x1f\x7f]', '', cleaned)

    # 2. Normalize whitespace
    cleaned = ' '.join(cleaned.split())
    cleaned = cleaned.strip()

    # 3. Enforce max length
    if len(cleaned) > MAX_QUERY_LENGTH:
        return SanitizedQuery(
            text=cleaned[:MAX_QUERY_LENGTH],
            is_safe=False,
            flag_reason=f'Query exceeds maximum length ({original_length} > {MAX_QUERY_LENGTH})',
            original_length=original_length
        )

    # 4. Check for injection patterns
    for pattern in _COMPILED_PATTERNS:
        match = pattern.search(cleaned)
        if match:
            reason = f'Prompt injection detected: matched pattern near "{match.group()[:40]}"'
            logger.warning(f"AI safety: {reason} — query: {cleaned[:100]}...")
            return SanitizedQuery(
                text=cleaned,
                is_safe=False,
                flag_reason=reason,
                original_length=original_length
            )

    return SanitizedQuery(
        text=cleaned,
        is_safe=True,
        original_length=original_length
    )


def validate_response(response_text: str, max_length: int = MAX_RESPONSE_LENGTH) -> str:
    """
    Validate and clean an LLM response before returning to the user.

    Applies:
    - Length truncation
    - System prompt leak detection and removal
    - Null byte stripping
    """
    if not response_text:
        return ''

    # 1. Strip null bytes
    cleaned = response_text.replace('\x00', '')

    # 2. Remove leaked system prompt fragments
    for marker in _SYSTEM_LEAK_MARKERS:
        if marker in cleaned:
            logger.warning(f"AI safety: system prompt leak detected in response, removing fragment")
            cleaned = cleaned.replace(marker, '[REDACTED]')

    # 3. Truncate to max length
    if len(cleaned) > max_length:
        cleaned = cleaned[:max_length] + '\n\n[Response truncated]'

    return cleaned.strip()


# ── Phase 5A: Data Privacy Scrubber ──

import ipaddress
import copy

# Critical Data (Redacted entirely)
_CRITICAL_PATTERNS = [
    (re.compile(r'\bBearer\s+[A-Za-z0-9\-\._~+/]+=*'), '[REDACTED_BEARER_TOKEN]'),
    (re.compile(r'\bAKIA[0-9A-Z]{16}\b'), '[REDACTED_AWS_KEY]'),
    (re.compile(r'(?i)(?:postgres|mysql|mongodb(?:\+srv)?|redis|amqp|postgresql):\/\/[^"\' \n]+'), '[REDACTED_CONNECTION_STRING]'),
    (re.compile(r'(?i)(https?:\/\/)([^:\/@\s]+:[^:\/@\s]+)@'), r'\1[REDACTED_CREDENTIALS]@'),
    (re.compile(r'(?i)(?:password|secret|token|api_key|auth|passwd)[\'"]?\s*[:=]\s*[\'"]?([A-Za-z0-9\-_+/]{8,})[\'"]?'), '[REDACTED_SECRET]'),
    (re.compile(r'\b[A-Za-z0-9_.+-]+@[A-Za-z0-9-]+\.[A-Za-z0-9-.]+\b'), '[REDACTED_EMAIL]')
]

# Contextual Data regexes
_IPV4_PATTERN = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
_IPV6_PATTERN = re.compile(r'\b(?:[A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4}\b')
_UUID_PATTERN = re.compile(r'\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b')
_ARN_PATTERN = re.compile(r'\barn:aws:[a-z0-9-]+:[a-z0-9-]*:[0-9]{12}:([a-zA-Z0-9-\/]+)\b')
_HOST_PATTERN = re.compile(r'\b([a-zA-Z0-9.-]+\.(?:internal|local|lan|corp))\b')

class ContextualScrubber:
    """
    Stateful scrubber that replaces contextual data consistently across a single payload,
    while removing critical data entirely.
    """
    def __init__(self):
        self.ip_map = {}
        self.host_map = {}
        self.arn_map = {}
        self.uuid_map = {}
        
        self.counts = {
            'INTERNAL_IP': 1,
            'PUBLIC_IP': 1,
            'DB_HOST': 1,
            'API_HOST': 1,
            'WEB_HOST': 1,
            'HOST': 1,
            'AWS_ARN': 1,
            'UUID': 1
        }

    def _get_ip_replacement(self, match: re.Match) -> str:
        ip_str = match.group(0)
        if ip_str in self.ip_map:
            return self.ip_map[ip_str]
        
        try:
            ip_obj = ipaddress.ip_address(ip_str)
            if not ip_obj.is_global:
                prefix = 'INTERNAL_IP'
            else:
                prefix = 'PUBLIC_IP'
        except ValueError:
            prefix = 'PUBLIC_IP'  # fallback
            
        replacement = f"[{prefix}_{self.counts[prefix]}]"
        self.counts[prefix] += 1
        self.ip_map[ip_str] = replacement
        return replacement

    def _get_host_replacement(self, match: re.Match) -> str:
        host_str = match.group(1)
        if host_str in self.host_map:
            return self.host_map[host_str]
            
        lower_host = host_str.lower()
        if 'db' in lower_host or 'sql' in lower_host or 'mongo' in lower_host or 'postgres' in lower_host:
            prefix = 'DB_HOST'
        elif 'api' in lower_host:
            prefix = 'API_HOST'
        elif 'web' in lower_host or 'front' in lower_host:
            prefix = 'WEB_HOST'
        else:
            prefix = 'HOST'
            
        replacement = f"[{prefix}_{self.counts[prefix]}]"
        self.counts[prefix] += 1
        self.host_map[host_str] = replacement
        return replacement

    def _get_arn_replacement(self, match: re.Match) -> str:
        arn_str = match.group(0)
        if arn_str in self.arn_map:
            return self.arn_map[arn_str]
            
        replacement = f"[AWS_ARN_{self.counts['AWS_ARN']}]"
        self.counts['AWS_ARN'] += 1
        self.arn_map[arn_str] = replacement
        return replacement

    def _get_uuid_replacement(self, match: re.Match) -> str:
        uuid_str = match.group(0)
        if uuid_str in self.uuid_map:
            return self.uuid_map[uuid_str]
            
        replacement = f"[UUID_{self.counts['UUID']}]"
        self.counts['UUID'] += 1
        self.uuid_map[uuid_str] = replacement
        return replacement

    def scrub(self, text: str) -> str:
        if not isinstance(text, str):
            return str(text)
            
        scrubbed = text
        
        # 1. Strip Critical Data blindly
        for pattern, replacement in _CRITICAL_PATTERNS:
            scrubbed = pattern.sub(replacement, scrubbed)
            
        # 2. Contextual Transformations
        scrubbed = _IPV4_PATTERN.sub(self._get_ip_replacement, scrubbed)
        scrubbed = _IPV6_PATTERN.sub(self._get_ip_replacement, scrubbed)
        scrubbed = _HOST_PATTERN.sub(self._get_host_replacement, scrubbed)
        scrubbed = _ARN_PATTERN.sub(self._get_arn_replacement, scrubbed)
        scrubbed = _UUID_PATTERN.sub(self._get_uuid_replacement, scrubbed)
        
        return scrubbed

def scrub_text(text: str) -> str:
    """Convenience function for single string scrubbing (creates new state)."""
    return ContextualScrubber().scrub(text)

def _recursive_scrub(payload, scrubber: ContextualScrubber):
    if isinstance(payload, dict):
        return {k: _recursive_scrub(v, scrubber) for k, v in payload.items()}
    elif isinstance(payload, list):
        return [_recursive_scrub(item, scrubber) for item in payload]
    elif isinstance(payload, str):
        return scrubber.scrub(payload)
    else:
        return payload

def scrub_payload(payload: dict) -> dict:
    """
    Recursively scrub a JSON-serializable dictionary (e.g. ScanResult evidence)
    to mask PII and secrets, while maintaining consistent context references.
    """
    scrubber = ContextualScrubber()
    return _recursive_scrub(payload, scrubber)
