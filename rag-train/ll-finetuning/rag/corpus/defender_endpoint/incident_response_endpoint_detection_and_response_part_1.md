# Incident Response: Endpoint Detection and Response

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint Detection and Response
**Incident Type:** Incident Response

## Scenario / Query
How do I initiate an automated investigation on a device from an alert in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Automated investigation enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Start a new, general-purpose automated investigation on the device if needed.
2. While an investigation is running, any other alert generated from the device is added to an ongoing automated investigation until that investigation completes.
3. If the same threat is seen on other devices, those devices are added to the investigation.

## Validation
1. Confirm that the automated investigation was initiated: In Microsoft 365 Defender, navigate to Incidents & alerts > Incidents. Select the relevant incident and verify that the 'Automated investigation' status shows 'Running' or 'Pending' for the device. 2. Check the device timeline: Go to Endpoints > Device inventory, select the device, and review the 'Timeline' tab for an entry indicating 'Automated investigation started'. 3. Use Advanced Hunting: Run the query `DeviceEvents | where ActionType == 'AutomatedInvestigationStarted' and DeviceName == '<device_name>'` to confirm the investigation start.

## Rollback
1. If the automated investigation was started in error, stop it: In Microsoft 365 Defender, go to Incidents & alerts > Incidents, select the incident, and under 'Automated investigations', find the running investigation and select 'Stop investigation'. 2. Alternatively, use the API: Send a POST request to `https://api.security.microsoft.com/api/machineactions/<machine_action_id>/cancel` with appropriate authentication to cancel the investigation action. 3. If the investigation already took actions (e.g., file quarantine), manually restore affected files from the Action center by selecting the action and choosing 'Undo'.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
