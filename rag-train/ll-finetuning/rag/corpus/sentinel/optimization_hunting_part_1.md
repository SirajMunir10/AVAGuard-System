# Optimization: Hunting

**Domain:** Sentinel
**Subdomain:** Hunting
**Incident Type:** Optimization

## Scenario / Query
How do I identify spikes in data using hunting query results?

## Environment Context
- **Tenant Type:** Microsoft Sentinel in Defender
- **Configuration:** Hunting > Queries tab

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Sort or filter on Results delta or Results delta percentage.
2. Compare the results of the last 24 hours against the results of the previous 24-48 hours to highlight any large differences or relative difference in volume.

## Validation
1. In the Microsoft Sentinel (in Defender) portal, navigate to 'Hunting' > 'Queries' tab. 2. Run the hunting query of interest. 3. In the results pane, locate the 'Results delta' and 'Results delta percentage' columns. 4. Confirm that the query results for the last 24 hours show a significant difference (spike) compared to the previous 24-48 hours, as indicated by a high 'Results delta percentage' or a large absolute 'Results delta' value. 5. Optionally, sort or filter by these columns to verify the spike is clearly visible.

## Rollback
1. Remove any custom sorting or filtering applied to the 'Results delta' or 'Results delta percentage' columns in the hunting query results view. 2. If a new hunting query was created to identify spikes, delete that query from the 'Queries' tab. 3. Revert any changes to existing hunting queries that were modified during the remediation. 4. Confirm that the hunting query results return to the default view without spike indicators.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/hunting>
