# Troubleshooting: Site Recovery

**Domain:** Azure
**Subdomain:** Site Recovery
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot replication issues for Hyper-V VMs in Azure Site Recovery?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Hyper-V host with Site Recovery replication

## Symptoms
- Replication failures or poor performance

## Error Codes
N/A

## Root Causes
1. iSCSI disk attached to the VM (unsupported)
2. Backup service not enabled in Hyper-V settings > Integration Services
3. Conflicts with apps taking VSS snapshots (e.g., Backup app taking snapshots when Site Recovery is scheduled)
4. High data churn rate on the VM

## Remediation Steps
1. Check that you don't have an iSCSI disk attached to the VM. This isn't supported.
2. Check that the Backup service is enabled. Verify that it's enabled in Hyper-V settings > Integration Services.
3. Make sure there are no conflicts with apps taking VSS snapshots. If multiple apps are trying to take VSS snapshots at the same time conflicts can occur. For example, if a Backup app is taking VSS snapshots when Site Recovery is scheduled by your replication policy to take a snapshot.
4. Check if the VM is experiencing a high churn rate: You can measure the daily data change rate for the guest VMs, using performance counters on Hyper-V host. To measure the data change rate, enable the following counter. Aggregate a sample of this value across the VM disks for 5-15 minutes, to get the VM churn. Category: 'Hyper-V Virtual Storage Device' Counter: 'Write Bytes / Sec'
5. Make sure that if you're using a Linux based server, then you have enabled app-consistency on it.
6. Run the Deployment Planner.
7. Review the recommendations for network and storage.

## Validation
1. On the Hyper-V host, open Hyper-V Manager, right-click the VM, select Settings, and under SCSI Controller confirm no iSCSI disks are attached. 2. In Hyper-V Manager, right-click the VM, select Settings, go to Integration Services, and verify that 'Backup (volume snapshot)' is checked. 3. Check the VM's event logs (Application and System) for VSS-related conflicts or errors during the scheduled replication window. 4. On the Hyper-V host, open Performance Monitor, add the counter 'Hyper-V Virtual Storage Device\Write Bytes / Sec' for the VM's virtual disks, and sample over 5-15 minutes to confirm the daily data change rate is within supported limits (typically <10 MB/s per disk). 5. If the VM is Linux-based, verify that app-consistency is enabled by checking the Azure Site Recovery Mobility Service configuration or the guest agent logs. 6. Run the Azure Site Recovery Deployment Planner for the Hyper-V environment and review its recommendations for network and storage.

## Rollback
1. If an iSCSI disk was removed, reattach it via the VM's SCSI Controller settings in Hyper-V Manager. 2. If the Backup service was disabled, re-enable it in Hyper-V Manager under Integration Services. 3. If VSS snapshot conflicts were resolved by rescheduling backup apps, revert the backup schedule to its original time. 4. If data churn was reduced by moving high-churn workloads, restore the original workload placement. 5. If app-consistency was disabled on a Linux VM, re-enable it according to the application's documentation. 6. If the Deployment Planner recommendations were applied (e.g., network or storage changes), revert those changes to the previous configuration.

## References
- <https://learn.microsoft.com/en-us/azure/site-recovery/hyper-v-azure-troubleshoot>
