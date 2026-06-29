# Hardening: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Hardening

## Scenario / Query
How to distinguish between password change for risk remediation and self-service password reset (SSPR) for account recovery in Entra ID Identity Protection?

## Environment Context
- **Tenant Type:** Entra ID tenant with Identity Protection enabled
- **Configuration:** Risk-based Conditional Access policies with Require password change or Require risk remediation grant controls

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. For risk remediation (password change): The user knows their current password, authenticates with multifactor authentication (MFA), and then changes their password. This is the mechanism used by risk-based Conditional Access policies, including the Require password change and Require risk remediation grant controls. This flow doesn't use self-service password reset (SSPR).
2. For account recovery (password reset): The user doesn't know their password and uses self-service password reset (SSPR) or an admin-initiated reset to recover access. A password reset through SSPR also remediates user risk.

## Validation
1. Sign in to the Entra admin center as a Security Administrator. 2. Navigate to Identity Protection > Risky users. 3. Select a user who was recently remediated via a risk-based Conditional Access policy. 4. Review the 'Risk detail' column: if the remediation was a password change (user knew password and used MFA), the detail should show 'User passed MFA driven by risk policy' and 'User changed password securely'. 5. For a user who used SSPR (did not know password), the risk detail should show 'User performed self-service password reset' or 'Admin reset password'. 6. Confirm that the user's risk level is now 'None' and the 'Risk state' is 'Remediated'.

## Rollback
1. If the password change remediation caused issues (e.g., user locked out or unable to authenticate), an admin can reset the user's password via Entra admin center > Users > select user > Reset password. 2. To revert a risk remediation that was incorrectly applied, navigate to Identity Protection > Risky users, select the user, and choose 'Dismiss user risk' to reset the risk state to 'Dismissed' (note: this does not undo the password change but removes the risk flag). 3. If the user's risk was remediated via SSPR but should have been a password change, ensure the user's SSPR registration is reviewed and, if needed, disable SSPR for that user via Authentication methods > Policies > Self-service password reset > select user > Block. 4. For Conditional Access policy misconfiguration, edit the policy to remove the 'Require password change' or 'Require risk remediation' grant control and save.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock>
