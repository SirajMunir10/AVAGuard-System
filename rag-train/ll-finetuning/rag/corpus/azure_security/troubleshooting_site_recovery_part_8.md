# Troubleshooting: Site Recovery

**Domain:** Azure
**Subdomain:** Site Recovery
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot app-consistent snapshot failures in Azure Site Recovery for Hyper-V VMs?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Hyper-V host with Azure Site Recovery

## Symptoms
- App-consistent snapshots are failing

## Error Codes
N/A

## Root Causes
1. VSS failing inside the VM
2. VSS failing inside the Hyper-V Host
3. Dynamic disks in the VM
4. iSCSI disk attached to the VM

## Remediation Steps
1. Check that the latest version of Integration services is installed and running. Run the following command from an elevated PowerShell prompt on the Hyper-V host: get-vm <vmName> | select Name, State, IntegrationServicesState
2. Check that VSS services are running and healthy: Sign in to the guest VM, open an admin command prompt, and run: Vssadmin list writers, Vssadmin list shadows, Vssadmin list providers
3. If writers are in a failed state, check the Application event log on the VM for VSS operation errors
4. Try restarting these services associated with the failed writer: Volume Shadow Copy, Azure Site Recovery VSS Provider
5. Wait for a couple of hours to see if app-consistent snapshots are generated successfully
6. As a last resort, try rebooting the VM
7. Check you don't have dynamic disks in the VM (check in Disk Management - diskmgmt.msc)
8. Check that you don't have an iSCSI disk attached to the VM

## Validation
1. On the Hyper-V host, run: get-vm <vmName> | select Name, State, IntegrationServicesState. Confirm IntegrationServicesState is 'OK'.
2. In the guest VM, run: vssadmin list writers. Verify all writers are in a 'Stable' state with no errors.
3. Run: vssadmin list shadows. Confirm at least one shadow copy exists.
4. Run: vssadmin list providers. Verify providers are listed.
5. Check Application event log for VSS-related errors; ensure no recent errors.
6. In Disk Management (diskmgmt.msc), verify no dynamic disks are present.
7. Confirm no iSCSI disks are attached to the VM.
8. Wait 2 hours and check Azure Site Recovery portal for successful app-consistent recovery points.

## Rollback
1. If integration services state is not 'OK', reinstall or update Integration Services from Hyper-V host.
2. If VSS writers are in a failed state, restart the Volume Shadow Copy service and Azure Site Recovery VSS Provider service on the guest VM.
3. If errors persist, reboot the guest VM.
4. If dynamic disks are found, convert them to basic disks (if possible) or exclude them from replication.
5. If iSCSI disks are attached, detach them or exclude them from replication.
6. If all else fails, contact Microsoft Support for further assistance.

## References
- <https://learn.microsoft.com/en-us/azure/site-recovery/hyper-v-azure-troubleshoot>
