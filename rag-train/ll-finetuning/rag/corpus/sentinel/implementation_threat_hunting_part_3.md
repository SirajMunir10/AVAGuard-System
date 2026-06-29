# Implementation: Threat Hunting

**Domain:** Sentinel
**Subdomain:** Threat Hunting
**Incident Type:** Implementation

## Scenario / Query
How do I use tags to filter bookmarks by campaign in Azure Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Azure Sentinel workspace with threat hunting enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Add tags to bookmarks to classify them for filtering.
2. For example, if you're investigating an attack campaign, you can create a tag for the campaign, apply the tag to any relevant bookmarks, and then filter all the bookmarks based on the campaign.

## Validation
1. In the Azure Sentinel workspace, navigate to Threat Management > Hunting > Bookmarks.
2. Select a bookmark that was tagged during remediation and confirm the tag appears in the Tags column.
3. Use the 'Tag' filter at the top of the bookmarks list to select the campaign tag; verify that only bookmarks with that tag are displayed.
4. Optionally, run the following Azure CLI command to list bookmarks with a specific tag: az sentinel bookmark list --workspace-name <workspace-name> --resource-group <resource-group> --query "[?tags.contains(@, 'campaign-tag')]"

## Rollback
1. In the Azure Sentinel workspace, navigate to Threat Management > Hunting > Bookmarks.
2. Select each bookmark that was incorrectly tagged, click 'Edit', remove the campaign tag from the Tags field, and save.
3. If the tag was created solely for this remediation and is no longer needed, ensure no bookmarks remain tagged with it; the tag will automatically disappear from the filter list when no bookmarks use it.
4. To remove tags programmatically, use: az sentinel bookmark update --workspace-name <workspace-name> --resource-group <resource-group> --bookmark-id <bookmark-id> --tags "[]"

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/hunting>
