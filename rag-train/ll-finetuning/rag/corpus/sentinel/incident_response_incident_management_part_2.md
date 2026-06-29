# Incident Response: Incident Management

**Domain:** Sentinel
**Subdomain:** Incident Management
**Incident Type:** Incident Response

## Scenario / Query
How do I close an incident in Microsoft Sentinel after investigation?

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
1. Set the incident's status to Closed.
2. Select a classification from the drop-down list: True Positive - suspicious activity, Benign Positive - suspicious but expected, False Positive - incorrect alert logic, False Positive - incorrect data, Undetermined.
3. Add descriptive text in the Comment field.
4. Select Apply to close the incident.

## Validation
1. In the Microsoft Sentinel workspace, navigate to 'Incidents' and verify the incident list no longer shows the closed incident in the 'New' or 'Active' status. 2. Use the following KQL query in the Log Analytics workspace to confirm the incident's status change: SecurityIncident | where IncidentNumber == "<IncidentNumber>" | project IncidentNumber, Status, Classification, ClassificationComment, TimeGenerated. 3. Check the 'AuditLogs' table for the corresponding 'Close incident' activity: AuditLogs | where OperationName == "Close incident" and TargetResources has "<IncidentNumber>".

## Rollback
1. In the Microsoft Sentinel workspace, navigate to 'Incidents' and locate the closed incident using the 'Search' or filter by 'Closed' status. 2. Select the incident and click 'Reopen incident' to revert its status to 'Active'. 3. If the incident was incorrectly classified, update the classification and comment fields as needed. 4. Verify the incident appears in the 'Active' incidents list and retains its original investigation details.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/investigate-cases>
