# Troubleshooting: Windows Enrollment (8018000a)

**Domain:** Intune
**Subdomain:** Windows Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error 8018000a indicating the device is already enrolled during Windows enrollment in Intune?

## Environment Context
- **Tenant Type:** Microsoft Entra ID / Intune
- **Configuration:** Windows device enrollment

## Symptoms
- Error message: 'Something went wrong. The device is already enrolled. You can contact your system administrator with the error code 8018000a.'
- Settings > Accounts > Work Access shows message: 'Another user on the system is already connected to a work or school. Please remove that work or school connection and try again.'

## Error Codes
- `8018000a`

## Root Causes
1. A different user has already enrolled the device in Intune or joined the device to Microsoft Entra ID.

## Remediation Steps
1. Sign out of Windows, then sign in by using the other account that has enrolled or joined the device.
2. Go to Settings > Accounts > Work Access, then remove the work or school account.
3. Sign out of Windows, then sign in by using your account.
4. Enroll the device in Intune or join the device to Microsoft Entra ID.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-windows-enrollment-errors>
