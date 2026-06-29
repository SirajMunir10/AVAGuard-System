# Implementation: Analytics Rules

**Domain:** Sentinel
**Subdomain:** Analytics Rules
**Incident Type:** Implementation

## Scenario / Query
How do I configure a custom detection rule in Microsoft Sentinel with MITRE ATT&CK mapping and scheduling options?

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
1. Select from among the MITRE ATT&CK tactics and techniques presented in the drop-down list. You can make multiple selections.
2. Choose Enabled to have the rule run immediately upon creation, or at the specific date and time you choose to schedule it (currently in PREVIEW).
3. Choose Disabled to create the rule but not run it. Enable it later from your Active rules tab when you need it.
4. Select Next: Set rule logic.

## Validation
1. Navigate to the Microsoft Sentinel workspace in the Azure portal. 2. Go to Analytics > Active rules and confirm the custom rule appears in the list. 3. Select the rule and verify that the MITRE ATT&CK tactics and techniques displayed match the selections made during configuration. 4. Check the rule status: if it was set to Enabled, confirm it shows as 'Enabled' and has a non-zero run count; if set to Disabled, confirm it shows as 'Disabled'. 5. For a scheduled rule, review the rule details to ensure the schedule (frequency, period, start time) is correctly reflected.

## Rollback
1. In the Microsoft Sentinel workspace, navigate to Analytics > Active rules. 2. Locate the custom rule and select it. 3. Click 'Edit' to open the rule configuration. 4. In the 'Analytics rule creation wizard', go to the 'Set rule logic' tab and remove or adjust any MITRE ATT&CK mappings as needed. 5. On the 'Review and create' tab, set the rule status to 'Disabled' if it was enabled and causing issues. 6. Alternatively, delete the rule entirely by selecting 'Delete' from the rule's context menu. 7. If the rule was created via API or PowerShell, use the equivalent commands to disable or remove it (e.g., `Remove-AzSentinelAlertRule`).

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-custom>
