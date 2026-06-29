# Troubleshooting: Hybrid Identity (InvalidHardMatch)

**Domain:** Entra ID
**Subdomain:** Hybrid Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve InvalidHardMatch error when the target Microsoft Entra object has privileged roles assigned?

## Environment Context
- **Tenant Type:** Microsoft Entra ID with hybrid identity
- **Configuration:** Microsoft Entra Connect synchronization

## Symptoms
- InvalidHardMatch error during synchronization

## Error Codes
- `InvalidHardMatch`

## Root Causes
1. Target Microsoft Entra object has privileged roles assigned

## Remediation Steps
1. Restore the user object from the Microsoft Entra ID Recycle Bin if soft-deleted
2. Remove all administrative roles from the Microsoft Entra user object
3. Ensure the OnPremisesImmutableId attribute is properly set to facilitate hard match
4. Allow Microsoft Entra Connect to perform the synchronization and complete the hard match operation
5. After successful synchronization, reassign the administrative roles to the user

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-sync-errors>
