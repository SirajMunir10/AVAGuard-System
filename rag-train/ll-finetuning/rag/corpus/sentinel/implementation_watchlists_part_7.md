# Implementation: Watchlists

**Domain:** Sentinel
**Subdomain:** Watchlists
**Incident Type:** Implementation

## Scenario / Query
How do I upload a watchlist file to Azure Storage for use in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace, Azure Storage account

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. If you don't already have an Azure Storage account, create a storage account. The storage account can be in a different resource group or region from your workspace in Microsoft Sentinel.
2. Use either AzCopy or the Azure portal to upload your CSV file with your watchlist data into the storage account.
3. If you don't already have a storage container, create one by running the following command: azcopy make https://<storage-account-name>.<blob or dfs>.core.windows.net/<container-name>
4. Next, run the following command to upload the file: azcopy copy '<local-file-path>' 'https://<storage-account-name>.<blob or dfs>.core.windows.net/<container-name>/<blob-name>'
5. If you don't use AzCopy, upload your file by using the Azure portal. Go to your storage account in Azure portal to upload the CSV file with your watchlist data. If you don't already have an existing storage container, create a container. For the level of public access to the container, use the default which is set to Private (no anonymous access). Upload a block blob to upload your CSV file to the storage account.

## Validation
1. Verify the storage account exists and is accessible: `az storage account show --name <storage-account-name> --resource-group <resource-group-name>` (if known). 2. Confirm the container exists: `az storage container exists --name <container-name> --account-name <storage-account-name> --auth-mode login` (or use `azcopy list https://<storage-account-name>.blob.core.windows.net/<container-name>`). 3. Check that the CSV file is uploaded: `az storage blob exists --container-name <container-name> --name <blob-name> --account-name <storage-account-name> --auth-mode login` (or `azcopy list https://<storage-account-name>.blob.core.windows.net/<container-name>` and look for the file). 4. In Azure portal, navigate to the storage account, select 'Containers', open the container, and confirm the CSV file appears with the correct size and last modified date. 5. In Microsoft Sentinel, go to 'Watchlists' and verify the watchlist can be created from the uploaded file (optional, but confirms end-to-end readiness).

## Rollback
1. If the storage account was newly created and is no longer needed, delete it: `az storage account delete --name <storage-account-name> --resource-group <resource-group-name> --yes`. 2. If only the container was created, delete it: `az storage container delete --name <container-name> --account-name <storage-account-name> --auth-mode login` (or use `azcopy remove https://<storage-account-name>.blob.core.windows.net/<container-name>?<SAS-token>` with appropriate permissions). 3. If the CSV file was uploaded incorrectly, delete it: `az storage blob delete --container-name <container-name> --name <blob-name> --account-name <storage-account-name> --auth-mode login` (or use `azcopy remove https://<storage-account-name>.blob.core.windows.net/<container-name>/<blob-name>`). 4. If using Azure portal, navigate to the storage account, select 'Containers', open the container, select the blob, and click 'Delete'. 5. Confirm removal by listing the container contents again.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/watchlists-create>
