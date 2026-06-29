# Troubleshooting: Password Reset Writeback (ADUnKnownError)

**Domain:** Entra ID
**Subdomain:** Password Reset Writeback
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot ADUnKnownError event in SSPR writeback?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** SSPR writeback configuration

## Symptoms
- Unknown error returned by Active Directory

## Error Codes
- `ADUnKnownError`

## Root Causes
1. Unknown error returned by Active Directory

## Remediation Steps
1. Check the Microsoft Entra Connect server event log for events from the ADSync source for more information

## Validation
1. On the Microsoft Entra Connect server, open Event Viewer and navigate to 'Windows Logs > Application'. 2. Filter the current log by source 'ADSync'. 3. Look for events with IDs 6329, 6325, or 6323 that contain details about the writeback operation. 4. Confirm that no new ADUnKnownError events appear in the Entra ID audit logs after the remediation. 5. Perform a test SSPR writeback by resetting a password for a test user and verify the password is updated in on-premises Active Directory.

## Rollback
1. If the remediation fails, revert any changes made to the Microsoft Entra Connect configuration by restoring the previous settings from backup. 2. Re-enable SSPR writeback if it was disabled during troubleshooting: Set-MsolDirSyncEnabled -EnableDirSync $true. 3. Restart the Microsoft Entra Connect Sync service: Restart-Service 'ADSync'. 4. If the issue persists, restore the on-premises Active Directory user's password to its previous value using Active Directory Users and Computers.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
