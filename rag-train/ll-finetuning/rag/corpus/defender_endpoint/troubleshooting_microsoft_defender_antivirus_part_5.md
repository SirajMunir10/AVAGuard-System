# Troubleshooting: Microsoft Defender Antivirus (Error Code: Error code Result code associated with threat status. Standard HRESULT values.)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Microsoft Defender Antivirus engine update failure (Event ID 2003)?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- The antimalware engine update failed
- Event ID 2003 with symbolic name MALWAREPROTECTION_ENGINE_UPDATE_FAILED

## Error Codes
- `Error Code: Error code Result code associated with threat status. Standard HRESULT values.`

## Root Causes
1. Interruption in network connectivity during an update

## Remediation Steps
1. Update definitions and force a rescan directly on the endpoint
2. Contact Microsoft Technical Support

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
