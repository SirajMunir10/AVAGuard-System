"""
AVAGuard Core — Structured Error Taxonomy

Defines standardized, enterprise-ready exceptions for error reporting,
debugging, and audit trails. Allows downstream systems to handle failures
deterministically and compile precise compliance/technical logs.
"""

class AVAGuardError(Exception):
    """Base exception class for all AVAGuard-related errors."""
    def __init__(self, message: str, details: dict = None):
        super().__init__(message)
        self.message = message
        self.details = details or {}

    def to_dict(self) -> dict:
        return {
            "error_type": self.__class__.__name__,
            "message": self.message,
            "details": self.details
        }


# ==============================================================================
# Provider Exceptions
# ==============================================================================

class ProviderError(AVAGuardError):
    """Base exception for all cloud or infrastructure provider failures."""
    pass


class ProviderAuthError(ProviderError):
    """Raised when authentication with the provider's API fails."""
    pass


class RateLimitError(ProviderError):
    """Raised when the provider's API triggers a rate limit or throttling response."""
    def __init__(self, message: str, retry_after: int = 60, details: dict = None):
        details = details or {}
        details["retry_after_seconds"] = retry_after
        super().__init__(message, details)
        self.retry_after = retry_after


class EvidenceCollectionError(ProviderError):
    """Raised when querying, parsing, or snapshotted API retrieval fails."""
    pass


# ==============================================================================
# Benchmark & Validation Exceptions
# ==============================================================================

class BenchmarkError(AVAGuardError):
    """Base exception for all benchmark-related operations."""
    pass


class BenchmarkValidationError(BenchmarkError):
    """Raised when benchmark JSON definitions violate the versioned schema."""
    pass


# ==============================================================================
# Remediation & Rendering Exceptions
# ==============================================================================

class RemediationError(AVAGuardError):
    """Base exception for all remediation engine operations."""
    pass


class RemediationRenderError(RemediationError):
    """Raised when Jinja2 rendering fails or lacks required non-compliant resource details."""
    pass


# ==============================================================================
# Security & Tenant Exceptions
# ==============================================================================

class TenantIsolationError(AVAGuardError):
    """Raised when cross-tenant leaks are detected or invalid routing occurs."""
    pass
