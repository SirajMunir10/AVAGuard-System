# Implementation: Hunting

**Domain:** Sentinel
**Subdomain:** Hunting
**Incident Type:** Implementation

## Scenario / Query
How to build hunting queries in Microsoft Sentinel using Kusto Query Language (KQL) operators?

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
1. Use the 'where' operator to filter a table to the subset of rows that satisfy a predicate.
2. Use the 'summarize' operator to produce a table that aggregates the content of the input table.
3. Use the 'join' operator to merge the rows of two tables to form a new table by matching values of the specified columns from each table.
4. Use the 'count' operator to return the number of records in the input record set.
5. Use the 'top' operator to return the first N records sorted by the specified columns.
6. Use the 'limit' operator to return up to the specified number of rows.
7. Use the 'project' operator to select the columns to include, rename or drop, and insert new computed columns.
8. Use the 'extend' operator to create calculated columns and append them to the result set.
9. Use the 'makeset' operator to return a dynamic (JSON) array of the set of distinct values that Expr takes in the group.
10. Use the 'find' operator to find rows that match a predicate across a set of tables.
11. Use the 'adx()' function to perform cross-resource queries of Azure Data Explorer data sources from the Microsoft Sentinel hunting experience and Log Analytics.

## Validation
1. In the Microsoft Sentinel workspace, navigate to the 'Hunting' blade and select 'New Query'. 2. Write a KQL query using the 'where' operator, e.g., `SecurityEvent | where EventID == 4624`, and run it. Confirm that only rows satisfying the predicate are returned. 3. Write a query using 'summarize', e.g., `SecurityEvent | summarize count() by Account`, and verify it produces an aggregated table. 4. Write a query using 'join', e.g., `let A = SecurityEvent | where EventID == 4624; let B = SecurityEvent | where EventID == 4634; A | join kind=inner B on Account`, and confirm rows are merged correctly. 5. Use 'count', e.g., `SecurityEvent | count`, and verify the number of records. 6. Use 'top', e.g., `SecurityEvent | top 10 by TimeGenerated desc`, and confirm the first N records sorted. 7. Use 'limit', e.g., `SecurityEvent | limit 5`, and verify up to 5 rows. 8. Use 'project', e.g., `SecurityEvent | project TimeGenerated, Account`, and confirm only selected columns appear. 9. Use 'extend', e.g., `SecurityEvent | extend EventHour = datetime_part("hour", TimeGenerated)`, and verify the new column. 10. Use 'makeset', e.g., `SecurityEvent | summarize makeset(Account) by EventID`, and confirm a JSON array of distinct values. 11. Use 'find', e.g., `find in (SecurityEvent, SigninLogs) where Account == "user@domain.com"`, and confirm rows from multiple tables. 12. Use the adx() function, e.g., `adx('https://adxcluster.region.kusto.windows.net').DatabaseName | take 10`, and confirm cross-resource query results.

## Rollback
1. Delete any custom hunting queries created during validation by navigating to the 'Hunting' blade, selecting the query, and clicking 'Delete'. 2. If the adx() function was used and caused connectivity issues, remove the query and verify that the Azure Data Explorer cluster is still accessible via its native tools. 3. No other rollback is required as the remediation steps are read-only query operations that do not modify the Sentinel workspace configuration.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/hunting>
