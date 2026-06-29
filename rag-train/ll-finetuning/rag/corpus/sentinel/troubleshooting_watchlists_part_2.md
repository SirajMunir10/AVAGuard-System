# Troubleshooting: Watchlists

**Domain:** Sentinel
**Subdomain:** Watchlists
**Incident Type:** Troubleshooting

## Scenario / Query
Why do I see both deleted and recreated watchlist entries in Log Analytics after deleting and recreating a watchlist?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Log Analytics workspace with Sentinel watchlists

## Symptoms
- Deleted and recreated watchlist entries appear together in Log Analytics

## Error Codes
N/A

## Root Causes
1. Data ingestion SLA of five minutes may cause temporary overlap of deleted and recreated entries

## Remediation Steps
1. Wait for the five-minute SLA for data ingestion to complete
2. If entries persist together for longer than five minutes, submit a support ticket

## Validation
1. Wait at least 5 minutes after deleting and recreating the watchlist. 2. Run the following KQL query in the Log Analytics workspace to confirm only the new watchlist entries appear: `_GetWatchlist('YourWatchlistAlias') | distinct *`. 3. Verify that the output contains only the recreated entries and no duplicates from the deleted watchlist. 4. Check the watchlist resource in the Azure portal to ensure the current version matches the recreated entries.

## Rollback
1. If duplicate entries persist beyond 5 minutes, do not attempt to delete and recreate the watchlist again. 2. Open a support ticket with Microsoft Azure, referencing the watchlist name, workspace ID, and the KQL query results showing duplicates. 3. As a temporary workaround, use the `_GetWatchlist` function with a filter to exclude the old entries, e.g., `_GetWatchlist('YourWatchlistAlias') | where TimeGenerated > datetime('YYYY-MM-DDTHH:MM:SS')` using the recreation timestamp. 4. Do not modify the watchlist resource until the support team provides guidance.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/watchlists-create>
