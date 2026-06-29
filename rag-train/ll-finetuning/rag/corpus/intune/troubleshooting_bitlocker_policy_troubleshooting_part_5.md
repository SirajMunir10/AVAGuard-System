# Troubleshooting: BitLocker policy troubleshooting

**Domain:** Intune
**Subdomain:** BitLocker policy troubleshooting
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot BitLocker encryption failures in Intune using event logs?

## Environment Context
- **Tenant Type:** Intune-managed Windows devices
- **Configuration:** BitLocker policies via MDM

## Symptoms
- BitLocker encryption fails silently
- Silent encryption not enabled

## Error Codes
N/A

## Root Causes
1. Missing hardware or software prerequisites such as TPM or WinRE
2. Conflicting Group Policy settings
3. TPM not available
4. Un-Allowed DMA capable bus/device(s) detected

## Remediation Steps
1. Investigate the BitLocker-API management event log at: Event Viewer > Applications and Service Logs > Microsoft > Windows > BitLocker-API
2. For conflicting Group Policy settings: Configure the compatible TPM startup PIN to Blocked
3. Set the PIN and TPM startup key to Blocked if silent encryption is required
4. For TPM not available: Ensure there is a TPM available on the device and check its status via TPM.msc or the PowerShell cmdlet get-tpm
5. For Un-Allowed DMA capable bus/device(s) detected: Verify with OEM that the device has no external DMA ports, then add the device to the allowed list (only if it is an internal DMA interface/bus)

## Validation
1. Open Event Viewer and navigate to Applications and Service Logs > Microsoft > Windows > BitLocker-API. Check for any recent error events (Event IDs 845, 846, 847, 848, 851, 852, 853, 854) that indicate encryption failures. 2. Run 'manage-bde -status' on the affected device to confirm the drive encryption status shows 'Fully Encrypted' or 'Encryption In Progress' as expected. 3. If silent encryption was the goal, verify that no PIN or startup key prompt appears during boot. 4. For TPM issues, run 'Get-Tpm' in PowerShell and confirm that 'TpmReady' returns True and 'TpmEnabled' returns True. 5. For DMA conflicts, check the BitLocker-API event log for Event ID 845 with details about un-allowed DMA devices; then verify that the device's DMA policy is correctly configured (e.g., via 'Get-BitLockerConfiguration' or registry check under 'HKLM\SOFTWARE\Policies\Microsoft\FVE\' for 'DisableDMA' or 'EnableDMAProtection').

## Rollback
1. If conflicting Group Policy settings were changed (e.g., setting TPM startup PIN to Blocked), revert the policy to 'Not Configured' or 'Allowed' in Intune or local Group Policy. 2. If a device was added to the allowed DMA list, remove the entry from the registry key 'HKLM\SOFTWARE\Policies\Microsoft\FVE\AllowedDmaDevices' or revert the Intune policy that added it. 3. If TPM was enabled or cleared during troubleshooting, restore the original TPM state using 'Clear-Tpm' (only if previously cleared) or re-enable TPM in BIOS if it was disabled. 4. If BitLocker was manually suspended or disabled, re-enable it via 'manage-bde -on C:' or reapply the Intune BitLocker policy. 5. Restore any modified BitLocker-API event log settings (e.g., log size or retention) to their original values.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-bitlocker-policies>
