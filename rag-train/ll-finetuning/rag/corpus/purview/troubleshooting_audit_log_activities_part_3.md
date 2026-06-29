# Troubleshooting: Audit Log Activities (ResultStatus.Failure)

**Domain:** Purview
**Subdomain:** Audit Log Activities
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot failed tenant settings updates in Purview audit logs?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Purview audit log enabled

## Symptoms
- Update operation for tenant settings returns ResultStatus.Failure or ResultStatus.AuthorizationFailure
- ObjectId field contains the original settings
- TenantSettings field contains the attempted organization settings

## Error Codes
- `ResultStatus.Failure`
- `ResultStatus.AuthorizationFailure`

## Root Causes
1. Organization admin lacks permissions to update tenant settings
2. Attempted settings may be invalid or conflict with existing policies

## Remediation Steps
1. Check the audit log for the TenantSettingsUpdated operation and verify the ResultStatus
2. If AuthorizationFailure, verify the admin has appropriate roles (e.g., Global Admin)
3. If Failure, compare ObjectId (original settings) with TenantSettings (attempted settings) to identify invalid changes

## Validation
Confirm that subsequent update operations return ResultStatus.Success

## Rollback
Revert to the original settings stored in ObjectId if the update failed

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
