# Governance: Device Configuration â€“ Tamper Protection

**Domain:** Defender for Endpoint
**Subdomain:** Device Configuration â€“ Tamper Protection
**Incident Type:** Governance

## Scenario / Query
A security administrator notices that Tamper Protection is not enforced on several Windows 10 devices enrolled in Microsoft Defender for Endpoint, despite a tenant-wide policy being set to 'On'. How can the administrator verify and enforce Tamper Protection across the organization using Microsoft Intune and the Microsoft 365 Defender portal?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Microsoft Defender for Endpoint Plan 2
- **Configuration:** Tamper Protection tenant-wide setting is enabled; devices are managed by Microsoft Intune with Windows 10 version 20H2 or later

## Symptoms
- Tamper Protection shows 'Off' on some devices in the Microsoft 365 Defender portal under Settings > Endpoints > Advanced features
- Users or local administrators can disable real-time protection or other Defender antivirus settings
- Security baselines report that Tamper Protection is not applied on targeted devices

## Error Codes
N/A

## Root Causes
1. Tamper Protection tenant-wide setting was enabled after some devices had already been configured with a conflicting Intune policy that disables Tamper Protection
2. Devices are not properly enrolled in Intune or do not have the required Windows version (20H2 or later) to support Tamper Protection
3. Group Policy Object (GPO) overrides the Intune-managed Tamper Protection setting

## Remediation Steps
1. In the Microsoft 365 Defender portal, navigate to Settings > Endpoints > Advanced features and verify that Tamper Protection is set to 'On'
2. In Microsoft Intune, create or modify a device configuration profile for Windows 10 using the 'Microsoft Defender Antivirus' profile type and set 'Enable Tamper Protection to prevent Microsoft Defender being disabled' to 'Allow'
3. Assign the profile to the affected device groups and ensure the devices are checked in to Intune
4. Remove any conflicting GPOs that set 'DisableAntiSpyware' or 'DisableRealtimeMonitoring' to 1, as documented in Microsoft guidance
5. On each affected device, run the PowerShell command `Get-MpComputerStatus | Select-Object IsTamperProtected` to verify the setting is now 'True'

## Validation
After applying the Intune profile and removing conflicting GPOs, run `Get-MpComputerStatus | Select-Object IsTamperProtected` on a sample of affected devices. Confirm that the output shows 'IsTamperProtected : True'. Also verify in the Microsoft 365 Defender portal that the devices show Tamper Protection as 'On'.

## Rollback
Set the Intune profile setting for 'Enable Tamper Protection to prevent Microsoft Defender being disabled' to 'Not configured' and reapply any previously removed GPOs that set 'DisableAntiSpyware' or 'DisableRealtimeMonitoring' to 1.

## References
- Microsoft Learn: 'Prevent security settings changes with tamper protection'
- Microsoft Learn: 'Manage tamper protection using Microsoft Intune' â€“ https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/manage-tamper-protection-intune
