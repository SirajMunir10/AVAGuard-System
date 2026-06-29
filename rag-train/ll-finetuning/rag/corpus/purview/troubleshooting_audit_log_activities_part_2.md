# Troubleshooting: Audit Log Activities (ResultStatus.Failure)

**Domain:** Purview
**Subdomain:** Audit Log Activities
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot failed member removal from a roster in Purview audit logs?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Purview audit log enabled

## Symptoms
- Remove operation for a roster member returns ResultStatus.Failure or ResultStatus.AuthorizationFailure
- MemberIds field contains the list of member IDs attempted

## Error Codes
- `ResultStatus.Failure`
- `ResultStatus.AuthorizationFailure`

## Root Causes
1. User or app lacks permissions to remove members from the roster
2. Member IDs may be invalid or already removed

## Remediation Steps
1. Check the audit log for the RosterMemberDeleted operation and verify the ResultStatus
2. If AuthorizationFailure, review permissions for the user or app performing the removal
3. If Failure, verify the member IDs in MemberIds are valid and exist in the roster

## Validation
Confirm that subsequent remove operations return ResultStatus.Success

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
