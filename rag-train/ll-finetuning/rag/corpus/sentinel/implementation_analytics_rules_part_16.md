# Implementation: Analytics Rules

**Domain:** Sentinel
**Subdomain:** Analytics Rules
**Incident Type:** Implementation

## Scenario / Query
How do I create a custom detection rule in Microsoft Sentinel to detect threats using KQL?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace with Log Analytics

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. In the Azure portal, navigate to your Microsoft Sentinel workspace.
2. Under Configuration, select Analytics.
3. Select Create and then Scheduled query rule.
4. Define the rule logic using Kusto Query Language (KQL).
5. Set the query scheduling and alert threshold.
6. Configure incident creation settings.
7. Review and create the rule.

## Validation
1. In the Azure portal, navigate to your Microsoft Sentinel workspace.
2. Under Configuration, select Analytics.
3. Locate the newly created custom rule in the list of active rules.
4. Select the rule and review the rule details to confirm the KQL query, scheduling, and incident settings match the intended configuration.
5. Optionally, run the query manually in the Log Analytics workspace to verify it returns expected results.
6. Check the rule's status to ensure it is enabled and not in a 'Failing' state.

## Rollback
1. In the Azure portal, navigate to your Microsoft Sentinel workspace.
2. Under Configuration, select Analytics.
3. Locate the custom rule you created.
4. Select the rule and choose 'Delete' from the top menu or context menu.
5. Confirm the deletion to remove the rule and revert to the previous state.
6. If the rule was created via ARM template or API, redeploy the previous version or delete the resource accordingly.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-custom>
