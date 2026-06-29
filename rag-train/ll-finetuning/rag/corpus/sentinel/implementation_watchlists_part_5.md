# Implementation: Watchlists

**Domain:** Sentinel
**Subdomain:** Watchlists
**Incident Type:** Implementation

## Scenario / Query
How to upload a watchlist created from a template in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure/Defender portal
- **Configuration:** Microsoft Sentinel > Configuration > Watchlist

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. In the Defender portal, go to Microsoft Sentinel > Configuration > Watchlist.
2. Select the tab Templates (Preview).
3. Select the appropriate template from the list to view details of the template in the right pane.
4. Select Create from template to open the Watchlist wizard.
5. On the General page, notice that the Name, Description, and Alias fields are all read-only. Select Next: Source.
6. On the Source page, select Browse for files, and then select the file you created from the template.
7. Select Next: Review + create, and then select Create. A notification appears once the watchlist is created.

## Validation
1. In the Defender portal, navigate to Microsoft Sentinel > Configuration > Watchlist. 2. Confirm the new watchlist appears in the list with the expected Name, Description, and Alias. 3. Select the watchlist and verify its status shows as 'Active'. 4. Optionally, run the following KQL query to confirm the watchlist data is accessible: `_GetWatchlist('<Alias>')` (replace <Alias> with the actual alias). 5. Check that no errors or warnings are displayed in the watchlist details pane.

## Rollback
1. In the Defender portal, go to Microsoft Sentinel > Configuration > Watchlist. 2. Locate the newly created watchlist. 3. Select the watchlist and choose 'Delete' from the context menu or toolbar. 4. Confirm the deletion when prompted. 5. Verify the watchlist no longer appears in the list. 6. If the watchlist was created from a template and the file upload was incorrect, delete the watchlist and re-upload the correct file following the original steps.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/watchlists-create>
