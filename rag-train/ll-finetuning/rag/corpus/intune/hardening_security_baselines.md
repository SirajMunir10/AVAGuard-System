# Hardening: Security Baselines

**Domain:** Intune
**Subdomain:** Security Baselines
**Incident Type:** Hardening

## Scenario / Query
What are the default security settings applied by the Security Baseline for Windows 10 and later in Intune?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Security Baseline for Windows 10 and later

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. The default configuration automatically enables BitLocker for removable drives.
2. The default configuration automatically requires a password to unlock a device.
3. The default configuration automatically disables basic authentication.

## Validation
1. In the Microsoft Intune admin center, navigate to 'Endpoint security' > 'Security baselines'. Select the 'Security Baseline for Windows 10 and later' profile assigned to the target devices. Review the settings under 'BitLocker' to confirm 'Encryption of removable drives' is set to 'Require'. Under 'Password', confirm 'Require password to unlock device' is set to 'Require'. Under 'Authentication', confirm 'Basic authentication' is set to 'Block'. 2. On a managed Windows 10 device, open the Event Viewer and navigate to 'Applications and Services Logs' > 'Microsoft' > 'Windows' > 'DeviceManagement-Enterprise-Diagnostics-Provider' > 'Admin'. Verify event ID 851 for successful policy application. 3. Run 'Get-BitLockerVolume -MountPoint $env:SystemDrive' in PowerShell as administrator to confirm BitLocker protection status. 4. Attempt to unlock the device without a password to verify the password requirement is enforced. 5. Attempt to use basic authentication in a supported app (e.g., Internet Explorer) to confirm it is blocked.

## Rollback
1. In the Microsoft Intune admin center, navigate to 'Endpoint security' > 'Security baselines'. Select the assigned baseline profile and click 'Properties'. Under 'Configuration settings', set 'Encryption of removable drives' to 'Not configured', 'Require password to unlock device' to 'Not configured', and 'Basic authentication' to 'Not configured' or 'Allow'. Click 'Review + save' to apply changes. 2. Alternatively, create a new custom baseline profile with the desired settings and assign it to the same device groups, ensuring it has a higher priority. 3. On affected devices, run 'gpupdate /force' from an elevated command prompt to force policy refresh. 4. For BitLocker, run 'Disable-BitLocker -MountPoint $env:SystemDrive' in PowerShell as administrator to decrypt the drive (if rollback requires disabling encryption). 5. Monitor the 'DeviceManagement-Enterprise-Diagnostics-Provider' Admin event log for event ID 851 confirming the updated policy application.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/security-baselines>
