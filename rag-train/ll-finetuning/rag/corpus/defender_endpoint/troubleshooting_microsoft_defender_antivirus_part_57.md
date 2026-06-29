# Troubleshooting: Microsoft Defender Antivirus (5011)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to interpret Event ID 5011 indicating Microsoft Defender Antivirus scanning is enabled?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 5011 logged with message: Scanning for viruses is enabled.

## Error Codes
- `5011`

## Root Causes
1. Microsoft Defender Antivirus enabled scanning for viruses.

## Remediation Steps
N/A

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to 'Applications and Services Logs' > 'Microsoft' > 'Windows' > 'Windows Defender' > 'Operational'.
3. Verify that Event ID 5011 is logged with the message 'Scanning for viruses is enabled.'
4. Confirm that no related error events (e.g., 5007, 5010) are present.
5. Run 'Get-MpComputerStatus' in PowerShell to verify that 'AntivirusEnabled' is True.

## Rollback
1. If Event ID 5011 is missing or indicates scanning is disabled, run 'Set-MpPreference -DisableRealtimeMonitoring $false' in PowerShell as Administrator.
2. Restart the 'Microsoft Defender Antivirus' service via 'net start WinDefend'.
3. Verify the change by checking Event ID 5011 reappears with 'Scanning for viruses is enabled.'
4. If issues persist, review Group Policy or registry settings under 'HKLM\SOFTWARE\Policies\Microsoft\Windows Defender' to ensure no policy disables scanning.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
