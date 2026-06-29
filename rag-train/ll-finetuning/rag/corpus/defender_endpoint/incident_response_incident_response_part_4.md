# Incident Response: Incident Response

**Domain:** Defender for Endpoint
**Subdomain:** Incident Response
**Incident Type:** Incident Response

## Scenario / Query
How do I manually initiate a live response session on a compromised device in Microsoft Defender for Endpoint to collect forensic evidence?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Defender for Endpoint Plan 2
- **Configuration:** Live response must be enabled in the Microsoft 365 Defender portal under Settings > Endpoints > Advanced features. The analyst must have the appropriate RBAC permissions (e.g., 'Live response capabilities' set to 'Full').

## Symptoms
- Suspicious process execution detected on a device
- Alert indicates active lateral movement from a specific endpoint
- Device is online and reachable in the Defender for Endpoint console

## Error Codes
N/A

## Root Causes
1. Incident requires immediate forensic collection to determine the scope of compromise
2. Automated investigation and response did not fully contain the threat

## Remediation Steps
1. Navigate to the Microsoft 365 Defender portal (https://security.microsoft.com).
2. Go to Incidents & alerts > Incidents and select the relevant incident.
3. From the Devices list, select the affected device and choose 'Initiate Live Response'.
4. In the Live Response session, use the 'GetFile' command to collect specific files (e.g., malicious scripts, memory dumps).
5. Use the 'RunScript' command to execute a pre-approved PowerShell script for artifact collection.
6. After collection, use the 'PutFile' command to upload analysis tools if needed.
7. When finished, select 'Disconnect' to end the session.

## Validation
Verify that the collected files are available in the 'Evidence and Response' tab of the incident and that the live response session log shows no errors.

## Rollback
No rollback needed for initiating a live response session; however, if a script was executed that caused unintended changes, restore the device from a known good backup or reimage the device.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/live-response>
