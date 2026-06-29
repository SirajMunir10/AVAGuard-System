# Optimization: Insider Risk Management

**Domain:** Purview
**Subdomain:** Insider Risk Management
**Incident Type:** Optimization

## Scenario / Query
How to filter cases, save a view of a filter set, customize columns, or search for alerts in Insider Risk Management?

## Environment Context
- **Tenant Type:** Purview
- **Configuration:** Insider Risk Management policies active

## Symptoms
- Large queue of cases that is challenging to review

## Error Codes
N/A

## Root Causes
1. Number and type of active Insider Risk Management policies

## Remediation Steps
1. Filter cases by various attributes
2. Save a view of a filter set to reuse later
3. Display or hide columns
4. Search for an alert

## Validation
1. Navigate to Microsoft Purview compliance portal > Insider Risk Management > Cases. 2. Apply a filter (e.g., by status, date range, or policy) and confirm the case list updates accordingly. 3. Save the current filter set as a custom view using the 'Save view' option. 4. Switch to another view, then reload the saved view to verify it restores the original filters. 5. Customize columns by adding or removing fields (e.g., 'Case ID', 'Status', 'Last updated') and confirm the table reflects the changes. 6. Use the search box to enter a keyword or alert ID and verify that matching alerts appear in the results.

## Rollback
1. Delete any saved custom views by selecting the view name and choosing 'Delete view'. 2. Reset column customization by clicking 'Columns' and selecting 'Reset to default'. 3. Clear any active filters by clicking 'Clear filters' or removing each filter individually. 4. Clear the search box to remove any alert search query. 5. Refresh the Cases page to return to the default view.

## References
- <https://learn.microsoft.com/en-us/purview/insider-risk-management-cases>
