# Troubleshooting: Site Recovery

**Domain:** Azure
**Subdomain:** Site Recovery
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot initial and ongoing replication issues for Hyper-V to Azure disaster recovery?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Hyper-V replication with or without VMM

## Symptoms
- VM health status is critical in Hyper-V Manager console
- Replication is paused

## Error Codes
N/A

## Root Causes
1. Outdated Site Recovery services
2. Replication paused
3. Required services not running
4. Connectivity issues between Hyper-V server and Azure
5. Performance issues

## Remediation Steps
1. Make sure you're running the latest version of Site Recovery services
2. Check the VM health status in the Hyper-V Manager console. If it's critical, right-click the VM > Replication > View Replication Health. If replication is paused, select Resume Replication
3. Check that required services are running. If they aren't, restart them. If replicating Hyper-V without VMM, check that these services are running on the Hyper-V host: Virtual Machine Management service, Microsoft Azure Recovery Services Agent service, Microsoft Azure Site Recovery service, WMI Provider Host service. If replicating with VMM, check that these services are running: On the Hyper-V host, check that the Virtual Machine Management service, the Microsoft Azure Recovery Services Agent, and the WMI Provider Host service are running. On the VMM server, ensure that the System Center Virtual Machine Manager Service is running
4. Check connectivity between the Hyper-V server and Azure. To check connectivity, open Task Manager on the Hyper V host. On the Performance tab, select Open Resource Monitor. On the Network tab > Process with Network Activity, check whether cbengine.exe is actively sending large volumes (Mbs) of data. Check if the Hyper-V hosts can connect to the Azure storage blob URL. To check if the hosts can connect, select and check cbengine.exe. View TCP Connections to verify connectivity from the host to the Azure storage blob
5. Check performance issues, as described in the next section

## Validation
1. Verify the Site Recovery services version: On the Hyper-V host, open the Azure Site Recovery agent UI and confirm the version matches the latest listed in the Azure portal. 2. Check VM health: In Hyper-V Manager, right-click the VM > Replication > View Replication Health. Confirm the status is 'Healthy' and replication is not paused. 3. Ensure required services are running: Run `Get-Service -Name 'Virtual Machine Management','Microsoft Azure Recovery Services Agent','Microsoft Azure Site Recovery','WMI Provider Host'` (without VMM) or `Get-Service -Name 'Virtual Machine Management','Microsoft Azure Recovery Services Agent','WMI Provider Host'` on Hyper-V host and `Get-Service -Name 'System Center Virtual Machine Manager Service'` on VMM server (with VMM). All should show 'Running'. 4. Test connectivity: Open Resource Monitor on Hyper-V host, go to Network tab, and check that cbengine.exe shows active TCP connections to the Azure storage blob URL (e.g., *.blob.core.windows.net). 5. Confirm no performance issues: Review the next section of the troubleshooting guide for performance checks.

## Rollback
1. If validation fails after updating services, revert to the previous version of Site Recovery services using the installer from the Azure portal or a backup. 2. If replication was resumed but issues persist, pause replication again: In Hyper-V Manager, right-click the VM > Replication > Pause Replication. 3. If services were restarted and cause instability, stop and set them to their original startup type: Use `Set-Service -Name '<ServiceName>' -StartupType <OriginalType>` and `Stop-Service -Name '<ServiceName>'`. 4. If connectivity changes were made (e.g., firewall rules), restore previous firewall rules or network settings. 5. If performance tuning was applied, revert any changes to resource allocation or throttling settings.

## References
- <https://learn.microsoft.com/en-us/azure/site-recovery/hyper-v-azure-troubleshoot>
