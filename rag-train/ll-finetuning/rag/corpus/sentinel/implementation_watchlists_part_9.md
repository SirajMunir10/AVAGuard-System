# Implementation: Watchlists

**Domain:** Sentinel
**Subdomain:** Watchlists
**Incident Type:** Implementation

## Scenario / Query
How do I add a watchlist to a Microsoft Sentinel workspace in the Defender portal?

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
1. In the Defender portal, go to Microsoft Sentinel > Configuration > Watchlist.
2. Select + New to open the Watchlist wizard.
3. On the General page, enter the name, description, and alias for the watchlist, and then select Next: Source.
4. On the Source page, use the information in the following table to upload your watchlist data, and then select Next: Review + create.
5. Review the information, verify that it's correct, and then select Create.

## Validation
1. In the Defender portal, navigate to Microsoft Sentinel > Configuration > Watchlist.
2. Confirm the newly created watchlist appears in the list with the correct name, description, and alias.
3. Select the watchlist and verify that the uploaded data (e.g., CSV or JSON content) is displayed correctly in the preview pane.
4. Optionally, run a KQL query referencing the watchlist alias to confirm it can be used in analytics rules or hunting: `_GetWatchlist('<alias>')` should return the expected rows.

## Rollback
1. In the Defender portal, go to Microsoft Sentinel > Configuration > Watchlist.
2. Locate the watchlist you created and select it.
3. Click the delete icon or select Delete from the context menu.
4. Confirm the deletion when prompted.
5. Verify the watchlist no longer appears in the list and that any associated analytics rules or queries that referenced it will need to be updated or removed.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/watchlists-create>
