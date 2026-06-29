# Troubleshooting: Threat Intelligence

**Domain:** Sentinel
**Subdomain:** Threat Intelligence
**Incident Type:** Troubleshooting

## Scenario / Query
How do I view the export history for a threat intelligence item in Microsoft Sentinel or Defender portal?

## Environment Context
- **Tenant Type:** Azure or Defender
- **Configuration:** Threat intelligence page (Azure portal) or Intel management (Defender portal)

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to the exported item in either the Intel management (Defender portal) or Threat intelligence page (Azure portal).
2. In the Exports column, select View export history to show the export history for that item.

## Validation
1. In the Azure portal, navigate to Microsoft Sentinel > Threat intelligence. 2. Locate the specific threat intelligence item. 3. In the Exports column, confirm that 'View export history' is visible and clickable. 4. Click 'View export history' and verify that the export history pane opens and displays the expected export records (e.g., timestamp, destination, status). 5. In the Defender portal, go to Intel management, find the same item, and repeat steps 3-4 to confirm consistency.

## Rollback
1. If the export history does not display correctly, refresh the Threat intelligence page (Azure portal) or Intel management page (Defender portal). 2. If the issue persists, clear the browser cache and cookies, then reload the portal. 3. If the export history pane fails to open, try accessing the item from the alternate portal (e.g., if using Azure portal, switch to Defender portal). 4. If no export history is shown and it was expected, verify that the item was previously exported using the export feature; if not, no rollback is needed. 5. If the export history shows incorrect data, contact Microsoft support with the item ID and timestamps for further investigation.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/work-with-threat-indicators>
