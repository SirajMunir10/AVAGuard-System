"""
AVAGuard Core — Providers Package
"""

from avaguard_core.providers.base import CloudProvider, ProviderCapabilities, QueryResponse
from avaguard_core.providers.registry import ProviderRegistry
from avaguard_core.providers.azure.provider import AzureProvider

__all__ = [
    'CloudProvider',
    'ProviderCapabilities',
    'QueryResponse',
    'ProviderRegistry',
    'AzureProvider'
]
