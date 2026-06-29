# Hardening: Secure Score

**Domain:** Governance
**Subdomain:** Secure Score
**Incident Type:** Hardening

## Scenario / Query
A tenant's Microsoft Secure Score has dropped significantly because several identity hardening recommendations are not being applied. How can an administrator identify which specific recommendations are affecting the score and implement the required controls to improve the tenant's security posture?

## Environment Context
- **Tenant Type:** Enterprise (Microsoft 365 E5)
- **Configuration:** Azure AD P2 licenses enabled; Security defaults not enforced; Conditional Access policies partially deployed

## Symptoms
- Microsoft Secure Score value decreased by more than 10 points in the last 30 days
- Multiple identity-related recommendations show 'Not completed' status in the Secure Score dashboard
- Audit logs indicate no recent changes to Conditional Access policies or MFA registration

## Error Codes
N/A

## Root Causes
1. Administrators have not reviewed or acted upon Secure Score improvement actions for identity hardening
2. Security defaults are disabled, and no equivalent Conditional Access policies have been configured
3. Users are not required to register for multifactor authentication (MFA)

## Remediation Steps
1. Navigate to the Microsoft 365 Defender portal > Secure Score and filter by 'Identity' category to view all improvement actions
2. For each 'Not completed' action, review the detailed guidance provided in the Secure Score pane
3. Enable security defaults in Azure AD if appropriate, or create Conditional Access policies that enforce MFA, require compliant devices, and block legacy authentication as documented in 'Configure Microsoft Entra ID Protection' and 'Common Conditional Access policies'
4. Assign licenses and configure MFA registration policies to ensure all users complete registration

## Validation
After implementing the recommended improvement actions, verify that the Secure Score value increases within 24â€“48 hours and that the corresponding actions show 'Completed' status.

## Rollback
If security defaults were enabled, disable them via Azure AD > Properties > Manage Security defaults. If Conditional Access policies were created, delete or disable each policy in the Azure AD Conditional Access blade.

## References
- Microsoft Learn, 'What is Microsoft Secure Score?'
- Microsoft Learn, 'Common Conditional Access policies: Require MFA for all users' - https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/howto-conditional-access-policy-all-users-mfa
