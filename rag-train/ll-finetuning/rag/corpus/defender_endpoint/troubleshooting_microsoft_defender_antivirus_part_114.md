# Troubleshooting: Microsoft Defender Antivirus

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to tell if Microsoft Defender Antivirus doesn't start because a non-Microsoft antivirus is installed on Windows 10 or Windows 11?

## Environment Context
- **Tenant Type:** Windows 10 or Windows 11 device, not using Microsoft Defender for Endpoint
- **Configuration:** Non-Microsoft antivirus installed

## Symptoms
- Microsoft Defender Antivirus Service is set to manual in Services app
- When trying to start the service manually, a warning appears: 'The Microsoft Defender Antivirus Service service on Local Computer started and then stopped. Some services stop automatically if they aren't in use by other services or programs.'

## Error Codes
N/A

## Root Causes
1. Microsoft Defender Antivirus is automatically turned off to preserve compatibility with a non-Microsoft antivirus

## Remediation Steps
1. Open the Services app by selecting the Search icon from the taskbar and searching for 'services', or by typing 'services.msc' from the command-line.
2. Check the status of Microsoft Defender Antivirus Service under Windows Defender > Operational.
3. Generate a detailed report about currently active group policies by opening a command prompt in Run as admin mode and entering: GPresult.exe /h gpresult.html
4. Open the generated report at ./gpresult.html and look under the heading 'Windows Components/Microsoft Defender Antivirus' for entries like: Policy: Turn off Microsoft Defender Antivirus, Setting: Enabled, Winning GPO: Win10-Workstations
5. Also check under the heading 'Registry item (Key path: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender, Value name: DisableAntiSpyware)' for similar entries indicating Microsoft Defender Antivirus is turned off.

## Validation
1. Open Services app (services.msc) and verify that 'Microsoft Defender Antivirus Service' status is 'Running' and its Startup Type is 'Automatic'.
2. Open an elevated command prompt and run: sc query WinDefend
   Confirm the STATE is '4  RUNNING'.
3. Run: GPresult.exe /h gpresult.html
   Open gpresult.html and verify under 'Windows Components/Microsoft Defender Antivirus' that 'Turn off Microsoft Defender Antivirus' is either not listed or set to 'Disabled'.
4. Check registry: reg query "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableAntiSpyware
   Confirm the value is 0 or the key does not exist.

## Rollback
1. Open Group Policy Management Console (gpmc.msc) and edit the GPO that enabled 'Turn off Microsoft Defender Antivirus' (e.g., Win10-Workstations) to set it to 'Not Configured' or 'Disabled'.
2. On the affected device, run from an elevated command prompt: gpupdate /force
3. Delete the DisableAntiSpyware registry value if present:
   reg delete "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableAntiSpyware /f
4. Restart the Microsoft Defender Antivirus service: net start WinDefend
5. If the service fails to start, re-enable the original policy settings to restore the previous state.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus-when-migrating>
