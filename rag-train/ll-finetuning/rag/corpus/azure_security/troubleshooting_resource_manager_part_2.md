# Troubleshooting: Resource Manager

**Domain:** Azure
**Subdomain:** Resource Manager
**Incident Type:** Troubleshooting

## Scenario / Query
Why can't I create or delete management locks on Azure resources?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Management locks

## Symptoms
- Unable to create or delete management locks

## Error Codes
N/A

## Root Causes
1. Insufficient permissions: need Microsoft.Authorization/* or Microsoft.Authorization/locks/* actions

## Remediation Steps
1. Ensure the user has access to Microsoft.Authorization/* or Microsoft.Authorization/locks/* actions
2. Assign the user to the Owner role or the User Access Administrator role
3. Alternatively, assign a specialized built-in role that grants this access
4. Create a custom role with the required permissions: Microsoft.Authorization/* or Microsoft.Authorization/locks/*

## Validation
1. Run 'az role assignment list --assignee <userPrincipalName> --output table' to confirm the user has a role assignment that includes Microsoft.Authorization/* or Microsoft.Authorization/locks/* actions. 2. Attempt to create a management lock: 'az lock create --name testLock --lock-type CanNotDelete --resource-group <resourceGroupName>'. 3. Attempt to delete the management lock: 'az lock delete --name testLock --resource-group <resourceGroupName>'. 4. Verify no errors are returned and the lock operations succeed.

## Rollback
1. If the remediation assigned a custom role, remove the custom role assignment: 'az role assignment delete --assignee <userPrincipalName> --role <customRoleName> --resource-group <resourceGroupName>'. 2. If the remediation assigned the Owner or User Access Administrator role, remove that role assignment: 'az role assignment delete --assignee <userPrincipalName> --role "Owner" --resource-group <resourceGroupName>' (or "User Access Administrator"). 3. Verify the user can no longer create or delete locks: 'az lock create --name testLock --lock-type CanNotDelete --resource-group <resourceGroupName>' should fail with authorization error.

## References
- <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources>
