# Troubleshooting: Microsoft Defender Antivirus (2040)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to handle Event ID 2040 indicating that antimalware support for the operating system version will soon end?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 2040 with symbolic name MALWAREPROTECTION_OS_EXPIRING
- Message: Antimalware support for this operating system version will soon end.

## Error Codes
- `2040`

## Root Causes
1. The support for your operating system expires shortly. Running Microsoft Defender Antivirus on an out of support operating system isn't an adequate solution to protect against threats.

## Remediation Steps
N/A

## Validation
1. Open Event Viewer and navigate to 'Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational'. 2. Verify that no new Event ID 2040 (MALWAREPROTECTION_OS_EXPIRING) appears. 3. Run the PowerShell command: Get-MpComputerStatus | Select-Object AMProductVersion, AMEngineVersion, AMServiceEnabled, AntispywareEnabled, AntivirusEnabled. Confirm all values are populated and the service is running. 4. Check the operating system version with: (Get-WmiObject Win32_OperatingSystem).Caption. Ensure it is a supported version per Microsoft documentation.

## Rollback
1. If the operating system is still supported but the warning persists, reinstall the latest Microsoft Defender Antivirus platform update from https://www.microsoft.com/en-us/wdsi/defenderupdates. 2. Run the PowerShell command: Update-MpSignature -UpdateSource MU to force signature update. 3. Restart the Microsoft Defender Antivirus service: Restart-Service WinDefend. 4. If the issue continues, restore the previous operating system version from a backup or roll back any recent OS updates via 'Settings > Update & Security > Recovery > Go back to the previous version of Windows 10'.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
