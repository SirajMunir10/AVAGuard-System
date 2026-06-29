# Optimization: Threat Intelligence

**Domain:** Sentinel
**Subdomain:** Threat Intelligence
**Incident Type:** Optimization

## Scenario / Query
How to optimize threat intelligence feeds by extending the validity date on high value indicators using ingestion rules in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace with threat intelligence feeds enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select Ingestion rules to open a whole new page to view existing rules and construct new rule logic.
2. Enter a descriptive name for your rule.
3. Select the Object type. This use case is based on extending the Valid from property, which is only available for Indicator object types.
4. Add condition for Source Equals and select your high value Source.
5. Add condition for Confidence Greater than or equal and enter a Confidence score.
6. Select the Action. Since we want to modify this indicator, select Edit.
7. Select the Add action for Valid until, Extend by, and select a time span in days.
8. Consider adding a tag to indicate the high value placed on these indicators, like Extended. The modified date isn't updated by ingestion rules.
9. Select the Order you want the rule to run. Rules run from lowest order number to highest. Each rule evaluates every object ingested.
10. If the rule is ready to be enabled, toggle Status to on.
11. Select Add to create the ingestion rule.

## Validation
1. In the Microsoft Sentinel workspace, navigate to Threat Intelligence > Ingestion rules. 2. Confirm the newly created rule appears in the list with the expected name, status set to 'On', and the correct order number. 3. Ingest a test indicator that matches the rule conditions (e.g., source equals the high value source and confidence >= the specified score). 4. Verify that the ingested indicator's 'Valid until' property has been extended by the configured number of days and that the tag 'Extended' (if added) is present. 5. Check that the 'Modified date' of the indicator has not been updated. 6. Optionally, use the Threat Intelligence search or API to confirm the indicator's properties reflect the changes.

## Rollback
1. In the Microsoft Sentinel workspace, navigate to Threat Intelligence > Ingestion rules. 2. Locate the rule created for extending validity. 3. Toggle the Status to 'Off' to disable the rule. 4. If the rule must be removed entirely, select the rule and choose 'Delete' (or the delete option available). 5. For indicators already modified by the rule, manually update each indicator's 'Valid until' property back to its original value using the Threat Intelligence blade or API. 6. Remove the 'Extended' tag from affected indicators if it was added. 7. Verify that no new indicators are being modified by the disabled or deleted rule.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/work-with-threat-indicators>
