# Troubleshooting: Password Reset (6329)

**Domain:** Entra ID
**Subdomain:** Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
How to fix password writeback configuration error after adding a new Active Directory forest?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Microsoft Entra Connect with password writeback enabled

## Symptoms
- Password operations fail with a configuration error
- Application event log contains Microsoft Entra Connect error 6329 with text '0x8023061f (The operation failed because password synchronization isn't enabled on this Management Agent)'

## Error Codes
- `6329`
- `0x8023061f`

## Root Causes
1. Microsoft Entra Connect configuration changed to add a new Active Directory forest (or remove and read an existing forest) after password writeback was already enabled

## Remediation Steps
1. Disable and then re-enable the password writeback feature after the forest configuration changes are complete

## Validation
1. Open the Microsoft Entra Connect wizard and select 'View current configuration' to confirm the new forest is listed and password writeback is enabled. 2. On the Entra Connect server, open Event Viewer, navigate to 'Applications and Services Logs/Microsoft/Operational/Microsoft Entra Connect/PasswordHashSync', and verify no new error 6329 events with code 0x8023061f appear after a test password change. 3. Initiate a password reset or change for a user in the new forest and confirm the operation completes without error. 4. Run the PowerShell command `Get-ADSyncGlobalSettings | Where-Object {$_.Name -like '*PasswordWriteback*'}` to confirm the feature is enabled.

## Rollback
1. Open the Microsoft Entra Connect wizard and select 'Customize synchronization options'. 2. On the 'Optional features' page, clear the 'Password writeback' checkbox and complete the wizard to disable the feature. 3. Re-run the wizard, re-select 'Password writeback', and complete the wizard to re-enable it. 4. If the error persists, verify the new forest's connectivity and permissions by running the Microsoft Entra Connect troubleshooting tool or reviewing the 'Microsoft Entra Connect Sync: Password writeback configuration' documentation. 5. As a last resort, temporarily disable password writeback and contact Microsoft Support for further assistance.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
