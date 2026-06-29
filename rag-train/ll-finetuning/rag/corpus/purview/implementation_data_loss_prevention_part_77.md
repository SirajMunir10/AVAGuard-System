# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to configure evidence collection for file activities on devices in a DLP policy?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with endpoint monitoring

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enable Setup evidence collection for file activities on devices.
2. Add Azure storage accounts.
3. Select Collect original file as evidence for all selected file activities on Endpoint.
4. Select the Azure storage account you want to copy the items to.
5. Choose the activities you want to copy items for (e.g., Print, Copy to a network share).

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. Select the DLP policy configured for endpoint monitoring. Under 'Location', confirm 'Devices' is included. Under 'Actions', verify 'Collect original file as evidence for all selected file activities on Endpoint' is enabled. 2. In the same policy, under 'Evidence collection settings', confirm the Azure storage account is listed and the selected activities (e.g., Print, Copy to a network share) are checked. 3. On a test device, perform a monitored activity (e.g., print a sensitive file). Wait up to 15 minutes, then check the Azure storage account container for the copied file. Use Azure Storage Explorer or PowerShell: Get-AzStorageBlob -Container 'dlp-evidence' -Context $ctx. Verify the blob exists and contains the original file.

## Rollback
1. In the DLP policy, disable 'Collect original file as evidence for all selected file activities on Endpoint' by unchecking the option. 2. Remove the Azure storage account association from the policy by selecting 'Remove' next to the storage account in the evidence collection settings. 3. Optionally, delete the copied evidence files from the Azure storage account container using Azure Storage Explorer or PowerShell: Remove-AzStorageBlob -Container 'dlp-evidence' -Blob $blobName -Context $ctx. 4. Save the policy changes and confirm the policy is still active for other actions.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
