# Troubleshooting: Microsoft Defender for Endpoint onboarding

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint onboarding
**Incident Type:** Troubleshooting

## Scenario / Query
How to verify that Microsoft Defender Antivirus drivers (WdBoot, WdFilter) are in their default state during onboarding troubleshooting?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** Microsoft Defender Antivirus passive mode

## Symptoms
- Microsoft Defender Antivirus drivers may not be in default state

## Error Codes
N/A

## Root Causes
1. Windows Defender services (wdboot, wdfilter, wdnisdrv, wdnissvc, windefend) startup type changed from default

## Remediation Steps
1. Check registry key HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender to verify policy is disabled
2. Ensure WdBoot and WdFilter registry keys under SYSTEM\CurrentControlSet\Services have Start value set to 0 (DWord) for default configuration
3. Do not change the startup of Windows Defender services (wdboot, wdfilter, wdnisdrv, wdnissvc, windefend) as it is unsupported and may force reimaging

## Validation
1. Open Registry Editor (regedit.exe) as Administrator. 2. Navigate to HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender. Verify that the 'DisableAntiSpyware' value (if present) is set to 0 (DWord) or does not exist. 3. Navigate to HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WdBoot. Verify that the 'Start' value is 0 (DWord). 4. Navigate to HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WdFilter. Verify that the 'Start' value is 0 (DWord). 5. Open an elevated Command Prompt and run 'sc query WdBoot' and 'sc query WdFilter' to confirm the services are running (STATE should be RUNNING). 6. Run 'Get-MpComputerStatus | Select-Object AMRunningMode' in PowerShell to confirm the antivirus is in passive mode (expected: 'Passive Mode').

## Rollback
1. If any registry value was changed, restore the original values: - For HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender\DisableAntiSpyware, set it back to its original value (e.g., 1 if it was disabled). - For WdBoot and WdFilter 'Start' values, restore the original DWord value (e.g., 4 for disabled or 1 for system start). 2. If service startup types were modified, revert them to their original state using 'sc config <service> start=<original_type>' (e.g., 'sc config WdBoot start= boot' for boot-start). 3. Restart the system to reapply original driver states. 4. If the system fails to boot, use Windows Recovery Environment (WinRE) to restore a system backup or revert registry changes via offline registry editing.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
