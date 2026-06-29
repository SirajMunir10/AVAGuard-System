# Implementation: Analytics Rules

**Domain:** Sentinel
**Subdomain:** Analytics Rules
**Incident Type:** Implementation

## Scenario / Query
How do I create a custom analytics rule from scratch in Microsoft Sentinel when the built-in templates do not meet my specific detection needs?

## Environment Context
- **Tenant Type:** Microsoft Sentinel in Azure portal or Microsoft Defender portal
- **Configuration:** Analytics rule wizard

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Access the analytics rule wizard in either the Azure portal or the Defender portal.
2. Use the wizard to create a rule from scratch, customizing it to fit your specific scenarios.

## Validation
1. In the Azure portal or Microsoft Defender portal, navigate to Microsoft Sentinel > Analytics > Active rules. Confirm the newly created custom analytics rule is listed with the expected name, status (Enabled/Disabled), and severity. 2. Select the rule and review its configuration: ensure the rule query, entity mappings, alert details, and incident settings match the intended custom detection logic. 3. Optionally, run the rule query manually in the Log Analytics workspace to verify it returns the expected results. 4. If the rule is enabled, check that it is generating alerts or incidents as designed by reviewing the Incidents or Alerts blade for any triggered instances.

## Rollback
1. In the Azure portal or Microsoft Defender portal, navigate to Microsoft Sentinel > Analytics > Active rules. 2. Locate the custom analytics rule you created. 3. Select the rule and choose 'Delete' from the context menu or the command bar to remove it entirely. 4. If the rule was enabled and you prefer to disable it instead of deleting, select the rule and click 'Disable' to stop it from running. 5. Confirm the rule no longer appears in the Active rules list or is shown as Disabled, as appropriate.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-custom>
