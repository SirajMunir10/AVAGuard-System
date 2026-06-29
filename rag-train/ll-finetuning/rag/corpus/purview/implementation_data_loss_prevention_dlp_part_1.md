# Implementation: Data Loss Prevention (DLP)

**Domain:** Purview
**Subdomain:** Data Loss Prevention (DLP)
**Incident Type:** Implementation

## Scenario / Query
How do I set up evidence collection for file activities on devices in Microsoft Purview DLP?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP policies, Azure storage account

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Create an Azure storage account and a container in that storage account.
2. Configure permissions for the storage account.
3. Add the name and URL of the storage account in the DLP endpoint settings section for evidence collection.

## Validation
1. Verify the Azure storage account exists: `Get-AzStorageAccount -ResourceGroupName <ResourceGroupName> -Name <StorageAccountName>`
2. Confirm the container exists: `Get-AzStorageContainer -Name <ContainerName> -Context (Get-AzStorageAccount -ResourceGroupName <ResourceGroupName> -Name <StorageAccountName>).Context`
3. Check that the storage account permissions include the DLP service principal (e.g., Storage Blob Data Contributor) using Azure portal or `Get-AzRoleAssignment -Scope /subscriptions/<SubscriptionId>/resourceGroups/<ResourceGroupName>/providers/Microsoft.Storage/storageAccounts/<StorageAccountName>`
4. In the Microsoft Purview compliance portal, navigate to Data Loss Prevention > Endpoint DLP settings > Evidence collection and confirm the storage account name and container URL are correctly entered.
5. Initiate a test file activity on a device with Endpoint DLP policy and verify that evidence files appear in the container within a few minutes.

## Rollback
1. Remove the storage account name and container URL from the DLP endpoint settings: In the Microsoft Purview compliance portal, go to Data Loss Prevention > Endpoint DLP settings > Evidence collection and clear the fields.
2. Optionally, delete the container: `Remove-AzStorageContainer -Name <ContainerName> -Context (Get-AzStorageAccount -ResourceGroupName <ResourceGroupName> -Name <StorageAccountName>).Context -Force`
3. Optionally, delete the storage account: `Remove-AzStorageAccount -ResourceGroupName <ResourceGroupName> -Name <StorageAccountName> -Force`
4. Remove any role assignments for the DLP service principal: `Remove-AzRoleAssignment -ObjectId <DlpServicePrincipalObjectId> -RoleDefinitionName 'Storage Blob Data Contributor' -Scope /subscriptions/<SubscriptionId>/resourceGroups/<ResourceGroupName>/providers/Microsoft.Storage/storageAccounts/<StorageAccountName>`

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
