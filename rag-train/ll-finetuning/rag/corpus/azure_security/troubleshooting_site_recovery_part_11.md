# Troubleshooting: Site Recovery

**Domain:** Azure
**Subdomain:** Site Recovery
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve Hyper-V Volume Shadow Copy Requestor connection failure due to version mismatch in Azure Site Recovery?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Hyper-V Volume Shadow Copy Requestor failed to connect to virtual machine <./VMname> because the version does not match the version expected by Hyper-V

## Error Codes
N/A

## Root Causes
1. Version mismatch between Hyper-V and the virtual machine

## Remediation Steps
1. Check if the latest Windows updates are installed
2. Upgrade to the latest version of Integration Services

## Validation
1. On the Hyper-V host, run: Get-WindowsUpdate -ComputerName <HyperVHost> | Where-Object {$_.IsInstalled -eq $false} to verify all critical Windows updates are installed.
2. On the virtual machine, run: Get-WmiObject -Class Win32_Product | Where-Object {$_.Name -like '*Integration Services*'} to confirm the installed Integration Services version.
3. Compare the Integration Services version on the VM with the version expected by Hyper-V by checking the Hyper-V host's Integration Services version via: Get-VMHostSupportedVersion.
4. Initiate a test failover in Azure Site Recovery and verify that the Volume Shadow Copy Requestor connects successfully without version mismatch errors.

## Rollback
1. If the VM becomes unstable after upgrading Integration Services, uninstall the latest Integration Services update from the VM via Control Panel > Programs and Features, then reinstall the previous known-good version from the Hyper-V host's installation media.
2. If Windows updates cause issues, use the Windows Update standalone installer (wusa.exe /uninstall /kb:<KBNumber>) to remove the problematic update from the Hyper-V host.
3. Restore the VM from a recent checkpoint or backup if the VM fails to start after changes.
4. Re-run the test failover to confirm the original error returns, indicating successful rollback.

## References
- <https://learn.microsoft.com/en-us/azure/site-recovery/hyper-v-azure-troubleshoot>
