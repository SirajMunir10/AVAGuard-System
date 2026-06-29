# Implementation: Microsoft Defender Antivirus

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Implementation

## Scenario / Query
How to configure Microsoft Defender Antivirus features using supported tools?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Microsoft Defender Antivirus configuration

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use Microsoft Defender for Endpoint Security Policy Management
2. Use Microsoft Intune
3. Use Microsoft Configuration Manager
4. Use Microsoft Configuration Manager Tenant attach
5. Use Group Policy
6. Use PowerShell cmdlets
7. Use Windows Management Instrumentation (WMI)

## Validation
1. Verify that Microsoft Defender Antivirus is enabled and running: Get-MpComputerStatus | Select-Object AMRunningMode, AMServiceEnabled, AntivirusEnabled. 2. Confirm policy application: For Intune, check the device's 'Antivirus' policy status in the Microsoft Intune admin center under 'Devices' > 'All devices' > select device > 'Managed apps' > 'Policy'. For Configuration Manager, run 'Get-CMAntimalwarePolicy -Name <PolicyName>' in Configuration Manager PowerShell. For Group Policy, run 'gpresult /h gpresult.html' and review the HTML report for Defender policies. 3. Validate specific feature settings: For real-time protection, run 'Get-MpPreference | Select-Object DisableRealtimeMonitoring'. For cloud-delivered protection, run 'Get-MpPreference | Select-Object MAPSReporting'. Ensure values match intended configuration.

## Rollback
1. Revert to previous policy: In Intune, edit the antivirus policy and set 'DisableRealTimeMonitoring' to 'Not configured' or 'No'. In Configuration Manager, deploy a baseline policy with previous settings. In Group Policy, disable the relevant GPO or set the policy to 'Not configured'. 2. Reset PowerShell preferences: Set-MpPreference -DisableRealtimeMonitoring $false; Set-MpPreference -MAPSReporting 0. 3. Restore default WMI settings: Use 'Set-MpPreference' cmdlets to reset all preferences to defaults. 4. If using Configuration Manager tenant attach, remove the tenant attach policy from the device collection. 5. Re-enable any disabled services: Set-Service -Name WinDefend -StartupType Automatic; Start-Service -Name WinDefend.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-microsoft-defender-antivirus-features>
