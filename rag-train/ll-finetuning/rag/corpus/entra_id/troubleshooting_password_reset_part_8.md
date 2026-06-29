# Troubleshooting: Password Reset (ADPasswordPolicyError)

**Domain:** Entra ID
**Subdomain:** Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve password writeback failure due to on-premises password policy violations?

## Environment Context
- **Tenant Type:** Microsoft Entra ID with SSPR writeback
- **Configuration:** Password writeback enabled; on-premises password policies (age, history, complexity, filters)

## Symptoms
- Password reset or change operation fails
- Event indicating password does not meet domain policy requirements

## Error Codes
- `ADPasswordPolicyError`

## Root Causes
1. Password does not meet minimum password age requirements
2. Password violates password history requirements (recently used password)
3. Password does not meet complexity requirements
4. Password fails filtering criteria from password filters

## Remediation Steps
1. For testing purposes, set minimum password age to 0
2. For testing purposes, set password history to 0
3. Select a password that meets all complexity requirements
4. Select a password that passes any enabled password filters

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
