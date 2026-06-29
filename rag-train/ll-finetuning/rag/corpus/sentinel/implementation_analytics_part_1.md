# Implementation: Analytics

**Domain:** Sentinel
**Subdomain:** Analytics
**Incident Type:** Implementation

## Scenario / Query
How do I view the definition of a newly created custom scheduled rule in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace with Analytics enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to the main Analytics screen in Microsoft Sentinel.
2. Locate the table under the Active rules tab.
3. Find your custom rule of type 'Scheduled' in the table.

## Validation
1. Open the Azure portal and navigate to your Microsoft Sentinel workspace.
2. Under 'Configuration', select 'Analytics'.
3. On the 'Active rules' tab, locate the rule table.
4. In the 'Name' column, find the custom scheduled rule you created.
5. Click on the rule name to open its details pane.
6. Confirm the rule type is 'Scheduled' and verify the rule definition fields (e.g., rule query, frequency, alert threshold) match your intended configuration.

## Rollback
1. If the rule definition is incorrect or missing, delete the custom scheduled rule from the Analytics screen.
2. Re-create the rule using the correct parameters as documented in 'https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-custom'.
3. Alternatively, if the rule was created via API or script, re-run the original creation command with corrected parameters.
4. Verify the new rule appears in the 'Active rules' table with the expected definition.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-custom>
