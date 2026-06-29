"""
AVAGuard Core — Azure Cloud Provider

Implements the CloudProvider interface for Microsoft Azure, supporting
both live Microsoft Graph API requests (via a lightweight custom HTTP wrapper)
and mock operations (via MockGraphAPIClient adapter).
"""

import time
import logging
from typing import Dict, List, Any, Optional
from datetime import datetime

from avaguard_core.providers.base import CloudProvider, ProviderCapabilities, QueryResponse
from avaguard_core.providers.evidence import classify_evidence
from avaguard_core.errors import ProviderAuthError, EvidenceCollectionError, RateLimitError
from avaguard_core.graph_api_client import GraphAPIClient
from avaguard_core.mock_graph_client import MockGraphAPIClient

logger = logging.getLogger(__name__)


class AzureProvider(CloudProvider):
    """
    Microsoft Azure Cloud Provider scanning plugin.
    Coordinates MSAL authentication, dynamic OData $select scale optimizations,
    pagination traversal, exponential retry backoff, and mock dataset loading.
    """

    def __init__(self, provider_id: Optional[str] = None):
        super().__init__(provider_id or "azure")
        self.use_mock = False
        self.client: Optional[Any] = None
        self.tenant_id: str = ""
        self._capabilities = self._build_capabilities()

    def _build_capabilities(self) -> ProviderCapabilities:
        """Construct the static capability schema for the Azure Provider."""
        return ProviderCapabilities(
            name="azure",
            display_name="Microsoft Azure AD & CIS Ingestion Provider",
            supported_services=[
                "users",
                "domains",
                "groups",
                "directoryRoles",
                "servicePrincipals",
                "conditionalAccessPolicies",
                "securityDefaults",
                "signInRiskPolicy",
                "authenticationMethodsPolicy",
                "authorizationPolicy"
            ],
            supported_remediations=["azure_cli", "powershell", "terraform"],
            authentication_modes=["client_secret", "device_code", "mock"],
            supported_benchmarks=["cis_azure_foundations_v4.0.0"]
        )

    def get_capabilities(self) -> ProviderCapabilities:
        """Return the dynamically discovered capabilities of this provider."""
        return self._capabilities

    def initialize(self, credentials: Dict[str, Any]) -> None:
        """
        Authenticate client sessions and establish active API connections.

        Args:
            credentials: Secure connection parameters.
        """
        self.use_mock = credentials.get("use_mock", False)
        self.tenant_id = credentials.get("tenant_id", "mock-tenant-id")

        if self.use_mock:
            mock_file = credentials.get("mock_data_file", "datasets/failure_0.json")
            logger.info(f"Initializing Azure Provider in MOCK mode using dataset: {mock_file}")
            try:
                self.client = MockGraphAPIClient(mock_file)
            except Exception as e:
                raise ProviderAuthError(f"Failed to initialize mock client: {e}")
        else:
            tenant_id = credentials.get("tenant_id")
            client_id = credentials.get("client_id")
            client_secret = credentials.get("client_secret")
            use_device_code = credentials.get("use_device_code", False)

            if not tenant_id or not client_id:
                raise ProviderAuthError("Missing required tenant_id or client_id credentials.")

            logger.info(f"Initializing Azure Provider in LIVE mode for Tenant: {tenant_id}")
            try:
                self.client = GraphAPIClient(
                    tenant_id=tenant_id,
                    client_id=client_id,
                    client_secret=client_secret,
                    use_device_code=use_device_code
                )
                # Force token acquisition to validate credentials early
                self.client._get_access_token()
            except Exception as e:
                raise ProviderAuthError(f"Azure authentication handshake failed: {e}")

    def query_resources(self, resource_type: str, fields: List[str] = None) -> QueryResponse:
        """
        Query Microsoft Graph API and return a structured snapshot of resources.

        Args:
            resource_type: Target category/endpoint.
            fields: Specific parameters to retrieve.
        """
        if not self.client:
            raise EvidenceCollectionError("Provider is not initialized. Call initialize() first.")

        start_time = datetime.now()
        api_calls = 0

        # Normalization and routing
        endpoint = self._map_resource_to_endpoint(resource_type)

        try:
            if self.use_mock:
                # Mock route
                raw_data = self.client.get(endpoint)
                if isinstance(raw_data, dict) and "value" in raw_data:
                    resources = raw_data["value"]
                elif isinstance(raw_data, list):
                    resources = raw_data
                else:
                    resources = [raw_data] if raw_data else []
                api_calls = 1
            else:
                # Live route - custom HTTP calls with throttling, pagination, select projection
                resources, api_calls = self._execute_live_query(endpoint, fields)

        except Exception as e:
            logger.error(f"Azure Provider query failed for '{resource_type}': {e}")
            raise EvidenceCollectionError(f"Failed to collect evidence from Azure API: {e}")

        # Apply Dynamic Evidence Classification & Scrubbing
        evidence = classify_evidence(resources)

        return QueryResponse(
            provider_name="azure",
            resource_type=resource_type,
            resources=evidence["normalized"],
            query_timestamp=start_time,
            api_calls_count=api_calls,
            evidence_snapshot=evidence
        )

    def _map_resource_to_endpoint(self, resource_type: str) -> str:
        """Map simple resource classifications to Microsoft Graph endpoints."""
        mapping = {
            "users": "users",
            "domains": "domains",
            "groups": "groups",
            "directoryroles": "directoryRoles",
            "serviceprincipals": "servicePrincipals",
            "conditionalaccesspolicies": "policies/conditionalAccessPolicies",
            "securitydefaults": "policies/identitySecurityDefaultsEnforcementPolicy",
            "signinriskpolicy": "identityProtection/riskPolicies/signInRiskPolicy",
            "authenticationmethodspolicy": "policies/authenticationMethodsPolicy",
            "authorizationpolicy": "policies/authorizationPolicy"
        }
        normalized = resource_type.lower().strip().replace("_", "")
        return mapping.get(normalized, resource_type)

    def _execute_live_query(self, endpoint: str, fields: List[str] = None) -> tuple[List[Dict[str, Any]], int]:
        """Execute a paginated, throttling-aware live Graph query with OData select."""
        params = {}
        if fields:
            # Scale Optimization: Projet only required fields
            params["$select"] = ",".join(fields)

        all_items = []
        api_calls = 0

        # Execute first page query with retry backoff
        api_calls += 1
        result = self._execute_with_retry(self.client.get, endpoint, params=params)

        if isinstance(result, dict) and "value" in result:
            all_items.extend(result["value"])
        elif isinstance(result, list):
            all_items.extend(result)
        else:
            all_items.append(result)

        # Traverse pagination nextLink
        while isinstance(result, dict) and "@odata.nextLink" in result:
            next_url = result["@odata.nextLink"]
            logger.info(f"Traversing next page of results via pagination link: {next_url}")
            api_calls += 1
            response = self._execute_with_retry(self.client._execute_request, "GET", next_url)
            result = response.json()
            if isinstance(result, dict) and "value" in result:
                all_items.extend(result["value"])

        return all_items, api_calls

    def _execute_with_retry(self, func, *args, **kwargs) -> Any:
        """Execute client operations with exponential backoff for rate limiting."""
        max_retries = 3
        backoff_base = 2.0

        for attempt in range(max_retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                # Check for rate limiting / throttling responses
                err_str = str(e).lower()
                status_code = getattr(e, "status_code", None)

                # Check if it looks like a 429 rate limit
                if status_code == 429 or "too many requests" in err_str or "throttled" in err_str:
                    delay = backoff_base ** attempt
                    logger.warning(f"Rate limited during API query. Backing off for {delay}s. Attempt {attempt+1}/{max_retries}")
                    time.sleep(delay)
                    continue

                # Any other transient errors
                if attempt < max_retries - 1:
                    delay = backoff_base ** attempt
                    logger.warning(f"Transient query error: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
                    continue

                # Max retries exceeded
                raise e

        raise RateLimitError("Max API retry thresholds exceeded due to consistent provider throttling.")

    def is_healthy(self) -> bool:
        """Lightweight health check against active provider state."""
        if not self.client:
            return False

        if self.use_mock:
            return True

        try:
            # Query a minimal default profile endpoint (e.g. organization or domains)
            self.client.get_organization()
            return True
        except Exception as e:
            logger.error(f"Azure Provider health check failed: {e}")
            return False
