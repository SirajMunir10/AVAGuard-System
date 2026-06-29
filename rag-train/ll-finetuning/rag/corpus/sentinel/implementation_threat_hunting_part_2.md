# Implementation: Threat Hunting

**Domain:** Sentinel
**Subdomain:** Threat Hunting
**Incident Type:** Implementation

## Scenario / Query
How do I create and manage bookmarks in Azure Sentinel for tracking suspicious events during threat hunting?

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
1. In your results, mark the checkboxes for any rows you want to preserve, and select Add bookmark.
2. Add your own tags and notes to each bookmark.
3. Enrich your bookmarks with entity mappings to extract multiple entity types and identifiers, and MITRE ATT&CK mappings to associate particular tactics and techniques.
4. View all the bookmarked findings by clicking on the Bookmarks tab in the main Hunting page.
5. Add tags to bookmarks to classify them for filtering.
6. Investigate a single bookmarked finding by selecting the bookmark and then clicking Investigate in the details pane to open the investigation experience.

## Validation
1. Navigate to Azure Sentinel -> Threat Hunting -> Bookmarks tab. Confirm the bookmark appears in the list with the correct tags and notes. 2. Select the bookmark and verify the details pane shows entity mappings and MITRE ATT&CK mappings as configured. 3. Click 'Investigate' and confirm the investigation graph opens with the expected entities and alerts.

## Rollback
1. In the Bookmarks tab, select the bookmark to remove. 2. Click 'Delete' or use the delete option in the details pane to remove the bookmark. 3. If tags or notes were added, remove them by editing the bookmark and clearing the fields. 4. If entity mappings or MITRE ATT&CK mappings were added, edit the bookmark and remove those mappings.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/hunting>
