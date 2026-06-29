# Implementation: Microsoft Defender for Endpoint onboarding

**Domain:** Defender XDR
**Subdomain:** Microsoft Defender for Endpoint onboarding
**Incident Type:** Implementation

## Scenario / Query
A security administrator is onboarding Windows 10 devices to Microsoft Defender for Endpoint using Group Policy. After deploying the Group Policy Object (GPO) with the correct onboarding package, some devices show as 'Inactive' in the Microsoft 365 Defender portal. What is the most likely cause and how should the administrator resolve it?

## Environment Context
- **Tenant Type:** Enterprise (Microsoft 365 E5)
- **Configuration:** Group Policy-based onboarding for Microsoft Defender for Endpoint; devices are Windows 10 20H2+

## Symptoms
- Devices appear as 'Inactive' in the Microsoft 365 Defender portal after GPO deployment
- No recent sensor data or health signals from affected devices
- Microsoft Defender for Endpoint service is not running on some devices

## Error Codes
N/A

## Root Causes
1. The Group Policy Object was not linked to the correct Organizational Unit (OU) containing the target devices
2. The onboarding package (.cmd file) was not placed in the correct startup script location specified in the GPO
3. The Microsoft Defender for Endpoint sensor service (Sense) is disabled or not starting due to missing prerequisites (e.g., KB4052623 or later update)

## Remediation Steps
1. Verify that the GPO is linked to the OU containing the target Windows 10 devices
2. Confirm that the onboarding package (WindowsDefenderATPOnboardingPackage.cmd) is copied to the startup script path defined in the GPO (e.g., \\domain\sysvol\...\Scripts\Startup)
3. Ensure the devices have the required update KB4052623 installed (or a later cumulative update that includes it)
4. On an affected device, run 'sc query sense' to check the status of the Microsoft Defender for Endpoint sensor service; if not running, start it with 'sc start sense'
5. If the service fails to start, review the Microsoft-Windows-Sense/Operational event log for errors
6. After correcting the GPO link or script location, force a Group Policy update with 'gpupdate /force' and reboot the device

## Validation
After remediation, the device should appear as 'Active' in the Microsoft 365 Defender portal (Devices > Inventory) within one hour. Run 'Get-MpComputerStatus | select AMRunningMode' in PowerShell to confirm the sensor is running.

## Rollback
Remove the GPO link from the OU or delete the startup script path in the GPO. Uninstall the onboarding package by running the offboarding script from the Microsoft 365 Defender portal (Settings > Endpoints > Offboarding).

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-gp>
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding#microsoft-defender-for-endpoint-service-is-not-starting>
