"""
AVAGuard Core — Provider Registry

Manages dynamic discovery, capability registration, and instantiations
for all cloud and infrastructure provider plugins. Decouples the scanning
engine from vendor-specific clients.
"""

import logging
from typing import Dict, Type, List, Optional
from avaguard_core.providers.base import CloudProvider, ProviderCapabilities
from avaguard_core.errors import ProviderError

logger = logging.getLogger(__name__)


class ProviderRegistry:
    """
    Registry for dynamic loading and discovery of provider plugins.
    Allows modular extension without core scan engine modification.
    """
    _registry: Dict[str, Type[CloudProvider]] = {}
    _active_instances: Dict[str, CloudProvider] = {}

    @classmethod
    def register_provider(cls, name: str, provider_class: Type[CloudProvider]) -> None:
        """
        Register a new provider class.

        Args:
            name: Internal identifier (e.g. 'azure', 'aws').
            provider_class: Subclass of CloudProvider.
        """
        normalized_name = name.lower().strip()
        cls._registry[normalized_name] = provider_class
        logger.info(f"Successfully registered provider plugin: '{normalized_name}'")

    @classmethod
    def get_registered_providers(cls) -> List[str]:
        """Return list of all registered provider names."""
        return list(cls._registry.keys())

    @classmethod
    def get_capabilities(cls) -> Dict[str, ProviderCapabilities]:
        """
        Dynamically discover and query capabilities of all registered providers.
        """
        capabilities = {}
        for name, provider_class in cls._registry.items():
            try:
                # Instantiate a temporary provider instance to discover capabilities
                temp_instance = provider_class()
                capabilities[name] = temp_instance.get_capabilities()
            except Exception as e:
                logger.error(f"Failed to load capabilities for provider '{name}': {e}")
        return capabilities

    @classmethod
    def get_provider_class(cls, name: str) -> Optional[Type[CloudProvider]]:
        """Retrieve class for provider name."""
        return cls._registry.get(name.lower().strip())

    @classmethod
    def get_active_instance(cls, instance_id: str) -> Optional[CloudProvider]:
        """Retrieve active instantiated provider by its ID."""
        return cls._active_instances.get(instance_id)

    @classmethod
    def register_active_instance(cls, instance_id: str, instance: CloudProvider) -> None:
        """Register an active running provider instance (e.g., authenticated session)."""
        cls._active_instances[instance_id] = instance
        logger.debug(f"Registered active provider session instance: {instance_id}")

    @classmethod
    def clear_active_instances(cls) -> None:
        """Clear all active provider instances (useful for testing session tear-down)."""
        cls._active_instances.clear()
        logger.debug("Cleared all active provider session instances.")


# Auto-register core provider plugins
from avaguard_core.providers.azure.provider import AzureProvider
ProviderRegistry.register_provider("azure", AzureProvider)

