# Troubleshooting: Incident Management

**Domain:** Sentinel
**Subdomain:** Incident Management
**Incident Type:** Troubleshooting

## Scenario / Query
Why are incident comments being truncated or missing from advanced search results in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** SecurityIncident table in Log Analytics

## Symptoms
- Comments (starting with the earliest) are truncated in advanced search results
- Comments may not appear in advanced search results

## Error Codes
N/A

## Root Causes
1. The size limit of a single incident record in the SecurityIncident table in Log Analytics is 64 KB. If this limit is exceeded, comments (starting with the earliest) will be truncated.

## Remediation Steps
1. Reduce the number or size of comments per incident to stay within the 64 KB limit for the SecurityIncident table in Log Analytics.
2. Note that the actual incident records in the incidents database are not affected.

## Validation
1. Run a KQL query in the Log Analytics workspace to check the size of incident records: SecurityIncident | where TimeGenerated > ago(1h) | extend RecordSize = sizeof(*) | project RecordSize, IncidentNumber, Title, Comments. 2. Verify that no record exceeds 64 KB: SecurityIncident | where sizeof(*) > 64000 | count. 3. Confirm that comments are no longer truncated by searching for a known incident with many comments: SecurityIncident | where IncidentNumber == '<IncidentNumber>' | project Comments. 4. Check that the incident comments in the full incident details (via the Sentinel portal) remain intact and match the expected content.

## Rollback
1. If the remediation (reducing comments) causes loss of critical context, restore the original comments from a backup or by re-entering them via the Sentinel portal or API. 2. To revert any changes made to the Log Analytics workspace, ensure no data was deleted; if comments were removed, re-add them using the Azure Sentinel API: PUT https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/providers/Microsoft.SecurityInsights/incidents/{incidentId}/comments/{commentId}?api-version=2023-02-01-preview. 3. If the incident record size still exceeds 64 KB after rollback, consider splitting comments across multiple incidents or using external storage for lengthy notes.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/investigate-cases>
