# Troubleshooting: Windows Autopilot

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
During the ESP of a Windows Autopilot deployment, why does the Microsoft 365 Click-to-Run version of Office fail to install the Teams Machine-Wide Installer, or cause other Win32 app MSI based installs to fail?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Windows Autopilot deployment with Enrollment Status Page (ESP) enabled

## Symptoms
- Teams Machine-Wide Installer fails to install during ESP
- Other Win32 app MSI based installs fail during ESP

## Error Codes
N/A

## Root Causes
1. The Teams Machine-Wide Installer component of the Microsoft 365 Click-to-Run version of Office includes an MSI installation
2. ESP doesn't track the Teams Machine-Wide Installer MSI install
3. MSIs install via TrustedInstaller which doesn't allow simultaneous installations
4. Timing issue between the Teams Machine-Wide Installer MSI install and other Win32 app MSI installs

## Remediation Steps
1. Don't install Teams as part of the Microsoft 365 Click-to-Run install of Office. Instead, deploy Teams as a Win32 app after the Windows Autopilot deployment completes.
2. Don't install the Microsoft 365 Click-to-Run version of Office during ESP. Instead, deploy the Microsoft 365 Click-to-Run install of Office after the Windows Autopilot deployment completes.
3. Use a custom PowerShell script for Intune Management Extension (IME) that checks if TrustedInstaller is currently installing another MSI. If it is, then wait for the current MSI to finish installing before launching a new MSI install.
4. For Windows 11 deployments, use Windows Autopilot device preparation. Windows Autopilot device preparation doesn't use ESP so therefore supports mixing of LOB and Win32 apps.
5. Continue on error for ESP failures. If the problem occurs with this option enabled, some applications including Teams might not install. However, ESP continues and doesn't fail.

## Validation
1. Verify that the Teams Machine-Wide Installer is not present: Run 'Get-AppxPackage -Name MicrosoftTeams' in PowerShell as SYSTEM. If no output, Teams is not installed. 2. Check that no MSI installations are pending: Run 'Get-WmiObject -Class Win32_Product | Where-Object {$_.Name -like "*Teams*"}' to confirm no Teams-related MSI is registered. 3. Confirm ESP completed without errors: In Intune, navigate to Devices > Monitor > Enrollment failures, and verify no ESP failure events for the device. 4. If using the custom PowerShell script, check the Intune Management Extension log at C:\ProgramData\Microsoft\IntuneManagementExtension\Logs for any 'TrustedInstaller' wait events.

## Rollback
1. If Teams was deployed as a Win32 app after Autopilot, remove the Win32 app assignment in Intune: Go to Apps > All apps, select the Teams app, click Properties, and set Assignment to 'Uninstall'. 2. If Office was moved out of ESP, re-enable Office installation during ESP by adding the Office 365 Click-to-Run app to the ESP profile's 'Block apps' or 'Allow apps' list as appropriate. 3. If the custom PowerShell script was used, remove the script from Intune: Go to Devices > Scripts, select the script, and delete it. 4. If 'Continue on error' was enabled, disable it in the ESP profile: Go to Devices > Enrollment > Windows enrollment > Enrollment Status Page, edit the profile, and set 'Show progress and allow user to continue' to 'No'.

## References
- <https://learn.microsoft.com/en-us/autopilot/troubleshoot-oobe>
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/windows-enrollment-status>
