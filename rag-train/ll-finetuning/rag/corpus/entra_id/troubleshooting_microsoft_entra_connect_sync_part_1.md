# Troubleshooting: Microsoft Entra Connect Sync (InvalidSoftMatch)

**Domain:** Entra ID
**Subdomain:** Microsoft Entra Connect Sync
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve InvalidSoftMatch synchronization errors in Microsoft Entra Connect when a hard match fails and a soft match finds an object with a different immutableId?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Microsoft Entra Connect sync engine using objectGUID for sourceAnchor

## Symptoms
- InvalidSoftMatch synchronization error in Microsoft Entra Connect
- Object fails to provision in Microsoft Entra ID
- Duplicate proxyAddresses or userPrincipalName values in on-premises Active Directory

## Error Codes
- `InvalidSoftMatch`

## Root Causes
1. Hard match fails to find any matching object
2. Soft match finds a matching object but that object has a different immutableId value than the incoming object's sourceAnchor
3. The matching object was synced from another object from on-premises Active Directory
4. The object to be soft-matched with has a value for the immutableId attribute
5. Two or more objects with the same value for the proxyAddresses attribute exist in on-premises Active Directory
6. Two or more objects with the same value for the userPrincipalName attribute exist in on-premises Active Directory
7. An object was added in on-premises Active Directory with the same value for the proxyAddresses attribute as that of an existing object in Microsoft Entra ID
8. An object was added in on-premises Active Directory with the same value for the userPrincipalName attribute as that of an account in Microsoft Entra ID
9. A synced account was moved from Forest A to Forest B, resulting in a different sourceAnchor value

## Remediation Steps
1. Fix the duplicate data in on-premises Active Directory for proxyAddresses or userPrincipalName attributes
2. Ensure the object to be soft-matched with does not have a value for the immutableId attribute

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-sync-errors>
