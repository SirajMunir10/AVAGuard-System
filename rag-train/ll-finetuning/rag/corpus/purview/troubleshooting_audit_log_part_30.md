# Troubleshooting: Audit Log (ResultStatus.Failure)

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify failed plan copy operations in Microsoft Planner audit logs?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- Plan copy operation shows ResultStatus.Failure in audit log

## Error Codes
- `ResultStatus.Failure`

## Root Causes
1. Failed copy operation results in newPlanId being null, newContainerType being ContainerType.Invalid, and newContainerId being null

## Remediation Steps
1. Review the newPlanId, newContainerType, and newContainerId fields in the audit record to confirm failure

## Validation
Search the unified audit log for Planner activities with Operation 'CopyPlan' and ResultStatus 'Failure'. For each matching record, verify that the newPlanId field is null, newContainerType is 'ContainerType.Invalid', and newContainerId is null. Use the Search-UnifiedAuditLog cmdlet with parameters -Operations 'CopyPlan' -ResultSize 1000 and inspect the AuditData property. Confirm that no records show ResultStatus 'Success' for the same operation.

## Rollback
If the remediation (reviewing audit fields) does not resolve the issue, re-attempt the plan copy operation from the source plan. Ensure the source plan is not corrupted by checking its tasks, buckets, and details. If the copy fails again, contact Microsoft Support with the audit record IDs showing ResultStatus.Failure and the null fields. No automated rollback is available; manual re-copy is the only recovery action.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
