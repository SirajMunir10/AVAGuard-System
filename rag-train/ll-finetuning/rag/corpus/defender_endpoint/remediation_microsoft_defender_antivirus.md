# Remediation: Microsoft Defender Antivirus

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Remediation

## Scenario / Query
What system settings and services are restored by Microsoft Defender Antivirus after malware detection?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Microsoft Defender Antivirus, Malicious Software Removal Tool, or System Center Endpoint Protection

## Symptoms
- Malware detected and removed or quarantined by Microsoft Defender Antivirus

## Error Codes
N/A

## Root Causes
1. Malware infection that modified system settings and services

## Remediation Steps
1. No action is necessary. Microsoft Defender Antivirus removed or quarantined a threat.
2. Microsoft Defender Antivirus restores the following system settings and services that might have been changed by the malware: Default Internet Explorer or Microsoft Edge setting, User Access Control settings, Chrome settings, Boot Control Data, Regedit and Task Manager registry settings, Windows Update, Background Intelligent Transfer Service, and Remote Procedure Call service, Windows Operating System files

## Validation
1. Open Event Viewer and navigate to 'Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational'. Look for Event ID 1116 (malware detected) and Event ID 1117 (malware remediated). Confirm the threat was removed or quarantined.
2. Run the following PowerShell command to verify that default Internet Explorer or Microsoft Edge settings are restored: Get-ItemProperty -Path 'HKLM:\SOFTWARE\Policies\Microsoft\Internet Explorer\Main' | Select-Object *
3. Check User Access Control (UAC) settings: Get-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System' | Select-Object EnableLUA
4. Verify Chrome settings are restored: Get-ItemProperty -Path 'HKLM:\SOFTWARE\Policies\Google\Chrome' | Select-Object *
5. Confirm Boot Configuration Data (BCD) integrity: bcdedit /enum
6. Check that Regedit and Task Manager are enabled: Get-ItemProperty -Path 'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System' | Select-Object DisableRegistryTools; Get-ItemProperty -Path 'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System' | Select-Object DisableTaskMgr
7. Verify Windows Update service is running: Get-Service -Name wuauserv | Select-Object Status, StartType
8. Confirm Background Intelligent Transfer Service (BITS) is running: Get-Service -Name BITS | Select-Object Status, StartType
9. Check Remote Procedure Call (RPC) service status: Get-Service -Name RpcSs | Select-Object Status, StartType
10. Run System File Checker to verify Windows OS files: sfc /scannow

## Rollback
1. If a system setting was not restored correctly, manually restore it using Group Policy or registry edits. For example, to re-enable Registry Editor: Set-ItemProperty -Path 'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System' -Name 'DisableRegistryTools' -Value 0
2. To restore default Internet Explorer settings: Run 'inetcpl.cpl' and click 'Advanced' tab, then 'Reset'.
3. To restore UAC settings: Set-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System' -Name 'EnableLUA' -Value 1
4. To restore Chrome settings: Reset Chrome via chrome://settings/reset
5. To repair Boot Configuration Data: Run 'bootrec /fixmbr', 'bootrec /fixboot', 'bootrec /scanos', 'bootrec /rebuildbcd' from Windows Recovery Environment.
6. To re-enable Task Manager: Set-ItemProperty -Path 'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System' -Name 'DisableTaskMgr' -Value 0
7. To restart Windows Update service: Set-Service -Name wuauserv -StartupType Automatic; Start-Service -Name wuauserv
8. To restart BITS: Set-Service -Name BITS -StartupType Automatic; Start-Service -Name BITS
9. To restart RPC service: Set-Service -Name RpcSs -StartupType Automatic; Start-Service -Name RpcSs
10. If Windows OS files are corrupted, run 'DISM /Online /Cleanup-Image /RestoreHealth' followed by 'sfc /scannow'.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
