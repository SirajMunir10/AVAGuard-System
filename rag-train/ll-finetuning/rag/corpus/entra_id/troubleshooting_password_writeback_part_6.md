# Troubleshooting: Password Writeback (0x80230619)

**Domain:** Entra ID
**Subdomain:** Password Writeback
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve password writeback failure due to domain password policy restrictions (age, history, complexity, or filtering)?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Password writeback enabled, Azure AD Connect sync

## Symptoms
- Event source: ADSync BAIL: MMS(4924) 0x80230619
- Password change or reset fails

## Error Codes
- `0x80230619`

## Root Causes
1. Password does not meet minimum password age requirement
2. Password has been used recently (password history violation)
3. Password does not meet complexity requirements
4. Password fails filtering criteria
5. User has PASSWD_CANT_CHANGE property flag set

## Remediation Steps
1. Set minimum password age to 0 for testing
2. Set password history to 0 for testing
3. Ensure password meets complexity requirements
4. Remove or adjust password filters
5. Remove the PASSWD_CANT_CHANGE property flag from the user

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
