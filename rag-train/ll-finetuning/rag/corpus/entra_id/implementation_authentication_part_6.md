# Implementation: Authentication

**Domain:** Entra ID
**Subdomain:** Authentication
**Incident Type:** Implementation

## Scenario / Query
How to license and enable Microsoft Entra multifactor authentication for users and administrators?

## Environment Context
- **Tenant Type:** Microsoft 365 or Microsoft Entra ID
- **Configuration:** Conditional Access policies

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enable Microsoft Entra multifactor authentication by using Conditional Access.
2. For more information, see Common Conditional Access policy: Require MFA for all users.

## Validation
1. Confirm that the Conditional Access policy requiring MFA is enabled and applied to all users: run `Get-MgIdentityConditionalAccessPolicy -Filter "displayName eq 'Require MFA for all users'" | Select-Object Id, DisplayName, State` in Microsoft Graph PowerShell. Verify State is 'enabled'. 2. Test MFA enforcement by signing in as a test user and ensuring MFA prompt appears. 3. Check sign-in logs for MFA requirement: run `Get-MgAuditLogSignIn -Filter "userPrincipalName eq 'testuser@domain.com'" -Top 1 | Select-Object UserPrincipalName, ConditionalAccessStatus, MfaDetail` and confirm ConditionalAccessStatus is 'success' and MfaDetail includes 'satisfied'.

## Rollback
1. Disable the Conditional Access policy: run `Update-MgIdentityConditionalAccessPolicy -ConditionalAccessPolicyId "<policy-id>" -State "disabled"` in Microsoft Graph PowerShell. 2. Remove the policy if needed: run `Remove-MgIdentityConditionalAccessPolicy -ConditionalAccessPolicyId "<policy-id>"`. 3. Verify MFA is no longer enforced by signing in as a test user and confirming no MFA prompt appears. 4. Check sign-in logs to confirm MFA is not required: run `Get-MgAuditLogSignIn -Filter "userPrincipalName eq 'testuser@domain.com'" -Top 1 | Select-Object UserPrincipalName, ConditionalAccessStatus, MfaDetail` and verify ConditionalAccessStatus is 'notApplied' or MfaDetail is empty.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mfa-licensing>
