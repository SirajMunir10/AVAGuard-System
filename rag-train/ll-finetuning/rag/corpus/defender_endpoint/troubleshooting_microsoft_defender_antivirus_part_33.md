# Troubleshooting: Microsoft Defender Antivirus (1151)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to interpret Event ID 1151 (MALWAREPROTECTION_SERVICE_HEALTH_REPORT) for Microsoft Defender Antivirus client health?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 1151 logged with message: Endpoint Protection client health report (time in UTC)

## Error Codes
- `1151`

## Root Causes
1. Antivirus signature age may be 65535 days before first update
2. Antispyware signature age may be null before first update

## Remediation Steps
N/A

## Validation
Run the following PowerShell command to check the current signature age: Get-MpComputerStatus | Select-Object AntivirusSignatureAge, AntispywareSignatureAge. Confirm that AntivirusSignatureAge is not 65535 and AntispywareSignatureAge is not null. Also verify that the latest signature update succeeded by checking the last update time: Get-MpComputerStatus | Select-Object AntivirusSignatureLastUpdated, AntispywareSignatureLastUpdated. Then review Event ID 1151 in the System log to ensure no new instances with signature age anomalies appear.

## Rollback
If the remediation fails or causes issues, restore the previous signature state by forcing a signature update using: Update-MpSignature -UpdateSource MMPS. If the issue persists, reset the signature engine by running: & "$env:ProgramFiles\Windows Defender\MpCmdRun.exe" -RemoveDefinitions -All. Then re-run the update command. Finally, recheck the signature ages with Get-MpComputerStatus.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
