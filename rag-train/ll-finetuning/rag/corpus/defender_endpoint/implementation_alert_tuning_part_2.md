# Implementation: Alert Tuning

**Domain:** Defender for Endpoint
**Subdomain:** Alert Tuning
**Incident Type:** Implementation

## Scenario / Query
How to tune an alert in the Microsoft Defender portal to suppress or resolve it based on specific conditions?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Alert tuning rule conditions

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. In the Microsoft Defender portal, go to the Alerts page or an alert details page.
2. If you're on the Alerts page, first select the alert you want to tune, and then select Tune alert. Depending on your screen resolution, you might need to select the ellipsis ( ... ) to see the Tune alert option.
3. The Tune alert pane opens on the side, where you can define conditions for the alert.
4. In the Alert types area, select to apply the alert tuning rule only to alerts of the selected type, or any alert type based on the same conditions. If you select Any alert type based on certain conditions, also select the service sources where you want the rule to apply. Only services where you have permissions are shown in the list.
5. To set multiple rule conditions, select Add filter and use AND, OR, and grouping options to define the relationships between the multiple evidence types that trigger the alert. Further evidence properties are automatically populated as a new subgroup, where you can define your condition values. Condition values aren't case sensitive, and some properties support wildcards.
6. In the Action area of the Tune alert pane, select the relevant action you want the rule to take. Choose from Hide alert, Resolve alert, or Set as behavior.
7. Enter a meaningful name for your alert and a comment to describe the alert, and then select Save.

## Validation
1. Navigate to the Microsoft Defender portal (https://security.microsoft.com).
2. Go to the Alerts page under Incidents & alerts.
3. Locate the alert that was tuned and verify its status shows 'Resolved' or 'Hidden' as per the action selected.
4. Alternatively, go to Settings > Endpoints > Alert tuning to confirm the new rule appears in the list with the correct name, conditions, and action.
5. Trigger the same alert conditions (if safely possible) and confirm that the alert is automatically suppressed or resolved according to the rule.

## Rollback
1. In the Microsoft Defender portal, go to Settings > Endpoints > Alert tuning.
2. Find the alert tuning rule you created.
3. Select the rule and choose 'Delete rule' to remove it.
4. Confirm deletion when prompted.
5. If the alert was already resolved or hidden, you may need to manually reopen it from the Alerts page by selecting the alert and choosing 'Manage alert' > 'Set status' to 'New' or 'In progress'.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts>
