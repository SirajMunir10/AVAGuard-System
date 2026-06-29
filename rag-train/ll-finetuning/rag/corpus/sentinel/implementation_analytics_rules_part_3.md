# Implementation: Analytics Rules

**Domain:** Sentinel
**Subdomain:** Analytics Rules
**Incident Type:** Implementation

## Scenario / Query
How do I design and build a KQL query for a custom scheduled analytics rule in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Log Analytics workspace with Microsoft Sentinel enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Determine a data source, or a set of data sources, that you want to search to detect unusual or suspicious activity.
2. Find the name of the Log Analytics table into which data from those sources is ingested. You can find the table name on the page of the data connector for that source.
3. Use this table name (or a function based on it) as the basis for your query.
4. Decide what kind of analysis you want this query to perform on the table. This decision determines which commands and functions you should use in the query.
5. Decide which data elements (fields, columns) you want from the query results. This decision determines how you structure the output of the query.
6. Make sure that your query returns the TimeGenerated column, as scheduled analytics rules use it as the reference for the lookback period. This means that the rule only evaluates records where the TimeGenerated value falls within the specified lookback window.
7. Build and test your queries in the Logs screen. When you're satisfied, save the query for use in your rule.

## Validation
1. Navigate to the Log Analytics workspace in the Azure portal and open the Logs blade. 2. Run the KQL query you designed for the scheduled analytics rule. 3. Verify that the query returns results that include the TimeGenerated column and that the results fall within the expected lookback period. 4. Confirm that the query output contains the fields you intended to analyze. 5. In Microsoft Sentinel, go to Analytics > Scheduled query rules and create a new rule using your saved query. 6. Set the rule to run and observe that it triggers alerts as expected based on the query results.

## Rollback
1. If the custom scheduled analytics rule is causing issues (e.g., false positives, performance degradation), disable or delete the rule in Microsoft Sentinel under Analytics > Scheduled query rules. 2. If the query itself is problematic, revert to the previous version of the query by editing the rule and replacing the query with a known working version. 3. If the data source or table reference is incorrect, update the rule to use the correct table name or function as documented in the data connector page. 4. If the rule is not triggering alerts, review the query logic and ensure the TimeGenerated column is included and the lookback period is correctly configured.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-custom>
