# Implementation: Alert Tuning

**Domain:** Defender for Endpoint
**Subdomain:** Alert Tuning
**Incident Type:** Implementation

## Scenario / Query
How to create a tuning rule to suppress or resolve alerts based on specific triggers like file creation in Microsoft Defender XDR?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** Alert tuning rules with conditions and actions

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. In the Conditions area, add a condition for the alert's triggers. For example, if you want to prevent an alert from being triggered when a specific file is created, define a condition for the File:Custom trigger, and define the file details.
2. To set multiple rule conditions, select Add filter and use AND, OR, and grouping options to define the relationships between the multiple evidence types that trigger the alert.
3. In the Action area of the Tune alert pane, select the relevant action you want the rule to take. Choose from Hide alert, Resolve alert, or Set as behavior.

## Validation
1. Navigate to Microsoft Defender XDR > Incidents & alerts > Alerts. 2. Locate an alert that matches the tuning rule conditions (e.g., file creation trigger). 3. Verify the alert is no longer displayed (if action is 'Hide alert') or shows status 'Resolved' (if action is 'Resolve alert') or is categorized under 'Behavior' (if action is 'Set as behavior'). 4. Confirm the rule appears in the tuning rules list: go to Settings > Endpoints > Rules > Alert tuning. 5. Run a test that would normally trigger the alert (e.g., create the specified file) and confirm no new alert is generated for that condition.

## Rollback
1. Navigate to Microsoft Defender XDR > Settings > Endpoints > Rules > Alert tuning. 2. Locate the tuning rule you created. 3. Select the rule and choose 'Delete rule' or 'Disable rule' to revert its effect. 4. Confirm the rule is removed or disabled. 5. Verify that alerts for the previously suppressed condition are now generated as expected by triggering the condition (e.g., creating the specified file) and checking the Alerts queue.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts>
