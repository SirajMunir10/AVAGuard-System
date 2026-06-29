# Troubleshooting: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Troubleshooting

## Scenario / Query
How does risk remediation work in Entra ID Identity Protection and what happens when a user is blocked due to risk-based policies?

## Environment Context
- **Tenant Type:** Entra ID tenant with Identity Protection enabled
- **Configuration:** Risk-based policies configured with specific risk levels

## Symptoms
- User is blocked during sign-in because they cannot perform the required access control step

## Error Codes
N/A

## Root Causes
1. Risk-based policy applied during sign-in where criteria are not met
2. User risk level matches configured policy level but user cannot perform required step (e.g., multifactor authentication or secure password change)

## Remediation Steps
1. Admin intervention is required to unblock the user
2. Administrators can determine that extra measures are necessary, such as blocking access from locations or lowering the acceptable risk in their policies

## Validation
1. Sign in to the Entra admin center as a Security Administrator. 2. Navigate to Protection > Identity Protection > Risky users. 3. Verify the user's risk level and confirm the user is listed with a status of 'Blocked' or 'At risk'. 4. Check the user's sign-in logs to confirm the most recent sign-in was blocked due to a risk-based policy. 5. Review the risk-based policy configuration under Protection > Identity Protection > Risk policies to ensure the policy is enabled and the assigned risk level matches the user's risk level.

## Rollback
1. If the remediation (e.g., dismissing user risk or unblocking the user) causes unintended access, sign in to the Entra admin center as a Security Administrator. 2. Navigate to Protection > Identity Protection > Risky users. 3. Select the user and choose 'Confirm user compromised' to reapply the block. 4. Alternatively, re-enable the risk-based policy that was disabled during remediation. 5. If the policy was modified, restore the original risk level threshold and policy settings from backup or documentation.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock>
