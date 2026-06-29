# Incident Response: Microsoft Sentinel

**Domain:** Azure
**Subdomain:** Microsoft Sentinel
**Incident Type:** Incident Response

## Scenario / Query
An organization uses Microsoft Sentinel for incident response. A critical incident is created for a potential privilege escalation, but the assigned analyst cannot see the full incident details, including entities and alerts. What configuration change is needed to ensure the analyst has the correct permissions to view and triage the incident?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Microsoft Sentinel workspace with Azure RBAC; the analyst has Reader role on the resource group but cannot see incident entities.

## Symptoms
- Analyst assigned to a Sentinel incident sees only basic metadata (title, severity, status) but not the entities, alerts, or bookmarks associated with the incident.
- When opening the incident, the analyst receives a 'You do not have permission to view this data' message or sees empty entity fields.

## Error Codes
N/A

## Root Causes
1. The analyst has only the Reader role on the resource group containing the Log Analytics workspace, which does not grant read access to the security data (SecurityEvent, SigninLogs, etc.) stored in the workspace.
2. Microsoft Sentinel permissions require the Microsoft Sentinel Reader role (or higher) on the resource group that contains the workspace, not just the generic Reader role.

## Remediation Steps
1. Assign the Microsoft Sentinel Reader role to the analyst on the resource group that contains the Log Analytics workspace used by Sentinel. This role grants read access to incident data, entities, and alerts.
2. If the analyst also needs to respond to incidents (change status, assign, add comments), assign the Microsoft Sentinel Responder role instead.
3. Verify the assignment using Azure portal: navigate to the resource group â†’ Access control (IAM) â†’ Add role assignment â†’ select 'Microsoft Sentinel Reader' or 'Microsoft Sentinel Responder' â†’ select the analyst â†’ Review + assign.

## Validation
After the role assignment, the analyst should refresh the Sentinel incident page and confirm they can see all entities, alerts, and timeline details for the incident.

## Rollback
Remove the Microsoft Sentinel Reader or Responder role assignment from the analyst via the same IAM blade.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/roles>
