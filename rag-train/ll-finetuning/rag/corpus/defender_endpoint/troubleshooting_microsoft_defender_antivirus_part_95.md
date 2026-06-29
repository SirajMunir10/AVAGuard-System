# Troubleshooting: Microsoft Defender Antivirus (0x80508016)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Microsoft Defender Antivirus error code 0x80508016 with message ERR_MP_BAD_ACTION?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x80508016 displayed
- Message displayed: ERR_MP_BAD_ACTION

## Error Codes
- `0x80508016`

## Root Causes
1. This error is internal. The cause isn't clearly defined.

## Remediation Steps
N/A

## Validation
1. Open Event Viewer and navigate to 'Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational'. Verify that no new events with ID 1006, 1007, or 1008 related to error 0x80508016 appear after remediation.
2. Run the PowerShell command: Get-MpComputerStatus | Select-Object AMServiceEnabled, AMServiceVersion, AntispywareEnabled, AntivirusEnabled. Confirm all four properties return 'True'.
3. Execute a quick scan using: Start-MpScan -ScanType QuickScan. Verify the scan completes without error code 0x80508016.
4. Check the Microsoft Defender Antivirus client version by running: Get-MpComputerStatus | Select-Object AMProductVersion. Ensure it matches the latest version listed in official documentation.

## Rollback
1. If the error persists or new issues arise, restore the previous Microsoft Defender Antivirus policy configuration using Group Policy Management Console or Intune by reverting any recent changes to 'DisableAntiSpyware', 'DisableRealtimeMonitoring', or 'DisableBehaviorMonitoring' settings.
2. In an elevated PowerShell session, run: Set-MpPreference -DisableRealtimeMonitoring $false -DisableBehaviorMonitoring $false -DisableBlockAtFirstSeen $false to re-enable default protection features.
3. If a third-party antivirus was uninstalled, reinstall it and ensure it is registered with Windows Security Center.
4. As a last resort, use System Restore to revert to a point before the remediation was applied, selecting a restore point dated prior to the changes.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
