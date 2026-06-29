# Incident Response: Incident Response

**Domain:** Defender for Endpoint
**Subdomain:** Incident Response
**Incident Type:** Incident Response

## Scenario / Query
A security analyst receives a high-severity alert in Microsoft 365 Defender indicating that a device is communicating with a known malicious IP address. The analyst needs to isolate the device from the network while preserving forensic data, then run a full antivirus scan and collect an investigation package. What are the correct steps to perform device isolation, initiate a full scan, and collect the investigation package using Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Microsoft Defender for Endpoint Plan 2
- **Configuration:** Device isolation capability enabled and devices running supported Windows versions

## Symptoms
- High-severity alert triggered for device communicating with a known malicious IP address
- Device is potentially compromised and needs containment

## Error Codes
N/A

## Root Causes
1. Device is actively communicating with a known malicious IP address
2. Potential malware or unauthorized remote access on the device

## Remediation Steps
1. 1. In Microsoft 365 Defender portal (https://security.microsoft.com), go to Incidents & alerts > Incidents and select the relevant incident.
2. 2. From the incident page, select the device under investigation and choose 'Isolate device' from the actions menu. Select 'Selective isolation' to allow only a limited set of core services (e.g., Microsoft Update) while blocking all other network traffic.
3. 3. Confirm the isolation action and wait for the action to complete (status will show 'Isolation initiated').
4. 4. After isolation, initiate a full antivirus scan: on the same device action menu, select 'Run antivirus scan' and choose 'Full scan'.
5. 5. To collect forensic data, select 'Collect investigation package' from the device actions menu. This packages logs, registry, and other forensic artifacts.
6. 6. Review the collected package and scan results to determine next steps (e.g., threat removal, reimage).

## Validation
After isolation, the device should show 'Isolated' status in the device inventory. The full scan should complete with results visible in the device timeline. The investigation package should be available for download from the device page.

## Rollback
To release isolation, go to the device page and select 'Release from isolation'. This restores full network connectivity. Ensure the device is clean before releasing.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/respond-machine-alerts?view=o365-worldwide>
