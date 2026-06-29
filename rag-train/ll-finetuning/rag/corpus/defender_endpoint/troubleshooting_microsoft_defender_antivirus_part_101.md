# Troubleshooting: Microsoft Defender Antivirus (0x8050A003)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error code 0x8050A003 with message ERR_MP_BADDB_OLDENGINE in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Error code 0x8050A003 displayed
- Message ERR_MP_BADDB_OLDENGINE displayed

## Error Codes
- `0x8050A003`
- `ERR_MP_BADDB_OLDENGINE`

## Root Causes
1. This error is internal. The cause isn't clearly defined.

## Remediation Steps
N/A

## Validation
1. Open Windows Security app and navigate to 'Virus & threat protection' > 'Protection updates' > 'Check for updates'. Verify that the latest security intelligence updates are installed. 2. Run the command 'Get-MpComputerStatus' in PowerShell as Administrator and confirm that 'AntivirusEnabled' is True and 'AMProductVersion' is a recent version (e.g., >= 4.18.2306.6). 3. Perform a quick scan using 'Start-MpScan -ScanType QuickScan' and check for any new errors. 4. Review the Microsoft Defender Antivirus operational event log (Event Viewer > Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational) for Event ID 1000 or 1001 indicating successful engine load.

## Rollback
1. If the error persists after updating, run the command 'MpCmdRun -RemoveDefinitions -All' to reset the definitions to a clean state, then re-run 'MpCmdRun -SignatureUpdate' to restore the latest definitions. 2. If the issue returns, use System Restore to revert to a point before the update: 'rstrui.exe' and select a restore point dated prior to the remediation. 3. As a last resort, reinstall Microsoft Defender Antivirus via PowerShell: 'Uninstall-WindowsFeature -Name Windows-Defender' (if applicable) then 'Install-WindowsFeature -Name Windows-Defender' and reboot.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
