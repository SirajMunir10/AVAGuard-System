# Implementation: Watchlists

**Domain:** Sentinel
**Subdomain:** Watchlists
**Incident Type:** Implementation

## Scenario / Query
How do I download a watchlist template from Microsoft Sentinel to populate with data and then upload it?

## Environment Context
- **Tenant Type:** Azure/Defender portal
- **Configuration:** Microsoft Sentinel watchlist templates

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. In the Defender portal, go to Microsoft Sentinel > Configuration > Watchlist.
2. Select the tab Templates (Preview).
3. Select a template from the list to view details of the template in the right pane.
4. Select the ellipses ... at the end of the row.
5. Select Download Schema.
6. Populate your local version of the file and save it locally as a CSV file.
7. Follow the steps to upload watchlist created from a template (Preview).

## Validation
1. In the Defender portal, navigate to Microsoft Sentinel > Configuration > Watchlist. 2. Verify the newly uploaded watchlist appears in the list with the correct name and source (template). 3. Select the watchlist and confirm the preview shows the expected data rows and columns matching the template schema. 4. Optionally, run a KQL query such as '_GetWatchlist('<watchlist_name>')' to confirm the data is queryable.

## Rollback
1. In the Defender portal, go to Microsoft Sentinel > Configuration > Watchlist. 2. Locate the uploaded watchlist. 3. Select the ellipsis (...) at the end of the row and choose 'Delete'. 4. Confirm deletion. 5. If the original template download was modified, re-download the template from the Templates tab by selecting the ellipsis and 'Download Schema' to restore the original schema.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/watchlists-create>
