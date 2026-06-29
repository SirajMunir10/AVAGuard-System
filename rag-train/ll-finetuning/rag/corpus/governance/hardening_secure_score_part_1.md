# Hardening: Secure Score

**Domain:** Governance
**Subdomain:** Secure Score
**Incident Type:** Hardening

## Scenario / Query
A security administrator notices that the Microsoft Secure Score for their tenant has dropped by 15 points after a recent configuration change. The drop is linked to the improvement action 'Enable multifactor authentication for all users in administrative roles'. How can the administrator identify which users are missing MFA and remediate this to restore the Secure Score?

## Environment Context
- **Tenant Type:** Azure AD (Microsoft Entra ID) with P1 or P2 licenses
- **Configuration:** Conditional Access policies and MFA registration status

## Symptoms
- Microsoft Secure Score decreased by 15 points
- Improvement action 'Enable MFA for administrative roles' shows a status of 'Not completed' or 'Partially completed'
- Some or all users assigned to privileged roles (e.g., Global Administrator, Exchange Administrator) do not have MFA enforced

## Error Codes
N/A

## Root Causes
1. MFA is not enforced via Conditional Access policy for administrative roles
2. Users in administrative roles have not registered for MFA

## Remediation Steps
1. 1. Sign in to the Microsoft Entra admin center as a Global Administrator.
2. 2. Navigate to Identity > Secure Score > Improvement actions.
3. 3. Locate the action 'Enable MFA for administrative roles' and review the affected users list.
4. 4. Create a Conditional Access policy that requires MFA for all users in administrative roles (e.g., Global Administrator, Exchange Administrator, SharePoint Administrator).
5. 5. Alternatively, use the legacy per-user MFA configuration by going to Identity > Users > Per-user MFA and enabling MFA for each affected user.
6. 6. Instruct users to register for MFA at https://aka.ms/mfasetup or via the Microsoft Authenticator app.
7. 7. After enforcement, verify the improvement action status updates within 24â€“48 hours.

## Validation
After implementing the Conditional Access policy or per-user MFA, navigate back to Secure Score > Improvement actions and confirm the status of 'Enable MFA for administrative roles' changes to 'Completed' or 'Partially completed' with a higher score contribution.

## Rollback
To roll back, disable or delete the Conditional Access policy that requires MFA for administrative roles, or set per-user MFA to 'Disabled' for each affected user.

## References
- Microsoft Learn: 'Improvement action details â€“ Enable MFA for administrative roles' â€“ https://learn.microsoft.com/en-us/entra/identity/monitoring-health/improvement-actions#enable-mfa-for-administrative-roles
- CIS Microsoft 365 Foundation Benchmark v2.0.0 â€“ Control 1.1.1: 'Ensure multifactor authentication is enabled for all users in administrative roles'
