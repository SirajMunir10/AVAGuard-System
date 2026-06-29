# Implementation: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Implementation

## Scenario / Query
How to scope an audit log search for specific record types associated with sensitivity labels in Microsoft Purview Information Protection?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Purview Audit Log Search with Record Types

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select the drop-down list to display the record types for audited activities
2. Select one or more record types to search for
3. Use the search box over the list to find a specific record type
4. For sensitivity labels in MIP, select MIPLabel, MipAutoLabelExchangeItem, MipAutoLabelSharePointItem, and MipAutoLabelSharePointPolicyLocation record types from the list

## Validation
1. Navigate to Microsoft Purview compliance portal > Audit > Audit log search. 2. Click the 'Record type' drop-down and verify that the list includes 'MIPLabel', 'MipAutoLabelExchangeItem', 'MipAutoLabelSharePointItem', and 'MipAutoLabelSharePointPolicyLocation'. 3. Select each of these record types and confirm they are checked. 4. Run a search with a date range covering recent activity and verify that results return entries for sensitivity label actions (e.g., label applied, label changed). 5. Optionally, export the search results and confirm the 'RecordType' column contains the selected values.

## Rollback
1. In the same Audit log search page, click the 'Record type' drop-down. 2. Uncheck any of the selected record types (MIPLabel, MipAutoLabelExchangeItem, MipAutoLabelSharePointItem, MipAutoLabelSharePointPolicyLocation) to remove them from the search scope. 3. Alternatively, click 'Clear all' to reset the record type selection to default. 4. Run a new search to confirm that sensitivity label activities are no longer filtered in the results.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-search>
