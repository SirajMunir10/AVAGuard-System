# Troubleshooting: Microsoft Defender Antivirus (2011)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to handle excessive Event ID 2011 (MALWAREPROTECTION_SIGNATURE_FASTPATH_DELETED) events flooding a SIEM server?

## Environment Context
- **Tenant Type:** Any
- **Configuration:** Platform version 4.18.2207.7 or later; registry key HKLM\SOFTWARE\Microsoft\Windows Defender\Reporting\EnableDynamicSignatureDroppedEventReporting

## Symptoms
- Hundreds of Event ID 2011 events reported simultaneously
- SIEM server becomes flooded with 2011 events

## Error Codes
- `2011`
- `MALWAREPROTECTION_SIGNATURE_FASTPATH_DELETED`

## Root Causes
1. When a new signature is delivered to Defender for Endpoint, sometimes hundreds of dynamic signatures expire at the same time, resulting in hundreds of 2011 events reported.

## Remediation Steps
1. No action is necessary. The Microsoft Defender Antivirus client is in a healthy state.
2. Beginning with platform version 4.18.2207.7, by default, Defender for Endpoint doesn't report 2011 events. This default behavior is controlled by the registry entry: HKLM\SOFTWARE\Microsoft\Windows Defender\Reporting\EnableDynamicSignatureDroppedEventReporting. The default value is false, which means 2011 events aren't reported. If it's set to true, 2011 events are reported.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
