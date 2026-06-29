# Troubleshooting: Microsoft Defender Antivirus (2030)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to interpret Event ID 2030 indicating that the antimalware engine was downloaded and configured to run offline on the next system restart?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 2030 with symbolic name MALWAREPROTECTION_OFFLINE_SCAN_INSTALLED is logged
- Message: The antimalware engine was downloaded and is configured to run offline on the next system restart

## Error Codes
- `2030`

## Root Causes
1. Microsoft Defender Antivirus downloaded and configured offline antivirus to run on the next reboot

## Remediation Steps
N/A

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational.
3. Verify that Event ID 2030 with source 'Windows Defender' and message 'The antimalware engine was downloaded and is configured to run offline on the next system restart' is present.
4. Confirm that no subsequent Event ID 2001 (engine update failure) or Event ID 2002 (engine update succeeded) appears after the 2030 event.
5. Check the current engine version by running: Get-MpComputerStatus | Select-Object AMEngineVersion, AMProductVersion, AMServiceEnabled.
6. Restart the device and verify that the offline scan completes by checking for Event ID 1001 (scan completed) or Event ID 1002 (scan failed) in the same log.

## Rollback
1. If the offline scan causes issues (e.g., system hangs or boot failure), boot into Safe Mode.
2. Open an elevated PowerShell prompt and disable the scheduled offline scan by running: Set-MpPreference -DisableScanningMeteredConnections $true -DisableCatchupFullScan $true -DisableCatchupQuickScan $true.
3. Remove any pending offline scan configuration by deleting the registry key: Remove-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows Defender\Scan' -Name 'OfflineScanScheduled' -ErrorAction SilentlyContinue.
4. Restart the system normally.
5. Re-enable scanning as needed: Set-MpPreference -DisableScanningMeteredConnections $false -DisableCatchupFullScan $false -DisableCatchupQuickScan $false.
6. Verify that Event ID 2030 no longer appears and that the engine is running online by checking Get-MpComputerStatus.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
