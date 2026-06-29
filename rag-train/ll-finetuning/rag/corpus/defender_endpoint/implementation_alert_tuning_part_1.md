# Implementation: Alert Tuning

**Domain:** Defender for Endpoint
**Subdomain:** Alert Tuning
**Incident Type:** Implementation

## Scenario / Query
How to create alert tuning rules in Microsoft Defender XDR to suppress alerts based on specific conditions?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** Alert tuning settings

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. In the Microsoft Defender portal, select Settings > Microsoft Defender XDR > Alert tuning.
2. Select Add new rule to tune a new alert, or select an existing rule row to make changes.
3. Selecting the rule title opens a rule details page, where you can view a list of associated alerts, edit conditions, or turn the rule on and off.
4. In the Tune alert pane, under Select service sources, select the service sources where you want the rule to apply. Only services where you have permissions are shown in the list.
5. In the Conditions area, add a condition for the alert's triggers. For example, if you want to prevent an alert from being triggered when a specific file is created, define a condition for the File:Custom trigger, and define the file details.
6. Listed triggers differ, depending on the service sources you selected. Triggers are all indicators of compromise (IOCs), such as files, processes, scheduled tasks, and other evidence types that might trigger an alert, including AntiMalware Scan Interface (AMSI) scripts, Windows Management Instrumentation (WMI) events, or scheduled tasks.
7. To set multiple rule conditions, select Add filter and use AND, OR, and grouping options to define the relationships between the multiple evidence types that trigger the alert. Further evidence properties are automatically populated as a new subgroup, where you can define your condition values. Condition values aren't case sensitive, and some properties support wildcards.

## Validation
1. In the Microsoft Defender portal, navigate to Settings > Microsoft Defender XDR > Alert tuning. 2. Locate the newly created or modified rule in the list. 3. Select the rule title to open the rule details page. 4. Verify that the rule status is set to 'On'. 5. Confirm that the service sources and conditions match the intended configuration. 6. Review the 'Associated alerts' section to ensure no alerts matching the rule's conditions are being generated.

## Rollback
1. In the Microsoft Defender portal, go to Settings > Microsoft Defender XDR > Alert tuning. 2. Select the rule you want to roll back. 3. To disable the rule without deleting it, toggle the rule status to 'Off'. 4. To completely remove the rule, select 'Delete rule' and confirm the deletion. 5. If you need to restore a previous configuration, re-create the rule with the original conditions or re-enable a previously disabled rule.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts>
