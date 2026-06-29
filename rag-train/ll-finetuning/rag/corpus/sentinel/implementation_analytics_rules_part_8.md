# Implementation: Analytics Rules

**Domain:** Sentinel
**Subdomain:** Analytics Rules
**Incident Type:** Implementation

## Scenario / Query
How do I configure the query scheduling and alert threshold for a custom detection rule in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace with Analytics rule creation enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Set the following parameters in the Query scheduling section: Run query every Controls the query interval: how often the query runs. Allowed range: 5 minutes to 14 days.
2. Lookup data from the last Determines the lookback period: the time period covered by the query. Allowed range: 5 minutes to 14 days. Must be longer than or equal to the query interval.
3. Start running Automatically: The rule runs for the first time immediately upon being created, and after that at the query interval.
4. At specific time (Preview): Set a date and time for the rule to first run, after which it runs at the query interval. Allowed range: 10 minutes to 30 days after the rule creation (or enablement) time.
5. Set the threshold for creating alerts. Use the Alert threshold section to define the sensitivity level of the rule. For example, set a minimum threshold of 100: Generate alert when number of query results Is greater than Number of events 100. If you don't want to set a threshold, enter 0 in the number field.
6. Under Event grouping, choose one of two ways to handle the grouping of events into alerts: Group all events into a single alert (default) or Trigger an alert for each event.

## Validation
1. In the Microsoft Sentinel workspace, navigate to Analytics > Active rules and select the custom rule. 2. Confirm 'Run query every' is set to the desired interval (e.g., 5 minutes). 3. Confirm 'Lookup data from the last' is set to a period equal to or longer than the query interval (e.g., 5 minutes). 4. Verify 'Start running' is set to 'Automatically' or a specific time within the allowed range. 5. In 'Alert threshold', confirm 'Generate alert when number of query results' is set to 'Is greater than' and the number matches the intended threshold (e.g., 100). 6. Check 'Event grouping' is set to either 'Group all events into a single alert' or 'Trigger an alert for each event' as desired. 7. Run the rule manually or wait for the next scheduled run and verify alerts are generated as expected.

## Rollback
1. Navigate to Analytics > Active rules and select the custom rule. 2. Click 'Edit' to open the rule wizard. 3. In the 'Query scheduling' section, revert 'Run query every' to the previous interval. 4. Revert 'Lookup data from the last' to the previous lookback period. 5. Revert 'Start running' to the previous setting. 6. In the 'Alert threshold' section, revert the threshold to the previous value (e.g., change from 100 to 0 if no threshold was set). 7. In 'Event grouping', revert to the previous grouping method. 8. Click 'Review and create' and then 'Save' to apply the rollback.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-custom>
