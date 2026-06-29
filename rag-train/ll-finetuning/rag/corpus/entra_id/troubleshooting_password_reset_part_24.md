# Troubleshooting: Password Reset (ADConfigurationError)

**Domain:** Entra ID
**Subdomain:** Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve password writeback failure due to Active Directory configuration issues?

## Environment Context
- **Tenant Type:** Microsoft Entra ID with SSPR writeback
- **Configuration:** Password writeback enabled; Microsoft Entra Connect configured

## Symptoms
- Password writeback fails
- Event indicating a configuration problem with Active Directory

## Error Codes
- `ADConfigurationError`

## Root Causes
1. Configuration issue with Active Directory preventing password writeback

## Remediation Steps
1. Check the Microsoft Entra Connect machine's Application event log for messages from the ADSync service for more information on which error occurred

## Validation
1. On the Microsoft Entra Connect server, open Event Viewer and navigate to 'Windows Logs > Application'. Filter by source 'ADSync'. Look for event IDs 6329, 31017, or 31019 that indicate successful password writeback operations. 2. Initiate a test password reset from the Microsoft Entra admin center for a user synchronized from on-premises Active Directory. 3. After the reset, verify the user can sign in with the new password on-premises. 4. Check the Microsoft Entra Connect server's Application event log for any new ADSync error events (e.g., event ID 6329 with error code 0x80230625). 5. Run the Microsoft Entra Connect wizard in 'Additional tasks' mode and select 'View current configuration' to confirm password writeback is enabled.

## Rollback
1. If the remediation fails, restore the original Active Directory configuration that was changed (e.g., revert any permission changes on the user object or organizational unit). 2. On the Microsoft Entra Connect server, open the Microsoft Entra Connect wizard, select 'Customize synchronization options', and uncheck 'Password writeback' to disable the feature temporarily. 3. Clear any cached credentials or stale writeback entries by restarting the Microsoft Entra Connect service (ADSync) from Services.msc. 4. Re-enable password writeback only after confirming the Active Directory configuration issue is resolved. 5. If the issue persists, refer to the official troubleshooting guide at https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback for further steps.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
