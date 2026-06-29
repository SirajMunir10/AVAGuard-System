# Implementation: Analytics Rules

**Domain:** Sentinel
**Subdomain:** Analytics Rules
**Incident Type:** Implementation

## Scenario / Query
How do I configure a custom analytics rule to generate a unique alert for each event returned by a query in Microsoft Sentinel?

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
1. In the rule creation wizard, under 'Alert enrichment', select 'Trigger an alert for each event'.
2. Define grouping parameters (e.g., by user, hostname) in the query itself.

## Validation
1. Navigate to Microsoft Sentinel > Analytics > Active rules. 2. Locate the custom rule and select it. 3. In the rule details pane, confirm that 'Alert enrichment' shows 'Trigger an alert for each event' is enabled. 4. Review the rule query to verify that grouping parameters (e.g., | summarize by user, hostname) are correctly defined. 5. Trigger a test event that matches the query and confirm that a unique alert is generated for each event in the Sentinel incidents blade.

## Rollback
1. In Microsoft Sentinel > Analytics > Active rules, select the custom rule. 2. Click 'Edit' to open the rule creation wizard. 3. Under 'Alert enrichment', change the setting from 'Trigger an alert for each event' to 'Trigger an alert for each query result' (or the default grouping option). 4. Remove any grouping parameters (e.g., | summarize by user, hostname) from the query if they were added. 5. Review and save the rule. 6. Verify that alerts are now generated per query result as before.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-custom>
