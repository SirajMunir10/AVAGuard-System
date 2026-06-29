# Governance: Privileged Identity Management (PIM)

**Domain:** Entra ID
**Subdomain:** Privileged Identity Management (PIM)
**Incident Type:** Governance

## Scenario / Query
A user reports they cannot activate a privileged role in Entra ID PIM, receiving an error that multifactor authentication (MFA) is required but they have already completed MFA. What configuration or policy issue could cause this, and how should it be resolved?

## Environment Context
- **Tenant Type:** Production
- **Configuration:** Entra ID PIM is configured with MFA requirement for role activation; Conditional Access policies may be interfering with PIM authentication context.

## Symptoms
- User cannot activate a PIM role despite completing MFA
- Error message indicates MFA is required
- No other sign-in issues outside of PIM activation

## Error Codes
N/A

## Root Causes
1. The Conditional Access policy requiring MFA for PIM activation does not include the 'Require authentication strength' or 'Require MFA' grant control correctly for the PIM authentication context
2. The user's authentication session does not satisfy the PIM activation policy because the MFA session is not fresh or is from a different context

## Remediation Steps
1. Review the Conditional Access policy that applies to PIM activation (targeting the 'Azure AD Privileged Identity Management' app or the 'Authentication Context' used by PIM). Ensure the policy includes the 'Require multifactor authentication' grant control.
2. Verify that the user's authentication session meets the MFA requirement by asking the user to sign out and sign in again, or perform a fresh MFA challenge before attempting activation.
3. If using authentication context, confirm that the PIM activation policy is correctly configured to use that context and that the Conditional Access policy targets that context.

## Validation
Ask the user to perform a fresh sign-in (closing all browser sessions) and attempt PIM activation again. If successful, the issue was stale session. If not, check the Conditional Access policy assignment and grant controls.

## Rollback
Temporarily remove the Conditional Access policy requiring MFA for PIM activation (not recommended for security) or add the user to an exclusion group for testing.

## References
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-activate-role>
