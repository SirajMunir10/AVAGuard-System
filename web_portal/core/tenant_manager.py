"""
AVAGuard Web Portal — Tenant-Aware Model Manager

Provides automatic organization-scoping for all multi-tenant models.
Prevents cross-tenant data leaks by ensuring every query includes
an organization filter at the database layer, not just the view layer.

Usage:
    class MyModel(models.Model):
        organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
        # ... other fields ...

        objects = TenantAwareManager()

    # In views (after TenantMiddleware sets request.organization):
    results = MyModel.objects.for_tenant(request.organization).all()

    # Or use the unscoped manager for admin/system operations:
    all_results = MyModel.objects.unscoped().all()
"""

import logging
from django.db import models

logger = logging.getLogger(__name__)


class TenantAwareQuerySet(models.QuerySet):
    """
    QuerySet that can be scoped to an organization.

    Provides .for_tenant(org) to scope and .unscoped() to bypass.
    """

    def for_tenant(self, organization):
        """
        Filter results to a specific organization.

        Args:
            organization: Organization instance or UUID.

        Returns:
            Filtered queryset scoped to the organization.
        """
        if organization is None:
            logger.warning(
                "TenantAwareQuerySet.for_tenant() called with None organization. "
                "Returning empty queryset for safety."
            )
            return self.none()
        
        # Check if the model has a direct organization field
        has_org_field = any(f.name == 'organization' for f in self.model._meta.get_fields())
        if has_org_field:
            return self.filter(organization=organization)
        
        # If the model is ScanResult, filter via the scan relationship
        if self.model.__name__ == 'ScanResult':
            return self.filter(scan__organization=organization)
            
        logger.warning(
            f"Model {self.model.__name__} does not have an organization field. "
            "Unable to apply default tenant filtering."
        )
        return self.none()

    def unscoped(self):
        """
        Return the queryset without tenant scoping.
        Use ONLY for system-level operations (migrations, admin, analytics).
        """
        return self.all()


class TenantAwareManager(models.Manager):
    """
    Manager that provides tenant-scoped and unscoped access patterns.

    Does NOT automatically filter (that would break Django admin and
    management commands). Instead, provides explicit .for_tenant()
    and .unscoped() methods to make the developer's intent clear.

    Views should ALWAYS use .for_tenant(request.organization).
    System code may use .unscoped() with justification.
    """

    def get_queryset(self):
        return TenantAwareQuerySet(self.model, using=self._db)

    def for_tenant(self, organization):
        """Scope all queries to the given organization."""
        return self.get_queryset().for_tenant(organization)

    def unscoped(self):
        """Bypass tenant scoping (system operations only)."""
        return self.get_queryset().unscoped()


def get_tenant_from_request(request):
    """
    Extract the organization from an authenticated request.

    Returns:
        Organization instance or None if not authenticated/no org.
    """
    if not hasattr(request, 'user') or not request.user.is_authenticated:
        return None

    # Try cached value first (set by TenantMiddleware)
    if hasattr(request, 'organization'):
        return request.organization

    # Fall back to user's organization
    org = getattr(request.user, 'organization', None)
    return org
