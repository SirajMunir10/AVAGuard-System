# Troubleshooting: Microsoft Defender Antivirus (3002)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Event ID 3002 indicating real-time protection failure in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Real-time protection encountered an error and failed
- Event ID 3002 with symbolic name MALWAREPROTECTION_RTP_FEATURE_FAILURE

## Error Codes
- `3002`

## Root Causes
1. One of the services failed to start

## Remediation Steps
1. Restart the system
2. Run a full scan

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
