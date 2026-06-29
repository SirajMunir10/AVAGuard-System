# Incident Response: Incident Response

**Domain:** Sentinel
**Subdomain:** Incident Response
**Incident Type:** Incident Response

## Scenario / Query
A security analyst needs to create a custom analytics rule in Microsoft Sentinel to detect when a user account is created and then added to a privileged role within 10 minutes, indicating a potential privilege escalation attack. What KQL query and rule configuration should be used?

## Environment Context
- **Tenant Type:** Azure AD tenant with Microsoft Sentinel enabled
- **Configuration:** Sentinel workspace connected to Azure AD audit logs and Azure Activity logs

## Symptoms
- User account creation followed by immediate role assignment
- Multiple accounts created in a short time span
- Accounts added to Global Administrator or Privileged Role Administrator roles

## Error Codes
N/A

## Root Causes
1. No detection rule for rapid account creation and privilege escalation
2. Insufficient monitoring of Azure AD audit logs for suspicious sequences

## Remediation Steps
1. Create a custom analytics rule in Microsoft Sentinel using the following KQL query:
```kusto
let threshold = 10m;
AuditLogs
| where OperationName == "Add user"
| project UserCreationTime = TimeGenerated, TargetUser = TargetResources[0].id, UserPrincipalName = TargetResources[0].userPrincipalName
| join kind=inner (
    AuditLogs
    | where OperationName == "Add member to role"
    | project RoleAdditionTime = TimeGenerated, TargetUser = TargetResources[0].id, Role = TargetResources[0].displayName
) on TargetUser
| where RoleAdditionTime between (UserCreationTime .. (UserCreationTime + threshold))
| project TimeGenerated = RoleAdditionTime, TargetUser, UserPrincipalName, Role, UserCreationTime, RoleAdditionTime
```
2. Set the rule to run every 5 minutes and look back 1 hour
3. Configure the rule to generate an incident of severity High
4. Enable the rule and map the entities (Account, Azure Resource) as appropriate

## Validation
After deploying the rule, simulate a test by creating a new user and immediately assigning them to a privileged role. Verify that an incident is generated within 5 minutes.

## Rollback
Disable or delete the custom analytics rule in the Sentinel Analytics blade. No other rollback is required.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-custom>
- <https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/auditlogs>
