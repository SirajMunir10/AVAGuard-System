# Implementation: Automation Rules

**Domain:** Sentinel
**Subdomain:** Automation Rules
**Incident Type:** Implementation

## Scenario / Query
How do I add automated responses to a Microsoft Sentinel analytics rule?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel analytics rule

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. In the Automated responses tab, review the automation rules displayed in the list
2. To add a response that applies to many or all rules, edit an existing rule
3. To add a response that applies only to this analytics rule, select Add new to create a new automation rule
4. See Automate threat response in Microsoft Sentinel with automation rules for more information

## Validation
1. Navigate to Microsoft Sentinel > Automation > Automation rules. 2. Locate the automation rule created or edited for the analytics rule. 3. Confirm the rule's conditions include the specific analytics rule name. 4. Verify the rule's actions (e.g., run playbook, change severity) are correctly configured. 5. Trigger a test incident matching the rule's conditions and confirm the automated response executes as expected.

## Rollback
1. Navigate to Microsoft Sentinel > Automation > Automation rules. 2. Select the automation rule that was added or edited. 3. If a new rule was added, delete it. 4. If an existing rule was edited, revert its conditions and actions to the previous state. 5. If the previous state is unknown, disable the rule to stop further automated responses.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-custom>
- <https://learn.microsoft.com/en-us/azure/sentinel/automate-threat-response-with-automation-rules>
