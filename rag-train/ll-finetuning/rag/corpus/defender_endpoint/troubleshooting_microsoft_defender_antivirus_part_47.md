# Troubleshooting: Microsoft Defender Antivirus (2041)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve Event ID 2041 indicating antimalware support for the operating system has ended?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 2041 with symbolic name MALWAREPROTECTION_OS_EOL is logged
- Message: Antimalware support for this operating system has ended. You must upgrade the operating system for continued support.

## Error Codes
- `2041`

## Root Causes
1. The support for your operating system has expired. Running Microsoft Defender Antivirus on an out of support operating system isn't an adequate solution to protect against threats.

## Remediation Steps
1. You must upgrade the operating system for continued support.

## Validation
1. Verify that the operating system has been upgraded to a supported version (e.g., Windows 10, Windows 11, or Windows Server 2016 or later).
2. Run the command: `Get-WmiObject -Namespace root\Microsoft\ProtectionManagement -Class MSFT_MpComputerStatus | Select-Object AMProductVersion, AMEngineVersion, AMServiceEnabled` to confirm Microsoft Defender Antivirus is active and up to date.
3. Check Event Viewer under Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational for Event ID 2041; ensure it no longer appears after the upgrade.
4. Run the command: `Get-MpComputerStatus | Select-Object AntivirusEnabled, AMServiceEnabled, RealTimeProtectionEnabled` to confirm real-time protection is enabled.

## Rollback
1. If the operating system upgrade fails or causes issues, restore the system to the previous state using a system backup or recovery point.
2. Reinstall the previous operating system version from installation media.
3. After rollback, verify that Microsoft Defender Antivirus is still functional by running: `Get-MpComputerStatus` and checking for any errors.
4. Monitor Event Viewer for Event ID 2041 to confirm the original issue persists, and consider alternative security measures (e.g., third-party antivirus) until a supported OS upgrade can be completed.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
