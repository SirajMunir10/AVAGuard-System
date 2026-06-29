# Optimization: Resource Management

**Domain:** Azure
**Subdomain:** Resource Management
**Incident Type:** Optimization

## Scenario / Query
How can I use tags to group billing data for cost tracking across different organizations or runtime environments?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Tags applied to resources, billing data export

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use tags to group usage by cost center.
2. Use tags to categorize costs by runtime environment, including the billing usage for virtual machines running in the production environment.
3. To retrieve information about tags, download the usage file from the Azure portal.

## Validation
1. Verify tags are applied to resources: Run 'az tag list --resource-id <resource-id>' for each tagged resource. 2. Download the usage file from Azure portal: Navigate to Cost Management + Billing > Usage + Charges > Download. 3. Open the downloaded CSV and confirm that the 'Tags' column contains the expected tag keys and values (e.g., 'CostCenter:IT', 'Environment:Production'). 4. Check that billing data for virtual machines in production shows the 'Environment:Production' tag.

## Rollback
1. Remove tags from resources: Run 'az tag delete --resource-id <resource-id> --tag-name <tag-name>' for each tag applied. 2. If tags were applied via policy, disable or delete the policy assignment. 3. Re-download the usage file to confirm tags are no longer present in the 'Tags' column.

## References
- <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources>
