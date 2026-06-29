# Troubleshooting: Hybrid Identity

**Domain:** Entra ID
**Subdomain:** Hybrid Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve the Existing Admin Role Conflict error during Microsoft Entra Connect sync?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Microsoft Entra Connect sync with admin role assignments

## Symptoms
- Admin Role Conflict error during sync
- Quarantined object in the cloud

## Error Codes
N/A

## Root Causes
1. Microsoft Entra account (owner) has admin roles assigned, preventing soft-match

## Remediation Steps
1. Remove the Microsoft Entra account (owner) from all admin roles
2. Hard delete the quarantined object in the cloud
3. Wait for the next sync cycle to soft-match the on-premises user to the cloud account (because the cloud user is now no longer a Hybrid Identity Administrator)
4. Restore the role memberships for the owner after the soft match completes

## Validation
Assign the administrative role to the existing user object again after the soft match between the on-premises user object and the Microsoft Entra user object has finished

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-sync-errors>
