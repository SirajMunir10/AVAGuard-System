# Incident Response: Incident Response

**Domain:** Defender XDR
**Subdomain:** Incident Response
**Incident Type:** Incident Response

## Scenario / Query
How do I investigate and remediate a ransomware incident detected by Microsoft Defender XDR, including isolating affected devices and blocking indicators of compromise?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Defender for Endpoint Plan 2
- **Configuration:** Device isolation enabled via Microsoft Defender for Endpoint; automated investigation and response (AIR) enabled

## Symptoms
- Multiple devices showing 'Ransomware' alert in Microsoft 365 Defender portal
- Files encrypted with .locked extension on endpoints
- Ransom note dropped on affected systems
- Suspicious network connections to known malicious IP addresses

## Error Codes
N/A

## Root Causes
1. User opened a malicious email attachment containing ransomware payload
2. Unpatched vulnerability exploited to deploy ransomware

## Remediation Steps
1. Isolate affected devices using Microsoft Defender for Endpoint: In the Microsoft 365 Defender portal, go to Assets > Devices, select the affected device, and choose 'Isolate device'.
2. Block indicators of compromise (IOCs) such as file hashes, IP addresses, and domains using Threat Analytics or custom indicator rules in Microsoft Defender for Endpoint.
3. Run a full antivirus scan on isolated devices using Microsoft Defender Antivirus.
4. Initiate automated investigation and response (AIR) to automatically contain and remediate the incident.
5. Restore encrypted files from backup if available; if not, use Microsoft's documented recovery guidance for ransomware.

## Validation
Confirm that affected devices are isolated and no longer communicating with command-and-control servers; verify that blocked IOCs are no longer detected in the environment.

## Rollback
If isolation was applied incorrectly, unisolate the device via the Microsoft 365 Defender portal by selecting the device and choosing 'Unisolate device'.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/incident-response-ransomware>
