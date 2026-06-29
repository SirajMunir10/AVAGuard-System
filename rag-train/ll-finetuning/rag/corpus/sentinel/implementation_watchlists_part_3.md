# Implementation: Watchlists

**Domain:** Sentinel
**Subdomain:** Watchlists
**Incident Type:** Implementation

## Scenario / Query
How do I upload a CSV file from a local folder to create a watchlist in Microsoft Sentinel?

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
1. For a watchlist file you created without a watchlist template: Select Add new and enter the required information.
2. For a watchlist file created from a template downloaded from Microsoft Sentinel: Go to the watchlist Templates (Preview) tab. Select the option Create from template. Azure pre-populates the name, description, and watchlist alias for you.

## Validation
1. Navigate to Microsoft Sentinel workspace. 2. Go to Watchlists blade. 3. Confirm the new watchlist appears in the list with correct alias and source file name. 4. Select the watchlist and verify the preview shows the expected rows and columns from the uploaded CSV. 5. Optionally run a KQL query: `_GetWatchlist('<watchlist_alias>')` to confirm data is queryable.

## Rollback
1. In Microsoft Sentinel, go to Watchlists blade. 2. Select the watchlist created from the uploaded CSV. 3. Click Delete and confirm deletion. 4. If the watchlist was created from a template, also delete any associated watchlist items by running: `Watchlist | where WatchlistAlias == '<watchlist_alias>' | delete` in KQL (requires appropriate permissions). 5. Verify the watchlist no longer appears in the list and queries against it return no results.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/watchlists-create>
