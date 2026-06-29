# Troubleshooting: Password Reset (InPutValidationError)

**Domain:** Entra ID
**Subdomain:** Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve InPutValidationError when using SSPR writeback?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** SSPR writeback

## Symptoms
- Input passed to the web service API was invalid

## Error Codes
- `InPutValidationError`

## Root Causes
1. Invalid input passed to the web service API

## Remediation Steps
1. Try the operation again

## Validation
1. Confirm that the SSPR writeback configuration is correct by running: `Get-MgPolicyAuthenticationMethodPolicy -AuthenticationMethodId 'password' | Select-Object -ExpandProperty PasswordResetSettings`. 2. Verify that the on-premises directory synchronization is healthy by checking the last successful sync time in the Azure AD Connect dashboard. 3. Attempt a test password reset operation for a user with SSPR writeback enabled and ensure no error is returned. 4. Review the Entra ID audit logs for the user to confirm the password writeback succeeded (look for event 'Password reset (self-service)' with status 'Success').

## Rollback
1. If the remediation fails, revert to the previous SSPR writeback configuration by restoring the settings from backup or re-applying the original configuration. 2. Disable and re-enable SSPR writeback via the Entra ID admin center: navigate to 'Password reset' > 'On-premises integration' and toggle the writeback setting off, then on again. 3. If the issue persists, run `Set-MgPolicyAuthenticationMethodPolicy -AuthenticationMethodId 'password' -PasswordResetSettings @{enablement = 'disabled'}` to temporarily disable SSPR writeback, then re-enable it after a few minutes. 4. As a last resort, contact Microsoft Support with the error details and tenant ID for further assistance.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
