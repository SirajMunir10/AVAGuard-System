# Troubleshooting: Microsoft Defender Antivirus (2021)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Event ID 2021 where the antimalware engine failed to download a clean file in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- The antimalware engine failed to download a clean file.

## Error Codes
- `2021`

## Root Causes
1. Network connectivity issue when using the Dynamic Signature Service to download the latest definitions to a specific threat.

## Remediation Steps
1. Check your Internet connectivity settings.

## Validation
1. Run 'Get-MpComputerStatus | Select-Object AMProductVersion, AMEngineVersion, AMServiceEnabled, AMServiceVersion' to confirm the antimalware engine is running and up to date.
2. Check the latest definition update time: 'Get-MpComputerStatus | Select-Object AntivirusSignatureLastUpdated'.
3. Verify network connectivity to the Dynamic Signature Service by running 'Test-NetConnection -ComputerName definitions.microsoft.com -Port 443'.
4. Review the Microsoft-Windows-Windows Defender/Operational event log for Event ID 2021 to ensure no new occurrences.
5. Force a definition update: 'Update-MpSignature' and confirm success with no errors.

## Rollback
1. If connectivity changes caused issues, restore original proxy or firewall settings that were modified.
2. If a manual proxy was configured, revert to automatic detection: 'Set-MpPreference -ProxyBypass $true -ProxyServer $null'.
3. If network restrictions were removed, reapply them as needed.
4. Restart the Microsoft Defender Antivirus service: 'Restart-Service -Name WinDefend'.
5. Re-run 'Update-MpSignature' to ensure definitions are still current after rollback.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
