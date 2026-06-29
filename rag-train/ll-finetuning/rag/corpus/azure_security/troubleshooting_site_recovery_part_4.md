# Troubleshooting: Site Recovery

**Domain:** Azure
**Subdomain:** Site Recovery
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot enable protection issues for Hyper-V VMs in Azure Site Recovery?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** Hyper-V hosts and VMs, System Center Virtual Machine Manager (VMM) clouds

## Symptoms
- Issues when enabling protection for Hyper-V VMs

## Error Codes
N/A

## Root Causes
1. Hyper-V hosts or VMs do not meet requirements and prerequisites
2. Hyper-V servers in VMM clouds not prepared
3. Hyper-V Virtual Machine Management service not running on Hyper-V hosts
4. WMI not enabled or accessible on guest VM
5. Integration Services not running latest version on guest VM

## Remediation Steps
1. Check that your Hyper-V hosts and VMs meet all requirements and prerequisites
2. If Hyper-V servers are located in System Center Virtual Machine Manager (VMM) clouds, verify that you've prepared the VMM server
3. Check that the Hyper-V Virtual Machine Management service is running on Hyper-V hosts
4. Check for issues that appear in the Hyper-V-VMMS\Admin sign in to the VM. This log is located in Applications and Services Logs > Microsoft > Windows
5. On the guest VM, verify that WMI is enabled and accessible. Learn about basic WMI testing. Troubleshoot WMI. Troubleshoot problems with WMI scripts and services
6. On the guest VM, ensure that the latest version of Integration Services is running. Check that you have the latest version. Keep Integration Services up-to-date

## Validation
1. Verify that Hyper-V hosts and VMs meet all requirements and prerequisites as documented in the Azure Site Recovery support matrix.
2. If Hyper-V servers are in VMM clouds, confirm that the VMM server has been prepared for Azure Site Recovery (check VMM console for Site Recovery settings).
3. On each Hyper-V host, run `Get-Service -Name 'Hyper-V Virtual Machine Management'` and ensure the service status is 'Running'.
4. Check the Hyper-V-VMMS\Admin event log (Applications and Services Logs > Microsoft > Windows > Hyper-V-VMMS > Admin) for any errors or warnings.
5. On the guest VM, test WMI accessibility by running `wmic /node:"<VM_IP>" path Win32_ComputerSystem get Name` from the Hyper-V host or a management machine; ensure it returns the VM name without errors.
6. On the guest VM, verify Integration Services version by running `Get-WindowsFeature -Name Hyper-V` or checking the VM settings in Hyper-V Manager; ensure the version matches the latest available from Microsoft.

## Rollback
1. If validation fails due to unmet prerequisites, review the Azure Site Recovery support matrix and adjust the Hyper-V host or VM configuration accordingly (e.g., enable required features, update OS version).
2. If VMM server preparation is incomplete, follow the steps in 'Prepare VMM for Azure Site Recovery' documentation to complete the setup.
3. If the Hyper-V Virtual Machine Management service is not running, start it with `Start-Service -Name 'Hyper-V Virtual Machine Management'` and set its startup type to Automatic using `Set-Service -Name 'Hyper-V Virtual Machine Management' -StartupType Automatic`.
4. If errors are found in the Hyper-V-VMMS\Admin log, address each error per the log details (e.g., restart the service, check disk space, update Hyper-V).
5. If WMI is not accessible, enable WMI on the guest VM via Windows Firewall (allow inbound rule for 'Windows Management Instrumentation (WMI)') and ensure the 'Windows Management Instrumentation' service is running.
6. If Integration Services is outdated, download and install the latest Integration Services package from the Microsoft Download Center on the guest VM, then restart the VM.

## References
- <https://learn.microsoft.com/en-us/azure/site-recovery/hyper-v-azure-troubleshoot>
