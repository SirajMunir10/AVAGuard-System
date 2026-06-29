# Incident Response: Incident Response

**Domain:** Sentinel
**Subdomain:** Incident Response
**Incident Type:** Incident Response

## Scenario / Query
A security analyst in a Microsoft Sentinel environment receives an incident of type 'Malicious SQL login detected' but cannot find any related alerts or entities. How should the analyst triage and investigate this incident using built-in Sentinel features?

## Environment Context
- **Tenant Type:** Enterprise (Azure AD + hybrid on-premises SQL Server)
- **Configuration:** Microsoft Sentinel workspace with the 'SQL Server' data connector enabled and 'Azure SQL Database' analytics rule 'Create incidents based on Azure SQL Database threat detection' active.

## Symptoms
- Incident appears in Sentinel with severity Medium, title 'Malicious SQL login detected'.
- No alerts are listed under the incident's 'Alerts' tab.
- No entities (IP, user, host) are populated in the incident.
- The incident's 'Events' timeline is empty.

## Error Codes
N/A

## Root Causes
1. The analytics rule that generated the incident may have been triggered by a raw event that did not map to any known entity schema.
2. The data connector for SQL Server may not be ingesting the necessary fields (e.g., ClientIP, UserName) required for entity mapping.
3. The incident was created by a scheduled rule that uses a KQL query that does not produce entity mapping output.

## Remediation Steps
1. Open the incident and review the 'Description' and 'Tactics and Techniques' fields for context.
2. Use the 'Investigation' graph to manually search for related events: navigate to the 'Logs' blade and run a KQL query against the 'SQLSecurityAuditEvents' table filtered by the incident's time range.
3. If no events appear, verify that the 'SQL Server' data connector is properly configured and sending data to the Log Analytics workspace used by Sentinel.
4. Review the analytics rule that created the incident: navigate to 'Analytics' > 'Active rules', find the rule, and examine its 'Rule query' to understand which events trigger it.
5. If the rule uses a custom query, modify it to include entity mapping (e.g., '| extend AccountCustomEntity = UserName, IPCustomEntity = ClientIP') to enrich future incidents.
6. Document the findings in the incident's 'Comments' and update the incident status to 'Closed' with classification 'FalsePositive' if no malicious activity is confirmed.

## Validation
After applying the remediation, create a test incident by simulating a failed SQL login from a known test IP. Verify that the new incident contains the expected alert and entity data (IP, user).

## Rollback
If the rule modification causes performance issues or false positives, revert the rule query to its original version by restoring from the rule's 'History' tab or by using the 'Revert' option in the rule editor.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/investigate-incidents>
- <https://learn.microsoft.com/en-us/azure/sentinel/map-data-fields-to-entities>
