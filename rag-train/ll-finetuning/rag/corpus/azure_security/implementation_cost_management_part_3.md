# Implementation: Cost Management

**Domain:** Azure
**Subdomain:** Cost Management
**Incident Type:** Implementation

## Scenario / Query
How to group costs for an Azure resource using the cm-resource-parent tag?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** cm-resource-parent tag

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the cm-resource-parent tag with the value set to the resource ID of the Azure resource you want to group costs by.
2. For example, to group costs by an Azure Virtual Desktop host pool, provide the resource ID of the host pool.

## Validation
1. Verify that the cm-resource-parent tag is applied to the target resource by running: az tag list --resource-id <resource-id> --query "properties.tags.cm-resource-parent" -o tsv. 2. Confirm that the tag value matches the resource ID of the parent resource (e.g., the host pool resource ID). 3. Check that cost grouping appears in Cost Management by navigating to Cost analysis > Group by > Tag, and selecting cm-resource-parent. 4. Validate that costs are aggregated under the parent resource ID in the cost report.

## Rollback
1. Remove the cm-resource-parent tag from the resource by running: az tag delete --resource-id <resource-id> --tag-name cm-resource-parent. 2. If the tag was applied at a subscription or resource group scope, remove it from that scope using: az tag delete --resource-id <scope-id> --tag-name cm-resource-parent. 3. Verify removal by running: az tag list --resource-id <resource-id> --query "properties.tags.cm-resource-parent" -o tsv (should return empty). 4. Confirm that cost grouping no longer uses the tag by checking Cost analysis > Group by > Tag for cm-resource-parent.

## References
- <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources>
