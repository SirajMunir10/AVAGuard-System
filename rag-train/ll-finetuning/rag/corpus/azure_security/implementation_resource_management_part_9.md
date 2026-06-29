# Implementation: Resource Management

**Domain:** Azure
**Subdomain:** Resource Management
**Incident Type:** Implementation

## Scenario / Query
Which Azure resources only support 15 tags and what are the implications?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Tagging limits

## Symptoms
- Unable to add more than 15 tags to specific resources

## Error Codes
N/A

## Root Causes
1. The following Azure resources only support 15 tags: Azure Automation, Azure Content Delivery Network, Azure Public DNS (Zone and A records), Azure Private DNS (Zone and A records), Azure Log Analytics saved search

## Remediation Steps
1. Limit the number of tags applied to these resources to 15 or fewer
2. Consolidate tags if more than 15 are needed

## Validation
1. Run the following Azure CLI command to list tags on an affected resource (e.g., Automation account):
   az resource show --resource-group <rg-name> --resource-type "Microsoft.Automation/automationAccounts" --name <resource-name> --query tags
2. Count the number of tags returned. Confirm the count is ≤ 15.
3. Repeat for each resource type listed: Content Delivery Network profile (Microsoft.Cdn/profiles), Public DNS zone (Microsoft.Network/dnsZones), Private DNS zone (Microsoft.Network/privateDnsZones), Log Analytics saved search (Microsoft.OperationalInsights/workspaces/savedSearches).
4. Verify that no error is returned when attempting to add a new tag (if under the limit) or that the resource accepts the tag update without failure.

## Rollback
1. If the remediation (consolidation or removal of tags) causes loss of required metadata or breaks automation, restore the original tags from a backup or script.
2. Use Azure CLI to reapply the removed tags:
   az resource tag --resource-group <rg-name> --resource-type <resource-type> --name <resource-name> --tags <original-tag-key>=<original-tag-value>
3. If consolidation was performed, split the consolidated tags back into individual tags (ensuring total ≤ 15).
4. If the resource still fails to accept tags, verify that no other policy or limit is blocking the update and contact support if needed.

## References
- <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources>
