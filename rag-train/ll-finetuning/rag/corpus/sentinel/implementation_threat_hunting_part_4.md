# Implementation: Threat Hunting

**Domain:** Sentinel
**Subdomain:** Threat Hunting
**Incident Type:** Implementation

## Scenario / Query
How do I investigate a bookmarked finding using the interactive entity-graph diagram in Azure Sentinel?

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
1. Investigate a single bookmarked finding by selecting the bookmark and then clicking Investigate in the details pane to open the investigation experience.
2. View, investigate, and visually communicate your findings by using an interactive entity-graph diagram and timeline.

## Validation
1. In the Azure Sentinel workspace, navigate to Threat Management > Hunting > Bookmarks. 2. Select the bookmarked finding you investigated. 3. In the details pane, confirm the 'Investigate' button is present and click it. 4. Verify that the investigation experience opens with an interactive entity-graph diagram and timeline. 5. Confirm that entities related to the bookmark are displayed in the graph and timeline events are visible.

## Rollback
1. Close the investigation experience by clicking the 'X' in the top-right corner of the investigation pane. 2. If the investigation experience fails to load or displays incorrect data, clear the browser cache and retry step 1. 3. If the issue persists, verify that the Azure Sentinel workspace is healthy by checking the workspace status in the Azure portal. 4. If the workspace is degraded, contact Azure support to restore normal operations.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/hunting>
