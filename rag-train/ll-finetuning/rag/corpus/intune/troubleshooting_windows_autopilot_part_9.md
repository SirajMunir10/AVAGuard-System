# Troubleshooting: Windows Autopilot

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve Kiosk device profile not auto logging in when auto logon is enabled during Windows Autopilot deployment?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Kiosk device profile with auto logon enabled, Windows 11 version 24H2 with KB5058411 or later

## Symptoms
- Kiosk device profiles do not auto log in when auto logon is enabled
- Multiple reboots or unexpected reboots during Windows out-of-box experience (OOBE) when initially configuring the Kiosk
- Autologon entries in the registry might be deleted

## Error Codes
N/A

## Root Causes
1. Multiple reboots or unexpected reboots during OOBE when initially configuring the Kiosk cause autologon registry entries to be deleted

## Remediation Steps
1. Apply or reapply the kiosk profile after Windows Autopilot completes
2. Apply the autologon registry entries either manually or via a script. For example: reg.exe add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v "AutoAdminLogon" /t REG_SZ /d 1 /f
3. reg.exe add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v "DefaultDomainName" /t REG_SZ /d "." /f
4. reg.exe add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v "DefaultUserName" /t REG_SZ /d "kioskUser0" /f
5. Exclude items the required reboots during OOBE from Windows Autopilot
6. Manually enter the kiosk user credentials

## Validation
This issue is fixed in Windows 11, version 24H2 on systems that are patched with KB5058411 or later.

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/mem/autopilot/known-issues>
