# Incident Response: Incident Response

**Domain:** Entra ID
**Subdomain:** Incident Response
**Incident Type:** Incident Response

## Scenario / Query
A security administrator notices that a large number of failed sign-ins are occurring from an unusual geographic location. How should the administrator use Entra ID Identity Protection to investigate and respond to this potential incident?

## Environment Context
- **Tenant Type:** Microsoft Entra ID P2 licensed tenant
- **Configuration:** Identity Protection enabled with default risk policies

## Symptoms
- Multiple failed sign-in attempts from an IP address in a country not typical for the organization
- Sign-in logs show risk events such as 'Atypical travel' or 'Anonymous IP address'

## Error Codes
N/A

## Root Causes
1. Compromised credentials being used from an unusual location
2. No conditional access policy blocking sign-ins from untrusted countries

## Remediation Steps
1. Review the risky sign-ins report in the Microsoft Entra admin center under Identity Protection > Risky sign-ins
2. Confirm the risk level and select 'Confirm sign-in compromised' if appropriate
3. Block the user account temporarily via Identity Protection or disable the account in Entra ID
4. Reset the user's password and require multi-factor authentication (MFA) re-registration
5. Create a conditional access policy to block sign-ins from the identified country or region

## Validation
Verify that the user can no longer sign in from the suspicious location and that no further risky sign-ins are reported for that user.

## Rollback
If the block was applied via conditional access policy, remove the country condition from the policy. If the user account was disabled, re-enable it after password reset.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk>
