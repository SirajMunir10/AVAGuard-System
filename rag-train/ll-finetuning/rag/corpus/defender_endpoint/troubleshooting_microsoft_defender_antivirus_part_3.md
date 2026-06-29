# Troubleshooting: Microsoft Defender Antivirus (1116)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to interpret threat remediation actions and event IDs in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Threat detected but not remediated
- Protection History entries continue to generate
- Alerts continue to generate

## Error Codes
- `1116`
- `1117`

## Root Causes
1. ThreatSeverityDefaultAction set to None
2. Non-remediating threat actions configured (Allow, No action, None)

## Remediation Steps
1. Use standard remediation actions (Clean, Quarantine, or Remove) in all other environments
2. Configure ThreatSeverityDefaultAction to a remediating action

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
