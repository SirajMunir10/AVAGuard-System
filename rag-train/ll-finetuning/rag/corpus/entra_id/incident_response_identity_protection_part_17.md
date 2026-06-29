# Incident Response: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Incident Response

## Scenario / Query
How to manually remediate sign-in or user risk when risk-based policies are not configured or risk level does not meet self-remediation criteria?

## Environment Context
- **Tenant Type:** Entra ID tenant with Identity Protection enabled
- **Configuration:** Risk-based policies may not be configured or risk level may not meet self-remediation criteria

## Symptoms
- Risk-based policies are not configured
- Risk level does not meet criteria for self-remediation
- Time is of the essence for remediation

## Error Codes
N/A

## Root Causes
1. Risk-based policies not configured
2. Risk level insufficient for self-remediation
3. Urgent need for manual intervention

## Remediation Steps
1. Generate a temporary password for the user
2. Require the user to change their password
3. Dismiss the user's risk
4. Confirm the user is compromised and take action to secure the account
5. Unblock the user

## Validation
1. Sign in to the Microsoft Entra admin center as a Security Administrator or Global Administrator. 2. Navigate to Protection > Identity Protection > Risky users. 3. Locate the user account that was remediated. 4. Verify that the user's risk level now shows 'Dismissed' or 'Remediated' (not 'At risk'). 5. Confirm the user can sign in with the new temporary password by attempting a test sign-in. 6. Check the user's audit logs (Protection > Identity Protection > Audit logs) for the 'Dismiss user risk' and 'Generate temporary password' actions. 7. If the user was blocked, verify the block is removed by checking the user's sign-in logs for successful sign-ins after remediation.

## Rollback
1. If the temporary password was generated but not yet used, reset the password again to a known secure value and communicate it securely to the user. 2. If user risk was dismissed in error, re-confirm the user as compromised: In Identity Protection > Risky users, select the user and choose 'Confirm compromised'. 3. If the user was unblocked but should remain blocked, re-block the user: In Azure AD > Users > select the user > Sign-ins > block sign-in. 4. If the password change requirement was removed, re-enforce it by resetting the user's password again and requiring change on next sign-in. 5. Document the rollback actions in the incident response log.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock>
