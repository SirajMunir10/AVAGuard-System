# Troubleshooting: Self-Service Password Reset

**Domain:** Entra ID
**Subdomain:** Self-Service Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
The user never receives the password reset SMS or phone call.

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Phone number format

## Symptoms
- User does not receive SMS or phone call for password reset

## Error Codes
N/A

## Root Causes
1. The phone number in the directory may be malformed
2. Password reset doesn't support extensions, even if you specify one in the directory. The extensions are stripped before the call is made

## Remediation Steps
1. Make sure the phone number is in the format '+1 4251234567'
2. Use a number without an extension, or integrate the extension into the phone number in your private branch exchange (PBX)

## Validation
1. Verify the user's phone number format in Microsoft Entra ID: run `Get-MgUser -UserId <userPrincipalName> -Property BusinessPhones, MobilePhone | Format-List BusinessPhones, MobilePhone` in Microsoft Graph PowerShell. Confirm the number matches the required format '+1 4251234567' (country code, space, area code, and number) with no extension. 2. If an extension was previously present, confirm it has been removed or integrated into the PBX. 3. Initiate a test password reset for the user via the SSPR portal and confirm the SMS or phone call is received within a few minutes.

## Rollback
1. If the user still does not receive the SMS or phone call after correcting the phone number format, restore the original phone number (including any extension) by running `Update-MgUser -UserId <userPrincipalName> -MobilePhone '<originalNumber>'` in Microsoft Graph PowerShell. 2. Verify the original number is set by running `Get-MgUser -UserId <userPrincipalName> -Property MobilePhone | Format-List MobilePhone`. 3. Document the issue and escalate to Microsoft support if the problem persists, referencing the troubleshooting guide at https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr>
