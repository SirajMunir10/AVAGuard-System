# Troubleshooting: Site Recovery

**Domain:** Azure
**Subdomain:** Site Recovery
**Incident Type:** Troubleshooting

## Scenario / Query
How does a cannot-delete lock on a Virtual Machine protected by Site Recovery affect removal of protection or disabling replication?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Virtual Machine with cannot-delete lock and Site Recovery protection

## Symptoms
- Unable to remove certain resource links related to Site Recovery when removing protection or disabling replication

## Error Codes
N/A

## Root Causes
1. A cannot-delete lock prevents removal of resource links related to Site Recovery

## Remediation Steps
1. Remove the lock before disabling protection if you plan to protect the virtual machine again later
2. If the lock is not removed, follow certain steps to clean up the stale links before you can protect the virtual machine (see Troubleshoot Azure-to-Azure VM replication errors)

## Validation
1. Verify the VM's lock status: Run `az lock list --resource-group <ResourceGroupName> --resource-name <VMName> --resource-type Microsoft.Compute/virtualMachines --query "[?properties.level=='CannotDelete']"` and confirm no locks are returned.
2. Confirm Site Recovery links are removed: Run `az resource list --resource-group <ResourceGroupName> --query "[?contains(name, 'ASR') || contains(name, 'SiteRecovery')]"` and verify no stale Site Recovery resources exist.
3. Check replication status: Run `az site-recovery replication-protected-item list --fabric-name <FabricName> --protection-container <ContainerName> --query "[?friendlyName=='<VMName>']"` and confirm the VM is not listed.

## Rollback
1. Reapply the cannot-delete lock: Run `az lock create --lock-name CannotDeleteLock --lock-type CanNotDelete --resource-group <ResourceGroupName> --resource-name <VMName> --resource-type Microsoft.Compute/virtualMachines`.
2. Re-enable replication for the VM: Follow the steps in 'Enable replication for Azure VMs' at https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-how-to-enable-replication.
3. Verify replication is healthy: Run `az site-recovery replication-protected-item show --fabric-name <FabricName> --protection-container <ContainerName> --name <ProtectedItemName> --query "properties.providerSpecificDetails.healthErrors"` and confirm no errors.

## References
- <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources>
