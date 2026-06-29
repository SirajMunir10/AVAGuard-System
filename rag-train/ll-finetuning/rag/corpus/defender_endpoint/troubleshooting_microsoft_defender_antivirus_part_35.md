# Troubleshooting: Microsoft Defender Antivirus (2002)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to verify that the Microsoft Defender Antivirus engine was updated successfully using Event ID 2002?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 2002 with symbolic name MALWAREPROTECTION_ENGINE_UPDATED is logged

## Error Codes
- `2002`

## Root Causes
1. The antimalware engine updated successfully

## Remediation Steps
1. No action is necessary. The Microsoft Defender Antivirus client is in a healthy state.

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational.
3. Look for Event ID 2002 with source 'Windows Defender' and level 'Information'.
4. Confirm the event description includes 'The antimalware engine updated successfully' and shows the new engine version.
5. Optionally, run 'Get-MpComputerStatus | Select-Object AMEngineVersion' in PowerShell to verify the current engine version matches the event details.

## Rollback
No rollback is required because the engine update is a normal healthy operation. If the update caused unexpected behavior, contact Microsoft Support for assistance.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
