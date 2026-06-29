# Incident Response: Incident Response

**Domain:** Defender for Endpoint
**Subdomain:** Incident Response
**Incident Type:** Incident Response

## Scenario / Query
A security analyst receives an alert in Microsoft Defender for Endpoint indicating that a device has been compromised by a known malware variant. How should the analyst initiate an automated investigation and response, and what are the steps to contain the device using the built-in containment action?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Defender for Endpoint Plan 2
- **Configuration:** Automated investigation and response (AIR) enabled; device group with 'Contain device' action permitted

## Symptoms
- High-severity alert triggered for malware detection on a device
- Alert details show file hash and process tree associated with known malware
- Device is currently online and communicating with the network

## Error Codes
N/A

## Root Causes
1. Malware executed on the device due to user action or exploit
2. No prior containment action applied automatically

## Remediation Steps
1. From the Microsoft 365 Defender portal (https://security.microsoft.com), navigate to Incidents & alerts > Incidents and select the relevant incident.
2. Review the incident graph and evidence to confirm the compromised device.
3. On the device page, under 'Actions', select 'Contain device' to isolate the device from the network while allowing communication with Defender for Endpoint services.
4. Initiate an automated investigation by clicking 'Start investigation' on the alert or device page, which will run playbooks to analyze and remediate the threat.
5. After containment and investigation, apply remediation steps such as removing the detected file or running a full antivirus scan as recommended by the investigation results.

## Validation
Confirm that the device status shows 'Contained' in the device inventory and that the automated investigation completes with a status of 'Remediated' or 'Partially remediated'.

## Rollback
To release containment, navigate to the device page, select 'Actions', and choose 'Release from containment'. The device will regain network access after a few minutes.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/automated-investigations?view=o365-worldwide>
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/respond-machine-alerts?view=o365-worldwide>
