# Troubleshooting: Endpoint Security

**Domain:** Intune
**Subdomain:** Endpoint Security
**Incident Type:** Troubleshooting

## Scenario / Query
How to diagnose BitLocker encryption policy not applying correctly on Windows 10 devices managed by Intune?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** BitLocker encryption policy

## Symptoms
- BitLocker encryption policy is not applying correctly

## Error Codes
N/A

## Root Causes
1. Windows OS version and edition may not support the configured settings
2. BitLocker CSP settings may have been introduced on specific versions of Windows and only work on certain editions

## Remediation Steps
1. Check whether the Windows OS version and edition supports the settings you configured
2. Create an MDM Diagnostic Report from the device at C:\Users\Public\Documents\MDMDiagnostics
3. Use the EntDMID (unique device ID for Intune enrollment) to search through the All Devices view in the Microsoft Intune admin center
4. Use the MDM Diagnostic Report to identify whether a policy has been successfully sent to the device with the settings the administrator configured
5. Use the BitLocker CSP documentation as a reference to decipher which settings have been picked up when syncing with the Intune service
6. Determine if the policy is targeting the device and identify what settings have been configured

## Validation
1. On the affected Windows 10 device, open an elevated PowerShell prompt and run: 'Get-WmiObject -Namespace root\cimv2\Security\MicrosoftVolumeEncryption -Class Win32_EncryptableVolume | Select-Object DriveLetter, ProtectionStatus'. Verify that ProtectionStatus is 1 (on) for the system drive.
2. On the device, navigate to C:\Users\Public\Documents\MDMDiagnostics and open the MDM Diagnostic Report HTML file. In the report, locate the 'Policies' section and confirm that the BitLocker policy (e.g., 'BitLocker CSP') appears with the expected settings and status 'Success'.
3. In the Microsoft Intune admin center, go to 'Devices' > 'All devices', search for the device using its EntDMID (found in the MDM Diagnostic Report under 'Device Information'). Select the device, then click 'Device configuration' and verify that the BitLocker policy is listed and shows a status of 'Succeeded' or 'Compliant'.

## Rollback
1. If the BitLocker policy is incorrectly applied, in the Microsoft Intune admin center, navigate to 'Endpoint security' > 'Disk encryption' and locate the BitLocker policy that is causing issues. Edit the policy and either remove the device assignment or modify the settings to a supported configuration (e.g., change 'Encryption method' to 'XTS-AES 128-bit' for Windows 10 version 1511 and later).
2. On the affected device, open an elevated command prompt and run: 'manage-bde -off C:' to decrypt the drive if encryption was applied incorrectly. Wait for decryption to complete (verify with 'manage-bde -status').
3. On the device, run 'SyncML' to force a sync with Intune: in Settings, go to 'Accounts' > 'Access work or school', select the MDM enrollment, and click 'Sync'. Alternatively, run 'Start-Process "ms-settings:workplace"' in PowerShell and click 'Sync'.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-bitlocker-policies>
