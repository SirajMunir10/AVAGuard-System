"""
AVAGuard Web Portal — Tenant Middleware

Sets `request.organization` from the authenticated user's organization
on every request. Makes tenant context available to all views without
manual User.objects.get() + user.organization lookups.

Must be placed AFTER AuthenticationMiddleware in MIDDLEWARE.
"""

import logging
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)


class TenantMiddleware(MiddlewareMixin):
    """
    Middleware that attaches the current user's organization to the request.

    After this middleware runs, views can access `request.organization`
    to get the tenant context without additional database queries.

    Sets request.organization = None for:
    - Unauthenticated requests
    - Users without an organization assignment
    - API endpoints using JWT (organization comes from token claims)
    """

    def process_request(self, request):
        request.organization = None

        if hasattr(request, 'user') and request.user.is_authenticated:
            org = getattr(request.user, 'organization', None)
            if org is not None:
                request.organization = org
            else:
                logger.debug(
                    f"Authenticated user {request.user.email} has no organization assigned."
                )
