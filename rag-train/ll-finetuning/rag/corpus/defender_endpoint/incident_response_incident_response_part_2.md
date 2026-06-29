# Incident Response: Incident Response

**Domain:** Defender for Endpoint
**Subdomain:** Incident Response
**Incident Type:** Incident Response

## Scenario / Query
A security analyst receives a high-severity alert in Microsoft Defender for Endpoint indicating that a device has been compromised with a known malware variant. The analyst needs to isolate the device from the network to prevent lateral movement while allowing forensic investigation. What are the documented steps to isolate a device using Microsoft Defender for Endpoint, and what are the implications for the device's connectivity?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Defender for Endpoint Plan 2
- **Configuration:** Device isolation feature enabled; devices running Windows 10/11 and Windows Server 2019/2022

## Symptoms
- High-severity alert triggered for malware detection on a specific device
- Potential lateral movement risk from the compromised device

## Error Codes
N/A

## Root Causes
1. Malware infection detected on endpoint
2. Need to contain the threat while preserving forensic evidence

## Remediation Steps
1. 1. In Microsoft 365 Defender portal (https://security.microsoft.com), navigate to 'Incidents & alerts' > 'Incidents' and select the relevant incident.
2. 2. From the incident page, select the affected device under 'Devices' or go directly to 'Device inventory' and locate the device.
3. 3. On the device page, select 'Actions' > 'Isolate device'.
4. 4. In the isolation pane, choose 'Select isolation type': 'Full isolation' (blocks all network traffic except Defender for Endpoint services) or 'Selective isolation' (allows certain approved services).
5. 5. Provide a comment for the action and select 'Confirm'.
6. 6. Monitor the action progress in the 'Action center' (https://security.microsoft.com/action-center).
7. 7. After investigation, release the device by selecting 'Actions' > 'Release from isolation' on the device page.

## Validation
After isolation, verify the device status shows 'Isolated' in the device inventory. Confirm that network connectivity to other devices is blocked but the device can still communicate with Defender for Endpoint services (e.g., check that alerts and telemetry continue to be received).

## Rollback
To release the device from isolation, navigate to the device page in Microsoft 365 Defender, select 'Actions' > 'Release from isolation', provide a comment, and confirm. The device will regain normal network connectivity within a few minutes.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
