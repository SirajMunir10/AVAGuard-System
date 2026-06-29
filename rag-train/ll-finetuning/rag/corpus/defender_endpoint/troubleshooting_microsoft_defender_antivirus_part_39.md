# Troubleshooting: Microsoft Defender Antivirus (2010)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to interpret Event ID 2010 indicating Microsoft Defender Antivirus used cloud protection to retrieve additional security intelligence?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 2010 logged with MALWAREPROTECTION_SIGNATURE_FASTPATH_UPDATED

## Error Codes
- `2010`

## Root Causes
1. Microsoft Defender Antivirus used cloud protection (cloud-delivered protection), previously referred to as Dynamic Signature Service, to retrieve additional security intelligence

## Remediation Steps
N/A

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational.
3. Verify that Event ID 2010 is logged with the message containing 'MALWAREPROTECTION_SIGNATURE_FASTPATH_UPDATED'.
4. Confirm the event indicates cloud protection successfully retrieved additional security intelligence.
5. Optionally, run the PowerShell command: Get-MpComputerStatus | Select-Object -Property CloudProtectionEnabled, CloudBlockLevel, CloudTimeout. Ensure CloudProtectionEnabled is True.

## Rollback
No rollback is required because Event ID 2010 is an informational event indicating normal cloud protection operation. If cloud protection is undesired, disable it via Group Policy or PowerShell: Set-MpPreference -DisableRealtimeMonitoring $true -MAPSReporting 0. To re-enable, set: Set-MpPreference -DisableRealtimeMonitoring $false -MAPSReporting 2.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
