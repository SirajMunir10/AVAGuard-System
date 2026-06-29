# Implementation: Hunting

**Domain:** Sentinel
**Subdomain:** Hunting
**Incident Type:** Implementation

## Scenario / Query
How to set up and run a hunting query in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to the Microsoft Sentinel workspace in the Azure portal.
2. Select 'Hunting' from the menu.
3. Choose a pre-built query or create a new one.
4. Run the query to search for suspicious activities.

## Validation
1. In the Azure portal, navigate to your Microsoft Sentinel workspace. 2. Under 'Threat management', select 'Hunting'. 3. Verify that the hunting query you set up appears in the list of queries. 4. Select the query and click 'Run Query' to confirm it executes without errors and returns results. 5. Check the 'Results' pane to ensure data is displayed as expected.

## Rollback
1. In the Azure portal, go to your Microsoft Sentinel workspace. 2. Under 'Threat management', select 'Hunting'. 3. If you created a new query, locate it in the list, select it, and click 'Delete' to remove it. 4. If you modified an existing query, revert any changes by editing the query back to its original state or by using the 'Reset to default' option if available. 5. Confirm the query list reflects the original state before the change.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/hunting>
