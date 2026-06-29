"""
AVAGuard Web Portal - Cross-Cutting Security Layer (Phase 0.5)

Enterprise-grade security primitives:
- RBAC hierarchy enforcement (prevents privilege escalation)
- Sudo-mode re-authentication (server-side timestamp validation)
- Optimistic locking (prevents silent overwrites via 409 Conflict)
- Role hierarchy constants
- Compensating controls for same-level admin modification

These utilities are consumed by views and middleware. They are NOT
UI-level guards — they enforce invariants at the backend regardless
of how the request is constructed.
"""

import functools
import logging
from datetime import timedelta

from django.http import JsonResponse
from django.utils import timezone

logger = logging.getLogger(__name__)

# ======================================================================
# ROLE HIERARCHY — Numeric weight determines permission level.
# Higher weight = more privilege. Used for comparison checks.
# ======================================================================
ROLE_HIERARCHY = {
    'SUPER_ADMIN': 100,
    'IT_ADMIN': 75,
    'AUDITOR': 50,
    'VIEWER': 25,
}

# Sudo-mode validity window (seconds)
SUDO_VALIDITY_SECONDS = 300  # 5 minutes


def get_role_weight(role: str) -> int:
    """Return the numeric weight for a role string. Unknown roles get 0."""
    return ROLE_HIERARCHY.get(role, 0)


# ======================================================================
# 0.5A — RBAC HIERARCHY ENFORCEMENT
# ======================================================================

def can_modify_user(actor, target) -> bool:
    """
    Check if `actor` is allowed to modify `target`.

    Rules (per approved RBAC policy):
    1. Actor with equal or higher role weight MAY modify target.
       This intentionally allows same-level modification so admins
       can offboard peer admins who leave/are terminated.
    2. Self-modification of privilege-related fields is blocked
       separately via enforce_role_hierarchy().
    3. Compensating controls (audit logging, alerting) are applied
       when same-level modifications occur.
    """
    actor_weight = get_role_weight(actor.role)
    target_weight = get_role_weight(target.role)

    # Actor can modify target if their role weight is greater than
    # or equal to target's role weight.
    if actor_weight >= target_weight:
        return True

    return False


def is_peer_modification(actor, target) -> bool:
    """
    Check if this is a same-level admin modification.
    These require additional audit logging and alerting.
    """
    if actor.pk == target.pk:
        return False  # Self-modification is handled separately
    return get_role_weight(actor.role) == get_role_weight(target.role)


def log_admin_modification(actor, target, action_details: str, request=None):
    """
    Mandatory audit logging for all role/account modifications.
    Generates an enhanced alert for peer-admin modifications.

    This MUST be called by any view that modifies user accounts.
    """
    from core.models import AuditLog

    is_peer = is_peer_modification(actor, target)
    severity = 'PEER_ADMIN' if is_peer else 'STANDARD'

    details = (
        f"[{severity}] {actor.email} (role={actor.role}) modified "
        f"{target.email} (role={target.role}): {action_details}"
    )

    ip_address = None
    user_agent = ''
    if request:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        ip_address = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')
        user_agent = request.META.get('HTTP_USER_AGENT', '')

    AuditLog.log(
        action='USER_UPDATED',
        user=actor,
        organization=actor.organization,
        details=details,
        ip_address=ip_address,
        user_agent=user_agent,
        related_object=target,
    )

    # Enhanced alerting for peer-admin modifications
    if is_peer:
        logger.warning(
            f"ADMIN PEER MODIFICATION ALERT: {actor.email} ({actor.role}) "
            f"modified peer {target.email} ({target.role}): {action_details}"
        )


def enforce_role_hierarchy(actor, target):
    """
    Raise a structured error dict if `actor` cannot modify `target`.
    Returns None on success; returns a JsonResponse on failure.
    """
    # Block self-modification through admin controls
    if actor.pk == target.pk:
        return JsonResponse({
            'success': False,
            'errors': {'__all__': ['You cannot modify your own account through admin controls.']},
        }, status=403)

    if not can_modify_user(actor, target):
        logger.warning(
            f"Privilege escalation blocked: {actor.email} (role={actor.role}) "
            f"attempted to modify {target.email} (role={target.role})"
        )
        return JsonResponse({
            'success': False,
            'errors': {'__all__': [
                'Insufficient privileges. You cannot modify users with a higher role.'
            ]},
        }, status=403)

    return None  # Access granted


# ======================================================================
# 0.5B — SUDO-MODE ENFORCEMENT
# ======================================================================

