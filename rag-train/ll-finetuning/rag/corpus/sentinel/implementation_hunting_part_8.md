# Implementation: Hunting

**Domain:** Sentinel
**Subdomain:** Hunting
**Incident Type:** Implementation

## Scenario / Query
How do I create or edit a custom hunting query in Microsoft Sentinel and save it for my tenant or share it with other users in the same tenant?

## Environment Context
- **Tenant Type:** Microsoft Sentinel tenant
- **Configuration:** Hunting > Queries tab

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to the Hunting > Queries tab in Microsoft Sentinel.
2. Create or edit a query and save it as your own query or share it with users who are in the same tenant.

## Validation
1. Navigate to the Microsoft Sentinel workspace, then go to 'Hunting' > 'Queries' tab. 2. Confirm the custom query appears in the 'My queries' list (if saved as own) or in the 'All queries' list (if shared). 3. Run the query and verify it returns expected results. 4. If shared, log in as another user in the same tenant and confirm the query is visible under 'All queries'.

## Rollback
1. Navigate to 'Hunting' > 'Queries' tab. 2. Locate the custom query. 3. Select the query and click 'Delete' to remove it. 4. If the query was shared, ensure it is removed from all users' views. 5. If editing an existing query, revert to the original query text (if backed up) or recreate from known good version.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/hunting>
