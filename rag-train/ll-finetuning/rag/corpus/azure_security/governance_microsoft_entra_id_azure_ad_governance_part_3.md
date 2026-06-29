# Governance: Microsoft Entra ID (Azure AD) Governance

**Domain:** Azure
**Subdomain:** Microsoft Entra ID (Azure AD) Governance
**Incident Type:** Governance

## Scenario / Query
A security administrator notices that several guest users in the tenant have been assigned highly privileged Azure AD roles (e.g., Global Administrator) without any approval or review. How can the administrator enforce just-in-time (JIT) access and require approval for privileged role assignments using Microsoft Entra Privileged Identity Management (PIM)?

## Environment Context
- **Tenant Type:** Microsoft Entra ID (Azure AD) tenant with P2 licenses
- **Configuration:** Privileged Identity Management not yet configured for Azure AD roles; guest users are assigned directly via Azure AD portal

## Symptoms
- Guest users appear in Global Administrator or other highâ€‘privilege roles
- No approval workflow exists for role assignments
- Role assignments are permanent (not timeâ€‘bound)
- No audit records of role activation requests

## Error Codes
N/A

## Root Causes
1. Privileged Identity Management (PIM) not activated for Azure AD roles
2. Role assignments were made directly instead of through PIM eligible assignments
3. No access reviews configured for guest users

## Remediation Steps
1. Activate Privileged Identity Management in the Microsoft Entra admin center (Identity Governance > Privileged Identity Management > Azure AD roles > Settings).
2. Convert existing permanent role assignments to eligible assignments that require activation with justification and approval.
3. Configure role settings to require approval for activation, set maximum activation duration, and require multiâ€‘factor authentication.
4. Create an access review for guest users with privileged roles to ensure they still need access.
5. Remove direct permanent role assignments for guest users and reassign through PIM eligible assignments.

## Validation
Verify that all guest users with privileged roles now have eligible assignments only, and that activating the role requires approval and MFA. Run the PIM audit history report to confirm no direct assignments remain.

## Rollback
If PIM causes access issues, temporarily revert a specific role assignment to permanent (direct) by using the Azure AD portal or Remove-AzureADMSRoleAssignment PowerShell cmdlet, then reapply the PIM configuration after troubleshooting.

## References
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-deployment-plan>
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/azure-ad-pim-approval-workflow>
