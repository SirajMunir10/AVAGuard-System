# Troubleshooting: Audit Log (ResultStatus.Failure)

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify and troubleshoot failed operations in Microsoft Planner audit logs?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- Audit log shows ResultStatus.Failure or ResultStatus.AuthorizationFailure for Planner operations

## Error Codes
- `ResultStatus.Failure`
- `ResultStatus.AuthorizationFailure`

## Root Causes
1. Failed operations may indicate permission issues or system errors

## Remediation Steps
1. Check the MemberIds field in audit records for RosterMemberAdded failures
2. Check the newPlanId, newContainerType, and newContainerId fields for Plan copy failures
3. Check the ObjectId and PlanId fields for GoalCreated, PlanCreated, TaskCreated failures
4. Check the ObjectId and MemberIds fields for RosterCreated failures

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
