# Incident Response: Incident Response

**Domain:** Defender for Endpoint
**Subdomain:** Incident Response
**Incident Type:** Incident Response

## Scenario / Query
How do I investigate and remediate a confirmed malware incident on a single device using Microsoft Defender for Endpoint, including isolating the device and running a full antivirus scan?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Defender for Endpoint Plan 2
- **Configuration:** Device isolation and full scan actions enabled in Microsoft 365 Defender portal

## Symptoms
- Alert generated for 'Malware detected' on a specific device
- Device appears in the 'Devices' list with an active alert
- Incident page shows the device as 'At risk'

## Error Codes
N/A

## Root Causes
1. Malicious file executed on the device
2. Antivirus definitions may be outdated or real-time protection was disabled

## Remediation Steps
1. 1. In the Microsoft 365 Defender portal (https://security.microsoft.com), navigate to Incidents & alerts > Incidents and select the relevant incident.
2. 2. On the incident page, review the alert details and identify the affected device.
3. 3. From the device page, select 'Isolate device' to disconnect it from the network while allowing communication with Defender for Endpoint services.
4. 4. After isolation, run a full antivirus scan by selecting 'Run antivirus scan' > 'Full scan' from the device actions menu.
5. 5. Review scan results and take further action (e.g., remove or quarantine detected threats) as recommended by Defender for Endpoint.
6. 6. Once the threat is remediated, select 'Release from isolation' to restore network connectivity.

## Validation
Confirm that the device no longer shows active alerts and that the incident is resolved in the Microsoft 365 Defender portal.

## Rollback
If isolation was applied incorrectly, release the device from isolation immediately via the same device actions menu.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-to-incidents>
