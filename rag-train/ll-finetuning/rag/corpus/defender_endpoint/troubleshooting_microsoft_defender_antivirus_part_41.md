# Troubleshooting: Microsoft Defender Antivirus (Event ID 2013)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Event ID 2013 indicating that the Dynamic Signature Service deleted all dynamic definitions in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 2013 is logged with symbolic name MALWAREPROTECTION_SIGNATURE_FASTPATH_DELETED_ALL
- Message: The Dynamic Signature Service deleted all dynamic definitions
- Description: Microsoft Defender Antivirus discarded all Dynamic Signature Service signatures

## Error Codes
- `Event ID 2013`

## Root Causes
1. Microsoft Defender Antivirus discarded all Dynamic Signature Service signatures

## Remediation Steps
N/A

## Validation
1. Open Event Viewer and navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational. 2. Verify that no new Event ID 2013 entries appear after remediation. 3. Run the PowerShell command: Get-MpComputerStatus | Select-Object AntivirusSignatureVersion, AntispywareSignatureVersion, QuickScanSignatureVersion, EngineVersion. 4. Confirm that the signature versions are current and not empty. 5. Run: Get-MpPreference | Select-Object DisableRealtimeMonitoring, DisableBehaviorMonitoring, DisableBlockAtFirstSeen. Ensure these are set to False. 6. Perform a manual signature update: Update-MpSignature. 7. Run a quick scan: Start-MpScan -ScanType QuickScan. 8. Check for any new Event ID 2013 or related errors in the Operational log.

## Rollback
1. If the remediation introduced issues, restore the previous Microsoft Defender Antivirus policy settings via Group Policy or Intune. 2. Revert any changes to registry keys under HKLM\Software\Policies\Microsoft\Windows Defender\Signature Updates. 3. If a manual signature update was forced, allow the next automatic update cycle to occur (typically every 8 hours). 4. Restart the Microsoft Defender Antivirus service: Restart-Service -Name WinDefend. 5. If the service fails to start, set the startup type back to Automatic: Set-Service -Name WinDefend -StartupType Automatic. 6. Re-enable any disabled real-time protection: Set-MpPreference -DisableRealtimeMonitoring $false. 7. Reapply any custom exclusions that were removed during troubleshooting. 8. If the issue persists, contact Microsoft Support with the Event ID 2013 logs and the steps taken.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
