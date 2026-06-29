# Remediation: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Remediation

## Scenario / Query
How to restore a file from quarantine in Microsoft Defender for Endpoint after determining it is clean?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Windows Defender Antivirus platform

## Symptoms
- File quarantined by Microsoft Defender for Endpoint
- File determined to be clean after investigation

## Error Codes
N/A

## Root Causes
1. File was incorrectly flagged as a threat and quarantined

## Remediation Steps
1. Open an elevated Command Prompt (Run as administrator) on the device where the file was quarantined.
2. Run the following command to change directory to the latest antimalware platform version: (set "_done=" & if exist "%ProgramData%\Microsoft\Windows Defender\Platform\" (for /f "delims=" %d in ('dir "%ProgramData%\Microsoft\Windows Defender\Platform" /ad /b /o:-n 2^>nul') do if not defined _done (cd /d "%ProgramData%\Microsoft\Windows Defender\Platform\%d" & set _done=1)) else (cd /d "%ProgramFiles%\Windows Defender")) >nul 2>&1
3. Run the following command to restore the file: MpCmdRun.exe -Restore -Name EUS:Win32/CustomEnterpriseBlock -All
4. Note: In some scenarios, the ThreatName might appear as EUS:Win32/CustomEnterpriseBlock!cl or EUS:Win32/CustomEnterpriseBlock!cl

## Validation
Defender for Endpoint restores all custom blocked files that were quarantined on this device in the last 30 days.

## Rollback
Files quarantined as a potential network threat might not be recoverable. This type of file might not be accessible in quarantine due to lack of network credentials or expired tokens from a temporary sign-in.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-file-alerts>
