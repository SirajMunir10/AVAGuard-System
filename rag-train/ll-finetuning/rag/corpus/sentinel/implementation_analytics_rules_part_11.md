# Implementation: Analytics Rules

**Domain:** Sentinel
**Subdomain:** Analytics Rules
**Incident Type:** Implementation

## Scenario / Query
How do I simulate the results of a custom analytics rule query in Microsoft Sentinel before finalizing the rule?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel Analytics Rule

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. In the 'Results simulation' area, select 'Test with current data'.
2. Microsoft Sentinel simulates running the rule 50 times on current data using the defined schedule.
3. Review the graph showing the number of results over the time period defined in 'Query scheduling'.
4. If the query is modified, select 'Test with current data' again to update the graph.

## Validation
1. In Microsoft Sentinel, navigate to Analytics > Rule templates. Select the custom analytics rule you created. 2. In the rule details pane, click 'Edit'. 3. In the 'Results simulation' area, click 'Test with current data'. 4. Wait for the simulation to complete. 5. Verify that the graph displays results over the time period defined in 'Query scheduling'. 6. If the graph shows expected results (e.g., alerts or events matching your query), the rule is functioning correctly. 7. Optionally, modify the query and click 'Test with current data' again to confirm updated results.

## Rollback
1. If the simulation reveals unexpected results (e.g., no results or excessive false positives), do not enable the rule. 2. Edit the analytics rule and adjust the query or scheduling settings as needed. 3. Re-run 'Test with current data' to validate changes. 4. If the rule was already enabled, disable it by navigating to Active rules, selecting the rule, and clicking 'Disable'. 5. If necessary, delete the rule entirely by selecting it and clicking 'Delete'. 6. Revert to a previous known-good rule version if available via the rule's version history (if supported).

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-custom>
