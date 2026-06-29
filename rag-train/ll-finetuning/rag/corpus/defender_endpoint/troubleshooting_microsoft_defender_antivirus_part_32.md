# Troubleshooting: Microsoft Defender Antivirus (1127)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Event ID 1127 (Controlled Folder Access blocking an untrusted process from modifying disk sectors)?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** Controlled Folder Access (CFA) enabled

## Symptoms
- Event ID 1127 with symbolic name MALWAREPROTECTION_FOLDER_GUARD_SECTOR_BLOCK
- Message: Controlled Folder Access(CFA) blocked an untrusted process from making changes to the memory
- Description: Controlled Folder Access blocked an untrusted process from potentially modifying disk sectors

## Error Codes
- `1127`

## Root Causes
1. Controlled Folder Access blocked an untrusted process from accessing a device or disk for modification

## Remediation Steps
1. Add the blocked process to the Allowed Process list for CFA using PowerShell or Windows Security Center

## Validation
1. Open Event Viewer and navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational. Verify that no new Event ID 1127 appears for the same process after remediation. 2. Run the PowerShell command: Get-MpPreference | Select-Object -ExpandProperty ControlledFolderAccessAllowedApplications. Confirm the previously blocked process is listed. 3. Attempt to reproduce the original action that triggered the block (e.g., run the process or perform the disk modification) and confirm it completes without error or block notification.

## Rollback
1. Open Windows Security Center > Virus & threat protection > Manage ransomware protection > Allow an app through Controlled folder access. Remove the added process from the allowed list. 2. Alternatively, run PowerShell: Remove-MpPreference -ControlledFolderAccessAllowedApplications -Paths "<FullPathToProcess>". 3. Verify removal by running: Get-MpPreference | Select-Object -ExpandProperty ControlledFolderAccessAllowedApplications. Confirm the process is no longer listed. 4. Re-test the original action to ensure Controlled Folder Access blocking behavior is restored.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
