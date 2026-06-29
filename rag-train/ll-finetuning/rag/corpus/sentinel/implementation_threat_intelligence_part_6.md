# Implementation: Threat Intelligence

**Domain:** Sentinel
**Subdomain:** Threat Intelligence
**Incident Type:** Implementation

## Scenario / Query
How do I view, sort, filter, and search threat intelligence in the Microsoft Sentinel management interface without writing a Log Analytics query?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace with threat intelligence sources ingested

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. From the management interface, expand the 'What would you like to search?' menu.
2. Select a STIX object type or leave the default 'All object types'.
3. Select conditions using logical operators.
4. Select the object you want to see more information about.

## Validation
1. In the Azure portal, navigate to your Microsoft Sentinel workspace.
2. Under 'Threat management', select 'Threat intelligence'.
3. Expand the 'What would you like to search?' menu and confirm that STIX object types (e.g., indicator, threat-actor, attack-pattern) are listed.
4. Select a specific STIX object type (e.g., 'indicator') and verify that the list of indicators appears.
5. Use the condition filters (e.g., 'Created date' > 'Last 7 days') and confirm the results update accordingly.
6. Click on any object in the list and verify that the detail pane opens showing full information.

## Rollback
1. If the threat intelligence page does not load or shows errors, refresh the browser and re-navigate to the Sentinel workspace.
2. If STIX object types are missing, ensure that threat intelligence connectors (e.g., Microsoft Defender Threat Intelligence, TAXII) are enabled and data is ingested.
3. If filters do not apply correctly, clear all filters by clicking 'Reset filters' and reapply them one at a time.
4. If object details do not open, try selecting a different object or use the 'Search' box to locate a specific indicator.
5. If the issue persists, verify that the user has at least 'Microsoft Sentinel Reader' role permissions on the workspace.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/work-with-threat-indicators>
