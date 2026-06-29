# Troubleshooting: Watchlists

**Domain:** Sentinel
**Subdomain:** Watchlists
**Incident Type:** Troubleshooting

## Scenario / Query
How do I view the status of a watchlist in Microsoft Sentinel to confirm it is ready for use in queries?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Watchlist not appearing in Log Analytics queries
- Unable to use watchlist in KQL queries

## Error Codes
N/A

## Root Causes
1. Watchlist may still be processing or failed to load

## Remediation Steps
1. In the Defender portal, go to Microsoft Sentinel > Configuration > Watchlist.
2. On the My Watchlists tab, select the watchlist.
3. On the details page, review the Status (Preview).
4. When the status is Succeeded, select View in logs to use the watchlist in a query.
5. Note: It might take several minutes for the watchlist to show in Log Analytics.

## Validation
1. In the Defender portal, navigate to Microsoft Sentinel > Configuration > Watchlist.
2. On the My Watchlists tab, select the watchlist you created.
3. On the details page, check the Status (Preview) field. Confirm it shows 'Succeeded'.
4. If the status is 'Succeeded', select 'View in logs' to open the Log Analytics query editor.
5. Run a KQL query referencing the watchlist, e.g., '_GetWatchlist('<watchlist-alias>')' or use it in a join. Verify that the query returns the expected data without errors.

## Rollback
1. If the watchlist status shows 'Failed' or remains 'Processing' for an extended period, delete the watchlist: In the Defender portal, go to Microsoft Sentinel > Configuration > Watchlist, select the watchlist, and choose 'Delete'.
2. Re-create the watchlist by uploading the CSV file again or re-entering the data. Ensure the file format matches the expected schema.
3. Wait several minutes for the new watchlist to process. Then follow the validation steps to confirm it reaches 'Succeeded' status and is usable in queries.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/watchlists-create>
