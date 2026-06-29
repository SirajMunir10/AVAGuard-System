# Troubleshooting: Site Recovery (0x800700EA)

**Domain:** Azure
**Subdomain:** Site Recovery
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Hyper-V replication failures due to VSS snapshot generation errors in Azure Site Recovery?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Hyper-V failed to generate VSS snapshot set for virtual machine: More data is available. (0x800700EA)
- Replication operation for virtual machine failed: More data is available.

## Error Codes
- `0x800700EA`

## Root Causes
1. Backup operation is in progress
2. VM has dynamic disk enabled (not supported)

## Remediation Steps
1. Check if your VM has dynamic disk enabled. This isn't supported.

## Validation
1. Verify that the VM does not have dynamic disks: Run `Get-VM -Name <VMName> | Get-VMHardDiskDrive | Select-Object ControllerType, ControllerNumber, ControllerLocation, DiskNumber` and then `Get-Disk -Number <DiskNumber> | Select-Object Number, PartitionStyle, OperationalStatus, Size, FriendlyName` to confirm PartitionStyle is 'MBR' or 'GPT' (not 'RAW' or 'Dynamic').
2. Check that no backup operation is in progress: Run `Get-WBJob | Where-Object {$_.JobState -eq 'Running'}` and confirm no active backup jobs.
3. Verify replication health in Azure Site Recovery: In the Azure portal, navigate to Recovery Services vault > Replicated items, select the VM, and check the 'Health' and 'Latest recovery point' status to ensure replication is now successful.

## Rollback
1. If the VM uses dynamic disks and must be converted back, restore the VM from a known good backup that uses dynamic disks (if required).
2. If a backup operation was mistakenly stopped, restart the backup job: `Start-WBJob -Backup`.
3. If replication was disabled during troubleshooting, re-enable it: In the Azure portal, go to Recovery Services vault > Replicated items, select the VM, and click 'Enable replication' to reconfigure replication settings.

## References
- <https://learn.microsoft.com/en-us/azure/site-recovery/hyper-v-azure-troubleshoot>
