# Troubleshooting: Site Recovery

**Domain:** Azure
**Subdomain:** Site Recovery
**Incident Type:** Troubleshooting

## Scenario / Query
How to check replication health and resume paused replication for Hyper-V VMs in Azure Site Recovery?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** Hyper-V host configured in Site Recovery

## Symptoms
- Replication is paused

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Connect to the on-premises Hyper-V Manager console, select the VM, and verify health.
2. Select View Replication Health to see the details.
3. If replication is paused, right-click the VM > Replication > Resume replication.

## Validation
1. Connect to the on-premises Hyper-V Manager console. 2. Select the virtual machine. 3. Click 'View Replication Health' in the right-click menu or the details pane. 4. Confirm that the replication health status shows 'Healthy' and the replication state is 'Replicating' (not 'Paused'). 5. Optionally, run the PowerShell cmdlet: Get-VMReplication -VMName '<VMName>' | fl State,Health,LastReplicationTime to verify State is 'Replicating' and Health is 'Normal'.

## Rollback
1. Connect to the on-premises Hyper-V Manager console. 2. Select the virtual machine. 3. Right-click the VM, select 'Replication' > 'Pause replication'. 4. Confirm the pause when prompted. 5. Verify the replication state shows 'Paused' in the Replication Health dialog.

## References
- <https://learn.microsoft.com/en-us/azure/site-recovery/hyper-v-azure-troubleshoot>
