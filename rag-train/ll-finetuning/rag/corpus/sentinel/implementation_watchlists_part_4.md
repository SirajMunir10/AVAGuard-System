# Implementation: Watchlists

**Domain:** Sentinel
**Subdomain:** Watchlists
**Incident Type:** Implementation

## Scenario / Query
How do I upload a watchlist from a file in Microsoft Sentinel?

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
5. Field: Source type - CSV file with a header (.csv)
6. Field: Number of lines before row with headings - Enter the number of lines before the header row that's in your data file.
7. Field: Upload file - Either drag and drop your data file, or select Browse for files and select the file to upload.
8. Field: SearchKey - Enter the name of a column in your watchlist that you expect to use as a join with other data or a frequent object of searches.
9. Review the information, verify that it's correct, and then select Create.
10. A notification appears once the watchlist is created. It might take several minutes for the watchlist to be created and the new data to be available in queries.

## Validation
1. In the Defender portal, navigate to Microsoft Sentinel > Configuration > Watchlist. 2. Confirm the new watchlist appears in the list with the correct name, description, and alias. 3. Select the watchlist and verify the Source type, number of lines before header, uploaded file name, and SearchKey column match the values entered during creation. 4. Run a sample KQL query using the watchlist alias, e.g., `_GetWatchlist('<alias>')`, and confirm it returns the expected rows from the uploaded file.

## Rollback
1. In the Defender portal, go to Microsoft Sentinel > Configuration > Watchlist. 2. Locate the newly created watchlist. 3. Select the watchlist and choose Delete (or the delete option in the context menu). 4. Confirm the deletion when prompted. 5. If the watchlist was created but data is incorrect, delete it and re-upload the correct file following the original steps.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/watchlists-create>
