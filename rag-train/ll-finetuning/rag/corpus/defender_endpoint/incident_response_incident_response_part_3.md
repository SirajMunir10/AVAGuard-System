# Incident Response: Incident Response

**Domain:** Defender for Endpoint
**Subdomain:** Incident Response
**Incident Type:** Incident Response

## Scenario / Query
A security operations analyst receives an alert in Microsoft 365 Defender for a suspicious PowerShell command executed on a device. The analyst needs to contain the compromised device, collect the relevant evidence, and investigate the scope of the incident using Microsoft Defender for Endpoint's incident response capabilities. What are the recommended steps and tools to perform this response?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Microsoft Defender for Endpoint Plan 2
- **Configuration:** Device isolation and automated investigation enabled; Microsoft 365 Defender portal accessible with appropriate RBAC roles (e.g., Security Operator, Security Administrator)

## Symptoms
- Alert triggered for suspicious PowerShell command execution
- Device reported as compromised in Microsoft 365 Defender
- Potential lateral movement or data exfiltration suspected

## Error Codes
N/A

## Root Causes
1. Malicious PowerShell script executed on the device
2. Insufficient endpoint detection and response controls prior to incident

## Remediation Steps
1. 1. In Microsoft 365 Defender, navigate to Incidents & alerts > Incidents and select the relevant incident.
2. 2. Use the 'Isolate device' action to contain the compromised device from the network while allowing communication with Microsoft Defender for Endpoint services.
3. 3. Initiate an automated investigation from the incident page to allow Defender for Endpoint to automatically remediate identified threats.
4. 4. Collect forensic evidence by using the 'Collect investigation package' action on the device.
5. 5. Review the device timeline and alert evidence to identify the initial access vector and scope of compromise.
6. 6. If needed, run a Live Response session to execute additional commands for deeper investigation (e.g., get file, run script).
7. 7. After analysis, remediate by removing malicious files, registry keys, and scheduled tasks as identified, then unisolate the device.

## Validation
Confirm that the device is no longer showing active alerts, that the automated investigation completed with a status of 'No threats found' or 'Remediated', and that the device can communicate normally after unisolation.

## Rollback
If isolation was applied incorrectly, use the 'Release from isolation' action in the device actions menu. If automated remediation removed legitimate files, restore from backup or reimage the device.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/incident-response?view=o365-worldwide>
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/respond-machine-alerts?view=o365-worldwide>
