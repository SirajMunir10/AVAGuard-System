# Implementation: PostgreSQL

**Domain:** Azure
**Subdomain:** PostgreSQL
**Incident Type:** Implementation

## Scenario / Query
How do resource locks on a virtual network or subnet interfere with PostgreSQL server creation?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** PostgreSQL server in a virtual network with resource locks

## Symptoms
- Interference with network and Domain Name System operations during server creation

## Error Codes
N/A

## Root Causes
1. Resource locks (delete or read-only) at the virtual network or subnet level can interfere with network and DNS operations

## Remediation Steps
1. Remove any delete or read-only locks from your virtual network and all subnets before creating the server in a virtual network
2. Reapply the locks after the server is created

## Validation
1. Verify that no resource locks exist on the virtual network and all subnets: `az lock list --resource-group <resource-group-name> --resource-name <vnet-name> --resource-type Microsoft.Network/virtualNetworks` and `az lock list --resource-group <resource-group-name> --resource-name <subnet-name> --resource-type Microsoft.Network/virtualNetworks/subnets`. 2. Confirm the PostgreSQL server creation succeeds: `az postgres server create ...` (with appropriate parameters). 3. After creation, verify the server is in the desired virtual network/subnet: `az postgres server show --name <server-name> --resource-group <resource-group-name> --query "networkDelegation"`.

## Rollback
1. If server creation fails due to locks, remove any delete or read-only locks from the virtual network and all subnets: `az lock delete --resource-group <resource-group-name> --name <lock-name>` for each lock. 2. Retry the server creation. 3. After successful creation, reapply the original locks: `az lock create --resource-group <resource-group-name> --resource-name <vnet-name> --resource-type Microsoft.Network/virtualNetworks --lock-type <CanNotDelete|ReadOnly> --name <lock-name>` and similarly for each subnet.

## References
- <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources>
