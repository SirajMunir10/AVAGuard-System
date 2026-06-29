# Hardening: Endpoint Detection and Response

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint Detection and Response
**Incident Type:** Hardening

## Scenario / Query
How to apply Safeboot hardening as part of predictive shielding in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Predictive shielding feature enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Defender for Endpoint automatically applies the Safeboot hardening action as part of the predictive shielding feature.
2. To enrich predictive shielding actions, use the Microsoft Defender for Identity sensor in your environment.
3. After the action is applied, view the action impact in the incident graph.
4. Track the actions in the Action center.
5. Investigate further using advanced hunting.
6. View the current status of the Safeboot hardening action and other actions in the Activities tab (Preview).

## Validation
1. Confirm the Safeboot hardening action was applied by navigating to the Microsoft 365 Defender portal (https://security.microsoft.com) > Incidents & alerts > Incidents. Select the relevant incident and review the incident graph for the Safeboot action. 2. Go to Action center (https://security.microsoft.com/action-center) and verify the Safeboot hardening action is listed with a status of 'Completed' or 'In progress'. 3. Use advanced hunting with the following query in the Microsoft 365 Defender portal: DeviceEvents | where ActionType == 'SafebootHardening' | where Timestamp > ago(1h) | project Timestamp, DeviceName, ActionType, Status. 4. Check the Activities tab (Preview) for the device by navigating to Device inventory > select the device > Activities tab, and confirm the Safeboot hardening action is present with a status of 'Applied'.

## Rollback
1. If the Safeboot hardening action causes issues, manually remove the Safeboot state by restarting the device normally (without Safeboot). 2. To prevent automatic reapplication, disable predictive shielding for the affected device group by navigating to Microsoft 365 Defender portal > Settings > Endpoints > Advanced features > Predictive shielding and toggle off the feature for the relevant device group. 3. If the action was applied via a live response session, use the live response command 'restart' to reboot the device into normal mode. 4. Monitor the device and incident graph to ensure no further Safeboot actions are automatically applied.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
- <https://learn.microsoft.com/en-us/defender-endpoint/enrich-predictive-shielding>
- <https://learn.microsoft.com/en-us/defender-endpoint/manage-predictive-shielding-actions>
