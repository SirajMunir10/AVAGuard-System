# Troubleshooting: Audit Log Activities (ResultStatus.Failure)

**Domain:** Purview
**Subdomain:** Audit Log Activities
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot failed read operations for goals, plans, tasks, or chat messages in Purview audit logs?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Purview audit log enabled

## Symptoms
- Read operation for a goal, plan, task, or chat message returns ResultStatus.Failure or ResultStatus.AuthorizationFailure
- PlanId is null for goal or task read failures
- MessageList is an empty string for chat message list query failures
- GoalList is an empty string for goal list query failures
- PlanList is an empty string for plan list query failures
- TaskList is an empty string for task list query failures
- ContainerType is ContainerType.Invalid and ContainerId is null for plan read failures

## Error Codes
- `ResultStatus.Failure`
- `ResultStatus.AuthorizationFailure`

## Root Causes
1. User or app lacks permissions to read the resource
2. Resource may not exist or has been deleted
3. Authorization failure due to policy restrictions

## Remediation Steps
1. Check the audit log for the specific operation and verify the ResultStatus
2. If ResultStatus is AuthorizationFailure, review user or app permissions for the resource
3. If ResultStatus is Failure, verify the resource exists and is accessible

## Validation
Confirm that subsequent read operations return ResultStatus.Success and non-null fields

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
