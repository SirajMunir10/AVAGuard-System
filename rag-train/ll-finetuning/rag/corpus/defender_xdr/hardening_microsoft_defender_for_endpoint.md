# Hardening: Microsoft Defender for Endpoint

**Domain:** Defender XDR
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Hardening

## Scenario / Query
How do I verify and enforce that all Windows devices in my tenant have real-time protection enabled and are not running with tamper protection disabled, which could allow attackers to disable Defender AV?

## Environment Context
- **Tenant Type:** Enterprise Microsoft 365 E5 with Defender for Endpoint Plan 2
- **Configuration:** Devices onboarded to Defender for Endpoint, but some may have real-time protection turned off or tamper protection disabled due to local admin changes.

## Symptoms
- Defender for Endpoint alerts showing 'Real-time protection off' for specific devices
- Tamper protection status shows 'Disabled' in the Microsoft 365 Defender portal for some devices
- Devices appear in the 'Inactive' or 'At risk' device list despite being onboarded

## Error Codes
N/A

## Root Causes
1. Local administrators or users disabled real-time protection via Group Policy, registry, or PowerShell without tamper protection blocking the change
2. Tamper protection was not enabled via Intune or tenant-wide policy, allowing unauthorized modifications to Defender AV settings

## Remediation Steps
1. Enable tamper protection tenant-wide using Microsoft Intune: create a device configuration profile for Windows 10/11 with the 'Microsoft Defender Antivirus' policy setting 'Turn on tamper protection' set to 'Enabled'.
2. Use Microsoft 365 Defender portal to verify tamper protection status: go to Settings > Endpoints > Advanced features > Tamper protection and set it to 'On'.
3. Run the following PowerShell command on affected devices to re-enable real-time protection: Set-MpPreference -DisableRealtimeMonitoring $false (requires admin rights).
4. Deploy a proactive remediation script via Microsoft Intune or Configuration Manager to detect and fix devices where real-time protection is off.

## Validation
In the Microsoft 365 Defender portal, navigate to Devices, select a device, and confirm that 'Real-time protection' and 'Tamper protection' both show 'On'. Alternatively, run Get-MpComputerStatus | Select-Object RealTimeProtectionEnabled, TamperProtectionSource on the device.

## Rollback
To disable tamper protection, set the Intune policy to 'Not configured' or 'Disabled' and remove the PowerShell setting by running Set-MpPreference -DisableRealtimeMonitoring $true only if explicitly required and after risk assessment.

## References
- Microsoft Learn: 'Turn on tamper protection in Microsoft Defender for Endpoint'
- Microsoft Learn: 'Enable and configure Microsoft Defender Antivirus always-on protection'
