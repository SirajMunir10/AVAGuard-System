# Hardening: Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Defender for Endpoint
**Incident Type:** Hardening

## Scenario / Query
How to contain IP addresses of undiscovered or non-onboarded devices in Defender for Endpoint to prevent attack spread?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Contain IP policy; onboarded devices: Windows 10, Windows 11, Windows 2012 R2, Windows 2016

## Symptoms
- Attackers spreading from compromised devices to other noncompromised devices via IP addresses of undiscovered or non-onboarded devices

## Error Codes
N/A

## Root Causes
1. IP addresses associated with undiscovered devices or devices not onboarded to Defender for Endpoint are not automatically blocked

## Remediation Steps
1. Contain IP addresses automatically through automatic attack disruption using the Contain IP policy
2. The Contain IP policy automatically blocks a malicious IP address when Defender for Endpoint detects the IP address to be associated with an undiscovered device or a device not onboarded
3. After containment, view the action in the History view of the Action Center to see when the action occurred and identify the contained IP addresses
4. If a contained IP address is part of an incident, an indicator is present on the incident graph and on the incident's evidence and response tab

## Validation
A message indicating that the action is applied appears on the applicable incident, device, or IP page

## Rollback
To stop containment, select the Contain IP action in the Action Center, then in the flyout select Undo. This action restores the IP address' connection to the network.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
