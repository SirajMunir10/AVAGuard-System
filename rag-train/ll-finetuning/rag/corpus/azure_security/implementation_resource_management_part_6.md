# Implementation: Resource Management

**Domain:** Azure
**Subdomain:** Resource Management
**Incident Type:** Implementation

## Scenario / Query
How to implement a tagging strategy for Azure resources, resource groups, and subscriptions?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Tags can be applied to Azure resources, resource groups, and subscriptions but not to management groups

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. See Resource naming and tagging decision guide for recommendations on how to implement a tagging strategy
2. Use one of the tag policies to ensure cost-accruing services are provisioned with a tag

## Validation
1. Verify tags are applied to resources: Run 'az tag list --resource-id /subscriptions/{subscription-id}/resourceGroups/{resource-group}/providers/{resource-provider}/{resource-type}/{resource-name}' for each tagged resource. 2. Confirm tags on resource groups: Run 'az group show --name {resource-group-name} --query tags' for each group. 3. Check tags on subscriptions: Run 'az account tag list --resource-id /subscriptions/{subscription-id}' for each subscription. 4. Validate tag policies are enforced: Run 'az policy state list --resource-id /subscriptions/{subscription-id}/resourceGroups/{resource-group}/providers/{resource-provider}/{resource-type}/{resource-name}' to confirm compliance.

## Rollback
1. Remove tags from resources: Run 'az tag delete --resource-id /subscriptions/{subscription-id}/resourceGroups/{resource-group}/providers/{resource-provider}/{resource-type}/{resource-name} --tag-names {tag-name}' for each tag. 2. Remove tags from resource groups: Run 'az group update --name {resource-group-name} --remove tags.{tag-name}'. 3. Remove tags from subscriptions: Run 'az account tag delete --resource-id /subscriptions/{subscription-id} --tag-names {tag-name}'. 4. Disable or delete tag policies: Run 'az policy assignment delete --name {policy-assignment-name}' for each policy assignment.

## References
- <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources>
