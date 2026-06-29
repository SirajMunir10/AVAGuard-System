# avaguard-core/avaguard_core/checks/__init__.py
"""
AVAGuard Compliance Checks Registry - Updated to use dictionary format.
"""

from .base_check import BaseCheck, CheckResult, CheckStatus, CISSeverity

# Import using your actual class names
from .check_1_1_mfa import Check_1_1_MFA
from .check_1_3_security_defaults import Check_1_3_SecurityDefaults
from .check_1_5_guest_roles import Check_1_5_GuestRoles
from .check_1_8_sspr import Check_1_8_SSPR
from .check_1_11_legacy_auth import Check_1_11_LegacyAuth
from .check_1_23_custom_roles import Check_1_23_CustomRoles
from .check_2_1_domains import Check_2_1_Domains
from .check_3_1_signin_risk import Check_3_1_SigninRisk
from .check_inactive_users import Check_InactiveUsers
from .check_password_age import Check_PasswordAge

from typing import Dict, Type, Optional, List
from avaguard_core.checks.protocol import CheckProtocol

# Create dictionary mapping (check_id -> class)
AVAILABLE_CHECKS: Dict[str, Type[CheckProtocol]] = {
    "1.1": Check_1_1_MFA,
    "1.3": Check_1_3_SecurityDefaults,
    "1.5": Check_1_5_GuestRoles,
    "1.8": Check_1_8_SSPR,
    "1.11": Check_1_11_LegacyAuth,
    "1.23": Check_1_23_CustomRoles,
    "2.1": Check_2_1_Domains,
    "3.1": Check_3_1_SigninRisk,
    "inactive_users": Check_InactiveUsers,
    "password_age": Check_PasswordAge,
}

# Define tier-based access using dictionary
FREE_TIER_CHECKS: Dict[str, Type[CheckProtocol]] = {
    "1.3": Check_1_3_SecurityDefaults,
    "1.5": Check_1_5_GuestRoles,
    "1.11": Check_1_11_LegacyAuth,
    "1.23": Check_1_23_CustomRoles,
    "2.1": Check_2_1_Domains,
    "password_age": Check_PasswordAge,
}

PREMIUM_CHECKS: Dict[str, Type[CheckProtocol]] = {
    "1.1": Check_1_1_MFA,
    "1.8": Check_1_8_SSPR,
    "3.1": Check_3_1_SigninRisk,
    "inactive_users": Check_InactiveUsers,
}

# For backward compatibility, also keep the lists
AVAILABLE_CHECKS_LIST = [
    Check_1_1_MFA,
    Check_1_3_SecurityDefaults,
    Check_1_5_GuestRoles,
    Check_1_8_SSPR,
    Check_1_11_LegacyAuth,
    Check_1_23_CustomRoles,
    Check_2_1_Domains,
    Check_3_1_SigninRisk,
    Check_PasswordAge,
    Check_InactiveUsers
]

PREMIUM_CHECKS_LIST = [
    Check_1_1_MFA,
    Check_1_8_SSPR,
    Check_3_1_SigninRisk,
    Check_InactiveUsers
]

FREE_TIER_CHECKS_LIST = [
    c for c in AVAILABLE_CHECKS_LIST if c not in PREMIUM_CHECKS_LIST
]

# ==============================================================================
# DYNAMIC DECLARATIVE BENCHMARK COMPILER
# ==============================================================================

def create_declarative_check_class(control_def) -> Type[CheckProtocol]:
    """Dynamically compile a ControlDefinition Pydantic model into a Check class."""
    from avaguard_core.checks.declarative_check import DeclarativeCheck
    
    try:
        severity_enum = CISSeverity[control_def.remediation_metadata.severity.upper()]
    except (KeyError, ValueError):
        severity_enum = CISSeverity.MEDIUM

    # Level 2 controls require premium tier licensing
    requires_premium = "level 2" in control_def.profile_level.lower() or getattr(control_def, "requires_premium", False)

    class DynamicDeclarativeCheck(DeclarativeCheck):
        CHECK_ID = control_def.control_id
        TITLE = control_def.title
        DESCRIPTION = control_def.category
        CIS_CONTROL_ID = control_def.control_id
        CATEGORY = control_def.category
        CIS_SEVERITY = severity_enum
        PRIORITY = control_def.remediation_metadata.severity.title()
        REQUIRES_PREMIUM = requires_premium
        API_PERMISSIONS_REQUIRED = control_def.scan_query.fields or []
        
        # Link back to the dynamic ControlDefinition specification
        CONTROL_DEF = control_def

        def __init__(self, graph_client=None, config: Optional[Dict] = None):
            super().__init__(control_def, graph_client, config)

    # Set class name dynamically based on control ID
    safe_name = control_def.control_id.replace(".", "_")
    DynamicDeclarativeCheck.__name__ = f"Check_{safe_name}"
    DynamicDeclarativeCheck.__qualname__ = f"Check_{safe_name}"
    
    return DynamicDeclarativeCheck


def load_and_compile_declarative_benchmarks():
    """Recursively scan declarative JSON folders and inject compiled checks into the global maps."""
    import os
    from pathlib import Path
    from avaguard_core.benchmarks.loader import BenchmarkLoader
    
    benchmarks_dir = Path(__file__).parent.parent / "benchmarks" / "azure"
    if not benchmarks_dir.exists() or not benchmarks_dir.is_dir():
        return
        
    loader = BenchmarkLoader("CIS Microsoft Azure Foundations Benchmark", "4.0.0", "azure")
    try:
        loader.load_directory(str(benchmarks_dir))
        
        for cid, control in loader.benchmark.controls.items():
            if control.deprecated:
                continue
                
            dynamic_class = create_declarative_check_class(control)
            
            # Register dynamically in AVAILABLE_CHECKS registry
            AVAILABLE_CHECKS[cid] = dynamic_class
            if dynamic_class not in AVAILABLE_CHECKS_LIST:
                AVAILABLE_CHECKS_LIST.append(dynamic_class)
            
            # Tier-based classification
            if dynamic_class.REQUIRES_PREMIUM:
                PREMIUM_CHECKS[cid] = dynamic_class
                if dynamic_class not in PREMIUM_CHECKS_LIST:
                    PREMIUM_CHECKS_LIST.append(dynamic_class)
            else:
                FREE_TIER_CHECKS[cid] = dynamic_class
                if dynamic_class not in FREE_TIER_CHECKS_LIST:
                    FREE_TIER_CHECKS_LIST.append(dynamic_class)
                    
    except Exception as e:
        import logging
        logging.getLogger(__name__).error(f"Failed to dynamically compile declarative benchmarks: {e}")


# Run the dynamic compilation routine
load_and_compile_declarative_benchmarks()


# Export everything
__all__ = [
    'BaseCheck', 'CheckResult', 'CheckStatus', 'CISSeverity',
    
    # Dictionaries (for desktop app)
    'AVAILABLE_CHECKS', 'FREE_TIER_CHECKS', 'PREMIUM_CHECKS',
    
    # Lists (for backward compatibility)
    'AVAILABLE_CHECKS_LIST', 'FREE_TIER_CHECKS_LIST', 'PREMIUM_CHECKS_LIST',
    
    # Individual check classes
    'Check_1_1_MFA', 'Check_1_3_SecurityDefaults', 'Check_1_5_GuestRoles',
    'Check_1_8_SSPR', 'Check_1_11_LegacyAuth', 'Check_1_23_CustomRoles',
    'Check_2_1_Domains', 'Check_3_1_SigninRisk', 'Check_InactiveUsers',
    'Check_PasswordAge'
]