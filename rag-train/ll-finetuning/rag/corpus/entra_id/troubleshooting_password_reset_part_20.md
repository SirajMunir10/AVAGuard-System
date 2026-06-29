# Troubleshooting: Password Reset (OnBoardingConfigUpdateError)

**Domain:** Entra ID
**Subdomain:** Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve OnBoardingConfigUpdateError during SSPR writeback?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** SSPR writeback

## Symptoms
- Problem with writing or updating data in memory during onboarding

## Error Codes
- `OnBoardingConfigUpdateError`

## Root Causes
1. Problem with writing or updating data in memory before it's sent to the sync service

## Remediation Steps
1. Try disabling and then re-enabling password writeback to force a rewrite of this configuration file

## Validation
1. Sign in to the Entra admin center as a Global Administrator. 2. Navigate to Protection > Password reset > Properties. 3. Under the Password writeback section, confirm that the toggle for 'Allow users to reset their passwords using Microsoft Entra self-service password reset' is set to On. 4. Sign in to the server running Microsoft Entra Connect and open the Synchronization Service Manager. 5. Verify that the most recent synchronization cycle completed successfully with no errors related to password writeback. 6. As a test user, perform an SSPR operation and confirm the password is updated both in Entra ID and on-premises Active Directory.

## Rollback
1. Sign in to the Entra admin center as a Global Administrator. 2. Navigate to Protection > Password reset > Properties. 3. Under the Password writeback section, set the toggle for 'Allow users to reset their passwords using Microsoft Entra self-service password reset' to Off. 4. Wait for the next synchronization cycle to complete. 5. If the original issue persists, re-enable password writeback by setting the toggle back to On. 6. If problems continue, review the Microsoft Entra Connect health dashboard and event logs for further troubleshooting.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
