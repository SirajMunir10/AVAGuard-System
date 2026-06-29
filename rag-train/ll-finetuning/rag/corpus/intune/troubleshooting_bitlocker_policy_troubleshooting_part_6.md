# Troubleshooting: BitLocker policy troubleshooting

**Domain:** Intune
**Subdomain:** BitLocker policy troubleshooting
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify hardware-related TPM issues when troubleshooting BitLocker policies in Intune?

## Environment Context
- **Tenant Type:** Intune-managed Windows devices
- **Configuration:** BitLocker encryption policies

## Symptoms
- Hardware-related issues with TPM
- BitLocker policy failures possibly due to TPM problems

## Error Codes
N/A

## Root Causes
1. TPM hardware issues
2. Outdated TPM firmware

## Remediation Steps
1. Open Event Viewer by right-clicking on Start Menu and selecting Event Viewer
2. Navigate to Windows Logs > System
3. Filter on event sources TPMProvisioningService or TPM-WMI
4. Review errors from these sources to identify hardware-related TPM issues
5. Check with the OEM manufacturer for available firmware updates

## Validation
1. Open Event Viewer (eventvwr.msc).
2. Navigate to Windows Logs > System.
3. Apply a filter for event sources: TPMProvisioningService or TPM-WMI.
4. Confirm no new errors or warnings from these sources after remediation.
5. Run 'Get-Tpm' in PowerShell as Administrator and verify TpmReady = True, TpmEnabled = True.
6. In Intune, check the device's encryption status under Devices > Windows > Encryption report to confirm BitLocker policy compliance.

## Rollback
1. If TPM firmware update caused issues, contact OEM for rollback instructions (e.g., restore previous firmware version via OEM tool).
2. If TPM was cleared or disabled, re-enable TPM in BIOS/UEFI and re-provision: run 'Initialize-Tpm' in PowerShell as Administrator.
3. Reapply BitLocker policy in Intune by triggering a sync: from the device, go to Settings > Accounts > Access work or school > Info > Sync.
4. If errors persist, revert to previous BitLocker policy version via Intune portal: Devices > Configuration profiles > select profile > Properties > Settings and restore prior configuration.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-bitlocker-policies>
