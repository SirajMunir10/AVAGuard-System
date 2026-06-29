# Implementation: Automatic Attack Disruption

**Domain:** Defender for Endpoint
**Subdomain:** Automatic Attack Disruption
**Incident Type:** Implementation

## Scenario / Query
How does automatic attack disruption contain a suspicious device using Microsoft Defender for Endpoint?

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
1. Device contain - based on Microsoft Defender for Endpoint's capability, this action is an automatic containment of a suspicious device to block any incoming/outgoing communication with the said device.
2. In addition, Defender for Endpoint automatically contains malicious IP addresses associated with undiscovered/not onboarded devices to block any lateral movement and encryption activity to other Defender for Endpoint-onboarded/discovered devices. It does this through its Contain IP (Preview) policy.
3. Moreover, compromised critical assets' IP addresses are also automatically contained with specific blocking mechanisms to stop the spread of an attack while avoiding productivity loss.

## Validation
1. In Microsoft 365 Defender (https://security.microsoft.com), navigate to Incidents & alerts > Incidents. Select the incident that triggered the automatic attack disruption. Verify that the 'Attack story' tab shows a 'Contain device' action for the suspicious device, with status 'Completed' or 'Succeeded'. 2. In the same incident, under the 'Devices' tab, confirm the suspicious device is listed with containment status 'Contained'. 3. For IP containment, in the incident's 'Attack story', look for 'Contain IP' actions. Verify that the associated IP addresses are listed with status 'Contained'. 4. Optionally, from the device's page (go to Assets > Devices, select the contained device), confirm the 'Containment status' field shows 'Contained' and that the device's communication is blocked.

## Rollback
1. In Microsoft 365 Defender, navigate to Assets > Devices. Search for the contained device. Select the device, then click 'Release from containment' in the action bar. Confirm the release. 2. For contained IP addresses, navigate to Settings > Endpoints > Rules > Contain IP (Preview). Locate the containment rule or action for the specific IP. Select the IP and choose 'Release' or 'Remove containment'. 3. If the containment was part of an automatic disruption that caused unintended impact, consider adjusting the automatic attack disruption settings: go to Settings > Endpoints > Advanced features, and toggle 'Automatic attack disruption' off, then back on after resolving the issue. 4. Monitor the device and network for any residual blocking by checking the device's communication status in the device timeline.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption>
