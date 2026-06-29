# Implementation: Watchlists

**Domain:** Sentinel
**Subdomain:** Watchlists
**Incident Type:** Implementation

## Scenario / Query
How to create a large watchlist from a file in Azure Storage (preview) for Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Azure Storage account with a CSV file up to 500 MB

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Upload your watchlist file to your Azure Storage account.
2. Create a shared access signature URL for Microsoft Sentinel to retrieve the watchlist data.
3. Add the watchlist to your workspace in Microsoft Sentinel.

## Validation
1. Verify the watchlist file is uploaded to the Azure Storage container: `az storage blob list --account-name <storage_account_name> --container-name <container_name> --output table`
2. Confirm the SAS URL is generated and valid: `az storage container generate-sas --account-name <storage_account_name> --name <container_name> --permissions r --expiry <expiry_date> --https-only`
3. In Microsoft Sentinel, navigate to Watchlists, select the watchlist, and confirm the 'Last refreshed' time is recent and the file size matches the uploaded file.
4. Run a sample query using the watchlist: `_GetWatchlist('<watchlist_alias>') | take 10` to verify data is accessible.

## Rollback
1. Delete the watchlist from Microsoft Sentinel: In the Azure portal, go to Microsoft Sentinel > Watchlists, select the watchlist, and click 'Delete'.
2. Revoke the SAS URL by regenerating the storage account key: `az storage account keys renew --account-name <storage_account_name> --key primary`
3. Remove the uploaded file from Azure Storage: `az storage blob delete --account-name <storage_account_name> --container-name <container_name> --name <blob_name>`
4. If the watchlist was previously in use, restore from a backup or recreate using the original data source.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/watchlists-create>
