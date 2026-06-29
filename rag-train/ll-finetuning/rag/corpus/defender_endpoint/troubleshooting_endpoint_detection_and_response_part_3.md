# Troubleshooting: Endpoint Detection and Response

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint Detection and Response
**Incident Type:** Troubleshooting

## Scenario / Query
How to view automatic device isolation actions after they are applied in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Automatic device isolation enabled

## Symptoms
- Automatic isolation has been applied to a device
- Need to review the action and its status

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Open the relevant incident and review the Activities tab.
2. Open the affected device page and confirm the device isolation status.
3. Open Action center to review action history and current state.

## Validation
1. Navigate to the Microsoft 365 Defender portal (https://security.microsoft.com).
2. Go to Incidents & alerts > Incidents and open the relevant incident.
3. Select the Activities tab and verify that an 'Isolate device' action is listed with a status of 'Completed' or 'Pending'.
4. Go to the device page for the affected device (e.g., from the incident or via Assets > Devices).
5. On the device timeline, confirm the 'Isolation status' is set to 'Isolated'.
6. Go to Action center (https://security.microsoft.com/action-center) and review the action history. Confirm the 'Isolate device' action shows a status of 'Completed' and the device is listed as isolated.

## Rollback
1. In the Microsoft 365 Defender portal, go to Action center (https://security.microsoft.com/action-center).
2. Locate the 'Isolate device' action for the affected device.
3. If the action is still pending, you can cancel it by selecting the action and choosing 'Cancel'.
4. If the action has already completed, initiate a 'Release from isolation' action:
   - Go to Assets > Devices, select the isolated device.
   - Click 'Actions' > 'Release from isolation'.
   - Provide a reason and confirm.
5. Monitor the Action center to ensure the release action completes successfully.
6. Verify on the device page that the 'Isolation status' changes back to 'Not isolated'.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
