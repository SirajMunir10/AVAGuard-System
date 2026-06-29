"""
AVAGuard Core — Provider Base Interface

Defines Pydantic schemas for provider capabilities and query responses,
and the Abstract base class `CloudProvider` that all multi-cloud or OS
scanning plugins must implement.
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
from datetime import datetime


class ProviderCapabilities(BaseModel):
    """
    Schema for dynamically discovering provider features and compatibilities.
    Enables dynamic UI configuration and SaaS routing.
    """
    name: str = Field(description="Internal identifier of the provider (e.g., 'azure', 'aws')")
    display_name: str = Field(description="Human-readable title")
    supported_services: List[str] = Field(default_factory=list, description="APIs or services scanned")
    supported_remediations: List[str] = Field(default_factory=list, description="Remediation types generated")
    authentication_modes: List[str] = Field(default_factory=list, description="Available auth flows")
    supported_benchmarks: List[str] = Field(default_factory=list, description="Benchmarks supported")


class QueryResponse(BaseModel):
    """
    Structured snapshot returned by provider queries.
    Preserves audit evidence, timestamps, and performance counters.
    """
    provider_name: str
    resource_type: str
    resources: List[Dict[str, Any]] = Field(default_factory=list)
    query_timestamp: datetime = Field(default_factory=datetime.now)
    api_calls_count: int = 1
    evidence_snapshot: Dict[str, Any] = Field(default_factory=dict, description="Raw audit evidence")


class CloudProvider(ABC):
    """
    Abstract Base Class for all AVAGuard cloud, OS, and infrastructure providers.
    All plugins (Azure, AWS, GCP, K8s, Linux) must implement this.
    """

    def __init__(self, provider_id: Optional[str] = None):
        self.provider_id = provider_id or self.__class__.__name__.lower()
        self._capabilities: Optional[ProviderCapabilities] = None

    @abstractmethod
    def get_capabilities(self) -> ProviderCapabilities:
        """
        Return the dynamically discovered capabilities of this provider.
        """
        pass

    @abstractmethod
    def initialize(self, credentials: Dict[str, Any]) -> None:
        """
        Authenticate client sessions and establish active API connections.

        Args:
            credentials: Secure connection parameter dictionary.

        Raises:
            ProviderAuthError: If connection or authorization fails.
        """
        pass

    @abstractmethod
    def query_resources(self, resource_type: str, fields: List[str] = None) -> QueryResponse:
        """
        Query provider APIs and return a structured snapshot of resources.

        Args:
            resource_type: Target category/endpoint (e.g. 'users', 's3_buckets').
            fields: Specific parameters to retrieve (optional).

        Returns:
            QueryResponse schema containing resource records and audit context.

        Raises:
            EvidenceCollectionError: If query execution or snapshotted parsing fails.
            RateLimitError: If provider API triggers throttling responses.
        """
        pass

    @abstractmethod
    def is_healthy(self) -> bool:
        """
        Run a lightweight connectivity check to confirm client is active.
        """
        pass
