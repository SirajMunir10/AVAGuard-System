# Troubleshooting: Password Reset Writeback (ADPermissionsError)

**Domain:** Entra ID
**Subdomain:** Password Reset Writeback
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot ADPermissionsError event in SSPR writeback?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** SSPR writeback configuration

## Symptoms
- Active Directory Management Agent (ADMA) service account does not have appropriate permissions to set a new password

## Error Codes
- `ADPermissionsError`

## Root Causes
1. ADMA account does not have reset password permissions on all objects in the forest
2. User's attribute AdminCount is set to 1

## Remediation Steps
1. Ensure that the ADMA account in the user's forest has reset password permissions on all objects in the forest
2. For more information on how to set the permissions, see Step 4: Set up the appropriate Active Directory permissions

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
