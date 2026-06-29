# Implementation: Resource Management

**Domain:** Azure
**Subdomain:** Resource Management
**Incident Type:** Implementation

## Scenario / Query
What are the tag naming restrictions for Azure DNS, Traffic Manager, and Azure Front Door resources?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Tagging policies

## Symptoms
- Tag creation fails or is rejected
- Tags contain unsupported characters

## Error Codes
N/A

## Root Causes
1. Azure DNS tag names do not support special and Unicode characters
2. Traffic Manager does not support spaces, #, or : in tag names
3. Traffic Manager tag names cannot start with a number
4. Azure Front Door does not support # or : in tag names
5. Azure DNS zones do not support spaces or parentheses in tags
6. Azure DNS zones do not support tags starting with a number

## Remediation Steps
1. Ensure tag names for Azure DNS do not contain special or Unicode characters
2. Ensure tag names for Traffic Manager do not contain spaces, #, or : and do not start with a number
3. Ensure tag names for Azure Front Door do not contain # or :
4. Ensure tag names for Azure DNS zones do not contain spaces or parentheses and do not start with a number

## Validation
1. For each Azure DNS zone, run: `Get-AzDnsZone -ResourceGroupName <RG> -Name <zone> | Select-Object Tags` and verify that all tag names contain only alphanumeric characters, hyphens, underscores, and periods (no spaces, parentheses, Unicode, or special characters) and do not start with a number. 2. For each Traffic Manager profile, run: `Get-AzTrafficManagerProfile -ResourceGroupName <RG> -Name <profile> | Select-Object Tags` and verify that tag names contain no spaces, '#', or ':', and do not start with a number. 3. For each Azure Front Door resource, run: `Get-AzFrontDoor -ResourceGroupName <RG> -Name <frontdoor> | Select-Object Tags` and verify that tag names contain no '#' or ':'. 4. Attempt to create a test tag with allowed characters on each resource type using `Update-AzTag -ResourceId <resourceId> -Tag @{testkey='testvalue'} -Operation Merge` and confirm success.

## Rollback
1. If validation fails, remove any non-compliant tags using `Update-AzTag -ResourceId <resourceId> -Tag @{<nonCompliantKey>=$null} -Operation Delete`. 2. Reapply the original tags that were removed during remediation using `Update-AzTag -ResourceId <resourceId> -Tag @{<originalKey>='<originalValue>'} -Operation Merge`. 3. If the remediation caused resource creation or update failures, restore the previous tag set by running `Update-AzTag -ResourceId <resourceId> -Tag $originalTags -Operation Replace` where `$originalTags` is a hashtable of the tags before remediation. 4. Verify rollback by repeating the validation steps and confirming the tags match the pre-remediation state.

## References
- <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources>
