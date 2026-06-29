"""
AVAGuard Core — Evidence Classification and Hardening

Provides utility functions to categorize, normalize, and redact evidence
retrieved by cloud provider queries into raw, normalized, audit-safe,
and AI-safe datasets.
"""

import re
import copy
import logging
from typing import Dict, List, Any

logger = logging.getLogger(__name__)

# SENSITIVE KEY PATTERNS to scrub for AI safety (case-insensitive)
SENSITIVE_KEYS = {
    "tenantid", "tenant_id", "subscriptionid", "subscription_id",
    "clientid", "client_id", "clientsecret", "client_secret",
    "secret", "token", "password", "key", "passwordprofile",
    "mfatoken", "ipaddress", "ip", "telephonenumber", "mobilephone",
    "secret_value", "connection_string", "credentials", "access_token"
}

# Regex to detect emails, IPv4, IPv6, and UUIDs/GUIDs
EMAIL_REGEX = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
IPV4_REGEX = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b")
UUID_REGEX = re.compile(r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b")


def classify_evidence(resources: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Classify queried resource records into raw, normalized, audit-safe,
    and AI-safe evidence structures.
    
    Args:
        resources: Raw list of resource dictionary items.
        
    Returns:
        Dictionary mapping classification tiers to lists/dicts.
    """
    raw = copy.deepcopy(resources)
    
    # 1. Normalized: Uniform dictionary format, normalized dates, flattened structures where useful
    normalized = _normalize_resources(raw)
    
    # 2. Audit-Safe: Retains structural and compliance configurations but strips transient session tokens
    audit_safe = _generate_audit_safe(normalized)
    
    # 3. AI-Safe: 100% redacted. Strips secrets, client/tenant IDs, PII (names, emails, IPs, UUIDs)
    ai_safe = _generate_ai_safe(audit_safe)
    
    return {
        "raw": raw,
        "normalized": normalized,
        "audit_safe": audit_safe,
        "ai_safe": ai_safe
    }


def _normalize_resources(resources: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Normalize raw dictionary keys and standardize timestamp formats."""
    normalized_list = []
    for res in resources:
        norm = {}
        for k, v in res.items():
            # Standardize date field representations
            if isinstance(v, str) and ("datetime" in k.lower() or "date" in k.lower()):
                # Clean up Z or milliseconds spacing for uniformity
                v_clean = v.replace("Z", "").split(".")[0]
                norm[k] = v_clean
            else:
                norm[k] = v
        normalized_list.append(norm)
    return normalized_list


def _generate_audit_safe(normalized: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Remove volatile/temporary runtime attributes (session tokens, correlation IDs)."""
    audit_list = []
    for res in normalized:
        aud = copy.deepcopy(res)
        
        # Strip transient credentials/session tokens
        aud.pop("temp_session", None)
        aud.pop("session_token", None)
        aud.pop("correlation_id", None)
        aud.pop("_transient", None)
        
        audit_list.append(aud)
    return audit_list


def _generate_ai_safe(audit_safe: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Produce fully sanitized, PII-scrubbed evidence safe for AI/RAG services."""
    ai_list = []
    for res in audit_safe:
        safe = copy.deepcopy(res)
        
        # Step 1: Filter key-value pairs matching sensitive fields
        safe = _scrub_sensitive_keys(safe)
        
        # Step 2: Deep string redaction for PII, emails, IPs, and UUIDs
        safe = _redact_pii_strings(safe)
        
        ai_list.append(safe)
    return ai_list


def _scrub_sensitive_keys(data: Any) -> Any:
    """Recursively scrub any dictionary keys matching known secrets or IDs."""
    if isinstance(data, dict):
        scrubbed = {}
        for k, v in data.items():
            k_lower = k.lower()
            if any(sensitive in k_lower for sensitive in SENSITIVE_KEYS):
                scrubbed[k] = "[REDACTED_SENSITIVE_FIELD]"
            else:
                scrubbed[k] = _scrub_sensitive_keys(v)
        return scrubbed
    elif isinstance(data, list):
        return [_scrub_sensitive_keys(item) for item in data]
    return data


def _redact_pii_strings(data: Any) -> Any:
    """Recursively scan string fields to redact PII (emails, IPs, UUIDs, explicit names)."""
    if isinstance(data, dict):
        redacted = {}
        for k, v in data.items():
            # Specific high-risk PII fields
            k_lower = k.lower()
            if k_lower in ("displayname", "givenname", "surname", "mail", "userprincipalname"):
                redacted[k] = f"[REDACTED_{k.upper()}]"
            else:
                redacted[k] = _redact_pii_strings(v)
        return redacted
    elif isinstance(data, list):
        return [_redact_pii_strings(item) for item in data]
    elif isinstance(data, str):
        # Apply regex sanitizers
        s = EMAIL_REGEX.sub("[REDACTED_EMAIL]", data)
        s = IPV4_REGEX.sub("[REDACTED_IP]", s)
        s = UUID_REGEX.sub("[REDACTED_UUID]", s)
        return s
    return data
