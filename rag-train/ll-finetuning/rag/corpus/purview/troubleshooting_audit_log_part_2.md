# Troubleshooting: Audit Log (ResultStatus.Failure)

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify failed goal, plan, or task creation operations in Microsoft Planner audit logs?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- GoalCreated, PlanCreated, or TaskCreated operations show ResultStatus.Failure or ResultStatus.AuthorizationFailure

## Error Codes
- `ResultStatus.Failure`
- `ResultStatus.AuthorizationFailure`

## Root Causes
1. Failed creation results in ObjectId being null and PlanId being null for GoalCreated and TaskCreated
2. Failed creation results in ObjectId being null, ContainerType being ContainerType.Invalid, and ContainerId being null for PlanCreated

## Remediation Steps
1. Check the ObjectId and PlanId fields in audit records for GoalCreated and TaskCreated failures
2. Check the ObjectId, ContainerType, and ContainerId fields in audit records for PlanCreated failures

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
