# Troubleshooting: Microsoft Defender Antivirus

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to tell if Microsoft Defender Antivirus starts in passive mode because Microsoft Defender for Endpoint is used with a non-Microsoft antivirus on Windows 10 or Windows 11?

## Environment Context
- **Tenant Type:** Windows 10 or Windows 11 device, using Microsoft Defender for Endpoint
- **Configuration:** Non-Microsoft antivirus installed

## Symptoms
- Microsoft Defender Antivirus starts in passive mode with reduced functionality

## Error Codes
N/A

## Root Causes
1. Microsoft Defender for Endpoint is used with a non-Microsoft antivirus installed, causing Microsoft Defender Antivirus to start in passive mode

## Remediation Steps
1. Open the Services app by selecting the Search icon from the taskbar and searching for 'services', or by typing 'services.msc' from the command-line.
2. Check the status of Microsoft Defender Antivirus Service under Windows Defender > Operational.
3. Generate a detailed report about currently active group policies by opening a command prompt in Run as admin mode and entering: GPresult.exe /h gpresult.html
4. Open the generated report at ./gpresult.html and look under the heading 'Windows Components/Microsoft Defender Antivirus' for entries like: Policy: Turn off Microsoft Defender Antivirus, Setting: Enabled, Winning GPO: Win10-Workstations
5. Also check under the heading 'Registry item (Key path: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender, Value name: DisableAntiSpyware)' for similar entries indicating Microsoft Defender Antivirus is turned off.

## Validation
1. Open Services app (services.msc) and verify that 'Microsoft Defender Antivirus Service' shows 'Running' and 'Automatic' startup type.
2. Run 'Get-MpComputerStatus' in PowerShell as admin and confirm 'AMRunningMode' equals 'Passive Mode'.
3. Run 'GPresult.exe /h gpresult.html' as admin, open the report, and under 'Windows Components/Microsoft Defender Antivirus' confirm no policy sets 'Turn off Microsoft Defender Antivirus' to 'Enabled'.
4. Check registry key HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\DisableAntiSpyware and confirm value is 0 or absent.

## Rollback
1. If validation fails, ensure non-Microsoft antivirus is installed and active; if not, reinstall it.
2. If a GPO is forcing passive mode incorrectly, work with domain admin to remove or disable the 'Turn off Microsoft Defender Antivirus' policy.
3. If registry key DisableAntiSpyware is set to 1, change it to 0 or delete the value, then restart the Microsoft Defender Antivirus Service.
4. As a last resort, uninstall the non-Microsoft antivirus and re-enable Microsoft Defender Antivirus via 'Turn Windows Defender Antivirus on or off' in Windows Security.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus-when-migrating>
