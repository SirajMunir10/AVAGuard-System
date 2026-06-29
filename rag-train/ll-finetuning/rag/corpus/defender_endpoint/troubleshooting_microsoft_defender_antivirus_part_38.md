# Troubleshooting: Microsoft Defender Antivirus (2007)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve Event ID 2007 indicating the Microsoft Defender Antivirus platform will soon be out of date?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 2007 logged with message: The platform will soon be out of date. Download the latest platform to maintain up-to-date protection.

## Error Codes
- `2007`

## Root Causes
1. Microsoft Defender Antivirus will soon require a newer platform version to support future versions of the antimalware engine.

## Remediation Steps
1. Download the latest Microsoft Defender Antivirus platform to maintain the best level of protection available.

## Validation
1. Run 'Get-MpComputerStatus' in PowerShell and verify that 'AMProductVersion' and 'AMEngineVersion' are the latest versions listed at https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/manage-updates-baselines-microsoft-defender-antivirus. 2. Check the System event log for Event ID 2007; confirm no new occurrences after the update. 3. Verify that Microsoft Defender Antivirus is running and up-to-date by opening Windows Security > Virus & threat protection > Check for updates.

## Rollback
1. If the update fails or causes issues, uninstall the latest platform update via Control Panel > Programs > View installed updates, locate 'Microsoft Defender Antivirus' or 'Microsoft Defender Antivirus Platform Update', and select Uninstall. 2. Alternatively, run 'Start-Process "C:\Program Files\Windows Defender\MpCmdRun.exe" -ArgumentList "-RemoveDefinitions -All"' in PowerShell to revert to the previous platform version. 3. Reboot the device and verify that Event ID 2007 does not reappear; if it does, reapply the update from the Microsoft Update Catalog.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
