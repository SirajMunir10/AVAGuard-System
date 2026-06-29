# Incident Response: Microsoft Sentinel

**Domain:** Azure
**Subdomain:** Microsoft Sentinel
**Incident Type:** Incident Response

## Scenario / Query
A security operations team notices that a critical Microsoft Sentinel incident (e.g., account compromise) is not being automatically assigned to the correct analyst or group, causing delays in response. How can they configure automated incident assignment using Azure RBAC and Sentinel automation rules?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Microsoft Sentinel workspace with Log Analytics workspace, Azure RBAC roles (e.g., Microsoft Sentinel Responder), and Automation rules enabled.

## Symptoms
- Incidents remain unassigned or are assigned to the default 'Unassigned' state
- Manual assignment is required for every incident, causing delays
- Analysts are not receiving notifications for incidents they should handle

## Error Codes
N/A

## Root Causes
1. No automation rule configured to assign incidents based on criteria (e.g., severity, tactic, entity)
2. Missing or incorrect Azure RBAC role assignments for analysts (e.g., not granted 'Microsoft Sentinel Responder' role)
3. Automation rules are disabled or not ordered correctly in the Sentinel workspace

## Remediation Steps
1. 1. Ensure analysts have the 'Microsoft Sentinel Responder' role assigned at the resource group or subscription level (see Microsoft documentation).
2. 2. In Microsoft Sentinel, navigate to 'Automation' > 'Automation rules' and create a new rule.
3. 3. Set conditions (e.g., 'When incident is created' and 'Severity equals High') and actions (e.g., 'Assign incident to' a specific user or group).
4. 4. Order the automation rule appropriately (rules are processed in order; ensure this rule is above any conflicting rules).
5. 5. Save and enable the rule. Test by creating a test incident matching the conditions.

## Validation
Create a test incident in Sentinel that matches the rule conditions. Verify that the incident is automatically assigned to the designated analyst or group within a few minutes.

## Rollback
Disable or delete the automation rule. Reassign any incidents manually if needed. Remove RBAC role assignments only if they were added solely for this purpose and are no longer required.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/automate-incident-handling-with-automation-rules>
- <https://learn.microsoft.com/en-us/azure/sentinel/roles>
