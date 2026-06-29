# Troubleshooting: Self-Service Password Reset (UserNotLicensed = 12)

**Domain:** Entra ID
**Subdomain:** Self-Service Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
A user sees error 'We're sorry, you can't reset your password at this time because required licenses are missing from your organization.' What is the cause and how to resolve?

## Environment Context
- **Tenant Type:** Microsoft Entra
- **Configuration:** License assignment

## Symptoms
- User cannot reset password
- Error message: 'We're sorry, you can't reset your password at this time because required licenses are missing from your organization.'

## Error Codes
- `UserNotLicensed = 12`
- `SSPR_0012: Your organization doesn't have the required licenses necessary to perform password reset.`

## Root Causes
1. Required licenses are missing from the organization.

## Remediation Steps
1. Contact your admin and ask them to check your license assignment.

## Validation
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) as a Global Administrator. 2. Navigate to Identity > Users > All users. 3. Select the affected user. 4. Under 'Licenses', verify that a license that includes Microsoft Entra ID P1 or P2 (e.g., Microsoft Entra ID P2, Enterprise Mobility + Security E5) is assigned. 5. Alternatively, run the Microsoft Graph PowerShell command: Get-MgUserLicenseDetail -UserId 'user@domain.com' | Select-Object SkuPartNumber. Confirm the output includes a SKU like 'EMSPREMIUM' or 'AAD_PREMIUM_P2'.

## Rollback
1. If the license assignment was added incorrectly, sign in to the Microsoft Entra admin center as a Global Administrator. 2. Navigate to Identity > Users > All users. 3. Select the affected user. 4. Under 'Licenses', select the license that was assigned and click 'Remove license'. 5. Confirm the removal. 6. Alternatively, run the Microsoft Graph PowerShell command: Remove-MgUserLicense -UserId 'user@domain.com' -AddLicenses @() -RemoveLicenses @('SKU_ID'). Replace 'SKU_ID' with the actual SKU identifier (e.g., 'contoso:EMSPREMIUM').

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr>
