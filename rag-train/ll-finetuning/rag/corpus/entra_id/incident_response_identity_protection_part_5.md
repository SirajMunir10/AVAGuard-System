# Incident Response: Identity Protection (50053)

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Incident Response

## Scenario / Query
How to unblock a user account that was blocked by Microsoft Entra ID Protection due to high confidence sign-in risk?

## Environment Context
- **Tenant Type:** Microsoft Entra ID tenant with Identity Protection enabled
- **Configuration:** Risk-based sign-in or user risk policies configured

## Symptoms
- User receives 50053 authentication error
- Sign-in logs display block reason: 'Sign-in was blocked by built-in protections due to high confidence of risk.'

## Error Codes
- `50053`

## Root Causes
1. Sign-in attempt from an unfamiliar location or device
2. Sign-in performed using legacy authentication protocols
3. Sign-in displaying properties of a malicious attempt

## Remediation Steps
1. User can sign-in from a familiar location or device to try and unblock the sign-in; if successful, Microsoft ID Protection automatically remediates the sign-in risk (risk state changes from 'At risk' to 'Dismissed', risk detail changes from '-' to 'Microsoft Entra ID Protection assessed sign-in safe').
2. Exclude specific users from the sign-in or user risk policy if the current configuration is causing issues for those users (confirm it is safe to grant access without applying the policy).
3. Manually dismiss the risk or user so they can sign in.
4. Disable the policy if the configuration is causing issues for all users (manually dismiss risk or user before addressing the policy).
5. Add the IPs being used to sign in to the Trusted location settings if the sign-in is from a known company location.
6. Use a modern authentication protocol if the sign-in was performed using a legacy protocol.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock>
