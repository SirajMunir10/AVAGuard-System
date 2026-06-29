# Troubleshooting: Site Recovery (Hyper-V failed to generate VSS snapshot set for virtual machine 'XYZ': The writer experienced a non-transient error)

**Domain:** Azure
**Subdomain:** Site Recovery
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot VSS snapshot failures for Hyper-V VMs in Azure Site Recovery?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Hyper-V host with Azure Site Recovery replication

## Symptoms
- App-consistent snapshot failures
- Hyper-V failed to generate VSS snapshot set for virtual machine 'XYZ': The writer experienced a non-transient error

## Error Codes
- `Hyper-V failed to generate VSS snapshot set for virtual machine 'XYZ': The writer experienced a non-transient error`

## Root Causes
1. VSS service unresponsive
2. Hyper-V Integration Services not installed on the VM
3. Backup (VSS) Integration Service not enabled
4. Integration Services VSS service/daemons not running or not in OK state

## Remediation Steps
1. On the Hyper-V host server, open the Hyper-V Admin event log in Event Viewer > Applications and Services Logs > Microsoft > Windows > Hyper-V > Admin and verify events indicating app-consistent snapshot failures.
2. Check that Hyper-V Integration Services is installed on the VM and that the Backup (VSS) Integration Service is enabled.
3. Ensure the Integration Services VSS service/daemons are running on the guest and are in an OK state using the PowerShell command: Get-VMIntegrationService -VMName <VMName> -Name VSS
4. Alternatively, log into the guest VM to verify the Backup/VSS Integration Services are running and healthy.
5. Restart the Backup/VSS Integration Services on the VM and the Hyper-V Volume Shadow Copy requester service on the Hyper-V host server.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/site-recovery/hyper-v-azure-troubleshoot>