def is_sudo_valid(request) -> bool:
    """Check if the current session has a valid sudo-mode timestamp."""
    confirmed_at = request.session.get('sudo_confirmed_at')
    if not confirmed_at:
        return False

    try:
        confirmed_time = timezone.datetime.fromisoformat(confirmed_at)
        if timezone.is_naive(confirmed_time):
            confirmed_time = timezone.make_aware(confirmed_time)
        elapsed = timezone.now() - confirmed_time
        return elapsed.total_seconds() <= SUDO_VALIDITY_SECONDS
    except (ValueError, TypeError):
        return False


def set_sudo_timestamp(request):
    """Mark the current session as sudo-confirmed right now."""
    request.session['sudo_confirmed_at'] = timezone.now().isoformat()


def clear_sudo_timestamp(request):
    """Invalidate sudo-mode for the current session."""
    request.session.pop('sudo_confirmed_at', None)


def sudo_required(view_func):
    """
    Decorator: requires sudo-mode (re-authentication within 5 minutes)
    before allowing the view to execute.

    Returns 403 JSON with 'sudo_required': True so the frontend
    can prompt for re-authentication.
    """
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not is_sudo_valid(request):
            return JsonResponse({
                'success': False,
                'sudo_required': True,
                'errors': {'__all__': [
                    'This action requires re-authentication. '
                    'Please confirm your password to continue.'
                ]},
            }, status=403)
        return view_func(request, *args, **kwargs)
    return wrapper


# ======================================================================
# 0.5C — OPTIMISTIC LOCKING
# ======================================================================

def check_optimistic_lock(instance, submitted_timestamp_str: str):
    """
    Compare the instance's `updated_at` against the submitted timestamp.

    Args:
        instance: Django model instance with `updated_at` field.
        submitted_timestamp_str: ISO format string of the expected `updated_at`.

    Returns:
        None on success; JsonResponse(409) on conflict.
    """
    if not submitted_timestamp_str:
        # If no timestamp submitted, skip check (backwards compatibility)
        return None

    try:
        submitted_ts = timezone.datetime.fromisoformat(submitted_timestamp_str)
        if timezone.is_naive(submitted_ts):
            submitted_ts = timezone.make_aware(submitted_ts)
    except (ValueError, TypeError):
        return JsonResponse({
            'success': False,
            'errors': {'__all__': ['Invalid timestamp format for concurrency check.']},
        }, status=400)

    # Compare with microsecond tolerance
    db_ts = instance.updated_at
    if abs((db_ts - submitted_ts).total_seconds()) > 1.0:
        return JsonResponse({
            'success': False,
            'conflict': True,
            'errors': {'__all__': [
                'This record was modified by another user. '
                'Please refresh and try again.'
            ]},
            'server_updated_at': db_ts.isoformat(),
        }, status=409)

    return None  # No conflict


# ======================================================================
# 0.5D — ROLE VALIDATION FOR ASSIGNMENT
# ======================================================================

def validate_role_assignment(actor, new_role: str):
    """
    Ensure `actor` cannot assign a role higher than their own.

    Same-level assignment IS allowed (e.g., IT_ADMIN can create another
    IT_ADMIN). This matches the approved RBAC policy where same-level
    peer modification is intentional.

    Self-escalation is blocked by enforce_role_hierarchy() which prevents
    self-modification through admin controls.

    Returns None on success; JsonResponse(403) on violation.
    """
    actor_weight = get_role_weight(actor.role)
    new_weight = get_role_weight(new_role)

    if new_weight > actor_weight:
        return JsonResponse({
            'success': False,
            'errors': {'role': [
                f'You cannot assign the "{new_role}" role. '
                f'You can only assign roles at or below your own level.'
            ]},
        }, status=403)

    return None


def prevent_self_escalation(actor, target, new_role: str):
    """
    Explicitly block self-role-escalation.

    Even though enforce_role_hierarchy blocks self-modification through
    admin controls, this provides a defense-in-depth check specifically
    for role changes.

    Returns None on success; JsonResponse(403) on violation.
    """
    if actor.pk == target.pk:
        current_weight = get_role_weight(actor.role)
        new_weight = get_role_weight(new_role)
        if new_weight > current_weight:
            logger.warning(
                f"Self-escalation attempt blocked: {actor.email} tried to "
                f"change own role from {actor.role} to {new_role}"
            )
            return JsonResponse({
                'success': False,
                'errors': {'role': [
                    'You cannot escalate your own role. '
                    'Contact a higher-level administrator.'
                ]},
            }, status=403)

    return None
