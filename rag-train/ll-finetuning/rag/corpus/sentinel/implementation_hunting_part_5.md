# Implementation: Hunting

**Domain:** Sentinel
**Subdomain:** Hunting
**Incident Type:** Implementation

## Scenario / Query
How to create a custom detection rule from a hunting query in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. View the query's results.
2. Select New alert rule > Create Microsoft Sentinel alert.
3. Use the Analytics rule wizard to create a new rule based on your query.

## Validation
1. In the Microsoft Sentinel workspace, navigate to Analytics > Rule templates. Confirm the new custom detection rule appears in the list. 2. Select the rule and verify its query matches the original hunting query. 3. Use the 'Test with current data' option (or run a manual query in Log Analytics) to ensure the rule returns expected results. 4. Check the rule's status is 'Enabled' and its frequency/alert settings match the intended configuration.

## Rollback
1. In the Microsoft Sentinel workspace, go to Analytics > Active rules. 2. Locate the newly created custom detection rule. 3. Select the rule and choose 'Disable' to stop it from generating alerts. 4. If needed, delete the rule entirely by selecting 'Delete' and confirming. 5. Verify the rule no longer appears in the active rules list and that no alerts are generated from it.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/hunting>
- <https://learn.microsoft.com/en-us/azure/sentinel/create-custom-analytics-rules>
