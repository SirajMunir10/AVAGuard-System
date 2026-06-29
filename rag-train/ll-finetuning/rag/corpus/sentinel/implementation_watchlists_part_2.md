# Implementation: Watchlists

**Domain:** Sentinel
**Subdomain:** Watchlists
**Incident Type:** Implementation

## Scenario / Query
How do I create a watchlist in Microsoft Sentinel by uploading a file from a local folder?

## Environment Context
- **Tenant Type:** Microsoft Sentinel in Azure portal or Defender portal
- **Configuration:** Watchlists feature

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Upload a watchlist file from a local folder
2. Upload a watchlist file from your Azure Storage account
3. Create a watchlist manually

## Validation
1. In Microsoft Sentinel, navigate to Threat Management > Watchlists. 2. Confirm the newly created watchlist appears in the list with the correct name, alias, and source type (e.g., Local file). 3. Select the watchlist and click 'View watchlist' to verify the data rows and columns match the uploaded file. 4. Optionally, run a sample KQL query: `_GetWatchlist('<watchlist-alias>')` to ensure the watchlist returns the expected records.

## Rollback
1. In Microsoft Sentinel, go to Threat Management > Watchlists. 2. Select the watchlist you created. 3. Click 'Delete' and confirm the deletion. 4. If the watchlist was created from a local file, no further cleanup is needed. If it was created from an Azure Storage account, ensure the source file remains unchanged or remove it if desired. 5. If the watchlist was created manually, note that manual entries are lost upon deletion.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/watchlists-create>
