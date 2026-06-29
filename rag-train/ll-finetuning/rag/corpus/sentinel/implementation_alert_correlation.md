# Implementation: Alert Correlation

**Domain:** Sentinel
**Subdomain:** Alert Correlation
**Incident Type:** Implementation

## Scenario / Query
How do I configure automated response after setting alert grouping in the Defender portal?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** Alert rule creation wizard in Defender portal or Azure portal

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select Next: Automated response
2. Defender portal
3. Azure portal

## Validation
1. In the Microsoft Defender portal (https://security.microsoft.com) or Azure portal (https://portal.azure.com), navigate to Microsoft Sentinel > your workspace > Analytics. 2. Locate the alert rule you configured with alert grouping and automated response. 3. Select the rule and click 'Edit'. 4. In the 'Automated response' tab, verify that the desired automation rule (e.g., run a playbook, trigger a logic app) is listed and enabled. 5. Optionally, trigger a test alert that meets the rule criteria and confirm that the automated response executes as expected (e.g., check the playbook run history in Logic Apps).

## Rollback
1. In the Microsoft Defender portal or Azure portal, navigate to Microsoft Sentinel > your workspace > Analytics. 2. Locate the alert rule with the automated response you want to remove or modify. 3. Select the rule and click 'Edit'. 4. In the 'Automated response' tab, either disable the automation rule by toggling it off, or remove it by clicking the delete icon. 5. Click 'Review and create' then 'Save' to apply the changes. 6. If the entire rule needs to be reverted, delete the rule and recreate it from a backup of the original configuration.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-custom>
