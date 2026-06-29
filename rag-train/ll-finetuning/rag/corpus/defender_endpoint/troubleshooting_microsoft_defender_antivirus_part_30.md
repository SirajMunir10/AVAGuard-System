# Troubleshooting: Microsoft Defender Antivirus (1120)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to interpret Event ID 1120 (MALWAREPROTECTION_THREAT_HASH) in Microsoft Defender Antivirus logs?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** ThreatFileHashLogging unsigned

## Symptoms
- Event ID 1120 logged with MALWAREPROTECTION_THREAT_HASH

## Error Codes
- `1120`

## Root Causes
1. Microsoft Defender Antivirus deduced the hashes for a threat resource

## Remediation Steps
N/A

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational.
3. Verify that Event ID 1120 is present with source 'MALWAREPROTECTION_THREAT_HASH'.
4. Confirm the event details include a 'Threat Resource Hash' field with a valid SHA1 or SHA256 hash value.
5. If ThreatFileHashLogging is set to 'unsigned', ensure the hash is logged for unsigned threats only.
6. Run 'Get-MpThreatDetection' in PowerShell to cross-reference the threat detection and its hash.

## Rollback
1. If Event ID 1120 is missing or incorrect, reset the ThreatFileHashLogging policy to its default value by running: Set-MpPreference -ThreatFileHashLogging 'unsigned' (or remove the custom policy setting).
2. Restart the Microsoft Defender Antivirus service: 'net stop WinDefend' then 'net start WinDefend'.
3. Re-run the detection test to verify Event ID 1120 reappears correctly.
4. If issues persist, restore the original Group Policy or registry value for ThreatFileHashLogging from backup.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
