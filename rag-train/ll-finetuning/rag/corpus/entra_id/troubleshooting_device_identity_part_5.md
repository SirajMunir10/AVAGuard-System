# Troubleshooting: Device Identity (STATUS_NO_SUCH_LOGON_SESSION (-1073741729/ 0xc000005f))

**Domain:** Entra ID
**Subdomain:** Device Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve STATUS_NO_SUCH_LOGON_SESSION (-1073741729/ 0xc000005f) error during hybrid join?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- User realm discovery failed because the Microsoft Entra authentication service was unable to find the user's domain

## Error Codes
- `STATUS_NO_SUCH_LOGON_SESSION (-1073741729/ 0xc000005f)`

## Root Causes
1. The domain of the user's UPN must be added as a custom domain in Microsoft Entra ID
2. If the on-premises domain name is nonroutable (jdoe@contoso.local), configure an Alternate Login ID (AltID)

## Remediation Steps
1. Add the domain of the user's UPN as a custom domain in Microsoft Entra ID
2. If the on-premises domain name is nonroutable (jdoe@contoso.local), configure an Alternate Login ID (AltID)

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
