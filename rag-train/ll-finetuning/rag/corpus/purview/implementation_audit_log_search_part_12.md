# Implementation: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Implementation

## Scenario / Query
How to configure audit log search criteria including date range, keyword, and admin units?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log search configuration

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. On the Search page, configure the following search criteria as applicable:
2. Date and time range (UTC): The last seven days are selected by default. Select a date and time range to display the events that occurred within that period. The date and time are presented in Coordinated Universal Time (UTC). The maximum date range that you can specify is 180 days.
3. Keyword Search: Enter a keyword or phrase to search for in the audit log. The keyword or phrase is searched for in the audit log or in the file, folder, or sites (if specified) for the search. To search for text that contains special characters, replace the special characters with an asterisk(*) in your keyword search.
4. Admin Units: Select the drop-down list to display the administrative units you want the audited activities scoped to for your search. You can select one or more administrative units to scope your search to.

## Validation
1. Navigate to Microsoft Purview compliance portal > Audit > Search. 2. Verify the date and time range (UTC) displays the expected period (e.g., last 7 days or custom range up to 180 days). 3. Enter a test keyword or phrase in the Keyword Search field and confirm results include entries containing that term. 4. Select one or more administrative units from the Admin Units drop-down and confirm the search results are scoped to those units. 5. Run a search and confirm the audit log entries match the configured criteria.

## Rollback
1. Reset the date and time range to the default (last 7 days) by clearing custom selections. 2. Clear the Keyword Search field to remove any entered keyword or phrase. 3. Deselect all administrative units in the Admin Units drop-down to remove scope restrictions. 4. Run a search to confirm the audit log returns unfiltered results. 5. If issues persist, restore any previous search criteria from saved searches or documentation.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-search>
