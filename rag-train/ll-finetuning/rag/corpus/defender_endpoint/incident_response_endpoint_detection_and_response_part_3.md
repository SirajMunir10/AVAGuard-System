# Incident Response: Endpoint Detection and Response

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint Detection and Response
**Incident Type:** Incident Response

## Scenario / Query
How to perform automatic device isolation in Microsoft Defender for Endpoint, including safeguards and business impact considerations?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Automatic device isolation policy

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Scoped action: Isolation targets specific devices involved in the incident rather than broadly across the environment.
2. Time-limited isolation: Isolation is automatically undone after a defined time window. You can also release isolation earlier after completing investigation and remediation.
3. Customer control: Security operators can review the incident context and take follow-up actions, including releasing isolation when it's safe to do so.

## Validation
1. Confirm that the automatic device isolation policy is enabled by navigating to Microsoft 365 Defender > Settings > Endpoints > Advanced features > Automatic device isolation and verifying it is set to 'On'.
2. Simulate an incident by triggering a test alert on a target device (e.g., via a controlled malware simulation).
3. In Microsoft 365 Defender, go to Incidents & alerts > Incidents, select the test incident, and verify the device appears with an 'Isolated' status under the 'Devices' tab.
4. Check that the isolation action is scoped only to the target device and not applied to other devices in the environment.
5. Confirm the isolation duration by reviewing the action details in the Action center; ensure it matches the defined time window.
6. Attempt to release isolation early by selecting the device and choosing 'Release from isolation' from the actions menu, verifying the device returns to a normal state.

## Rollback
1. If automatic isolation causes unintended business impact (e.g., blocking critical systems), immediately release the isolated device(s) by navigating to Microsoft 365 Defender > Action center > Device isolation, selecting the affected device, and clicking 'Release from isolation'.
2. Disable the automatic device isolation policy by going to Settings > Endpoints > Advanced features > Automatic device isolation and setting it to 'Off'.
3. Manually review and release any other devices that were automatically isolated during the incident by checking the Action center for pending or completed isolation actions.
4. If the isolation policy was triggered incorrectly due to a false positive, investigate the alert rule or detection logic that caused the action and adjust as needed (e.g., modify alert suppression rules).
5. Document the incident and the rollback steps taken for future reference and to refine the automatic isolation policy.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
