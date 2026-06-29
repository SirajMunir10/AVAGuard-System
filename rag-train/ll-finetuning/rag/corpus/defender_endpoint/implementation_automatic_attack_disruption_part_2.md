# Implementation: Automatic Attack Disruption

**Domain:** Defender for Endpoint
**Subdomain:** Automatic Attack Disruption
**Incident Type:** Implementation

## Scenario / Query
How does automatic attack disruption isolate a compromised device using Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Automatic attack disruption enabled; Defender for Endpoint onboarded devices

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Isolate device (Preview) - based on Microsoft Defender for Endpoint's capability, this action automatically isolates a compromised device from the network when the incident analysis indicates with high confidence that the device is being used as an active foothold.
2. Most network traffic is blocked while the device remains connected to required security services for investigation and remediation.
3. Isolation is time-limited and scoped only to devices involved in the incident.
4. Security operators can release isolation at any time after completing investigation.

## Validation
1. In Microsoft 365 Defender (https://security.microsoft.com), navigate to Incidents & alerts > Incidents. 2. Select an incident that was automatically disrupted. 3. In the incident details, under 'Devices', verify that the affected device shows a status of 'Isolated' and that the isolation source is listed as 'Automatic attack disruption'. 4. Confirm that the device is still able to communicate with required security services (e.g., Defender for Endpoint cloud) by checking the device's connectivity status in the device inventory. 5. Review the incident timeline to see the automatic isolation action recorded with a timestamp and the reason 'Automatic attack disruption'.

## Rollback
1. In Microsoft 365 Defender, go to Device inventory and locate the isolated device. 2. Select the device and choose 'Release from isolation' from the actions menu. 3. Confirm the release action. 4. Verify the device's network connectivity is restored by checking its status in the device inventory (should show 'Connected'). 5. If the device remains isolated, use the 'Run antivirus scan' action to ensure no active threats remain, then retry release. 6. If issues persist, contact Microsoft Support for further assistance.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption>
