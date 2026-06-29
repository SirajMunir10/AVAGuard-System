# Troubleshooting: Password Reset

**Domain:** Entra ID
**Subdomain:** Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve password writeback access denied error due to ADMA account permissions?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Microsoft Entra Connect with password writeback enabled

## Symptoms
- Federated, pass-through authentication, or password-hash-synchronized users see an error after attempting to submit their password
- Error indicates that there was a service problem
- On-premises event logs show an error that the management agent was denied access

## Error Codes
N/A

## Root Causes
1. Active Directory Management Agent (ADMA) account specified during configuration lacks necessary permissions for password writeback

## Remediation Steps
1. Check that the ADMA account specified during configuration has the necessary permissions for password writeback
2. After permission is given, it can take up to one hour for the permissions to trickle down via the sdprop background task on the domain controller (DC)

## Validation
Password reset continues to fail with an access denied message until permission shows up on the user object

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
