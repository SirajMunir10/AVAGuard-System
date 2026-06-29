# Implementation: Analytics

**Domain:** Sentinel
**Subdomain:** Analytics
**Incident Type:** Implementation

## Scenario / Query
How do I enable, disable, or delete a custom scheduled rule in Microsoft Sentinel?

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
4. From this list, you can enable, disable, or delete each rule.

## Validation
1. Navigate to the Microsoft Sentinel workspace in the Azure portal. 2. Under 'Configuration', select 'Analytics'. 3. On the 'Active rules' tab, locate the custom scheduled rule in the table. 4. Verify the rule's status (Enabled/Disabled) matches the intended action. 5. If the rule was enabled, confirm it appears in the 'Active rules' list with a green checkmark. 6. If the rule was disabled, confirm it appears with a gray icon. 7. If the rule was deleted, confirm it no longer appears in the 'Active rules' list.

## Rollback
1. Navigate to the Microsoft Sentinel workspace in the Azure portal. 2. Under 'Configuration', select 'Analytics'. 3. On the 'Active rules' tab, locate the custom scheduled rule. 4. To re-enable a disabled rule, select it and click 'Enable'. 5. To re-disable an enabled rule, select it and click 'Disable'. 6. To restore a deleted rule, you must recreate it from scratch using the original rule configuration (e.g., query, schedule, alert details). 7. If the rule was deleted and no backup exists, consider using Azure Resource Graph or Azure CLI to check for recent changes or redeploy from a template if available.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-custom>
