# Hardening: Endpoint Detection and Response

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint Detection and Response
**Incident Type:** Hardening

## Scenario / Query
How does GPO hardening work as part of predictive shielding in Defender for Endpoint, and what are the steps to apply and manage this action?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Predictive shielding (Preview) feature enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Defender for Endpoint automatically applies the GPO hardening action as part of the predictive shielding feature.
2. Group Policy Object (GPO) hardening temporarily stops new GPO policies from being applied to devices identified as high risk.
3. To enrich predictive shielding actions, use the Microsoft Defender for Identity sensor in your environment.
4. After the action is applied, view the action impact in the incident graph, track the actions in the Action center, and investigate further using advanced hunting.

## Validation
1. Navigate to Microsoft 365 Defender portal (https://security.microsoft.com) > Incidents & alerts > Incidents. Select the relevant incident and review the incident graph to confirm the 'GPO hardening' action is listed under 'Actions taken'. 2. Go to Action center (https://security.microsoft.com/action-center) and filter by 'GPO hardening' to verify the action status shows as 'Completed' or 'In progress'. 3. Run an advanced hunting query: `DeviceEvents | where ActionType == 'GpoHardeningApplied' | where Timestamp > ago(1h)` to confirm the action was applied to the targeted device.

## Rollback
1. In the Microsoft 365 Defender portal, navigate to Action center and locate the 'GPO hardening' action. If the action is still pending, select 'Cancel' to abort. 2. If the action has already been applied, contact Microsoft Support to request manual removal of the GPO hardening policy from the affected device. 3. Alternatively, use Group Policy Management Console (GPMC) on the affected device to remove any temporary GPOs applied by Defender for Endpoint, ensuring no new GPOs are blocked. 4. Monitor the device in the incident graph and Action center to confirm the rollback is reflected.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
