# Troubleshooting: Windows Enrollment (0x80180014)

**Domain:** Intune
**Subdomain:** Windows Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve the error 'Your organization does not support this version of Windows' with error code 0x80180014 during Windows MDM enrollment?

## Environment Context
- **Tenant Type:** stand-alone Intune
- **Configuration:** Windows MDM enrollment disabled in Intune tenant

## Symptoms
- Error message: 'There was a problem. Your organization does not support this version of Windows.'
- Error code: 0x80180014

## Error Codes
- `0x80180014`

## Root Causes
1. Windows MDM enrollment is disabled in your Intune tenant

## Remediation Steps
1. In the Microsoft Intune admin center, choose Devices > Enrollment restrictions > choose a device type restriction.
2. Choose Properties > Edit (next to Platform settings) > Allow for Windows (MDM).
3. Click Review + Save.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-windows-enrollment-errors>
