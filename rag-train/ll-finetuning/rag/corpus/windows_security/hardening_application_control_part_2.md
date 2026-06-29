# Hardening: Application Control

**Domain:** Windows Security
**Subdomain:** Application Control
**Incident Type:** Hardening

## Scenario / Query
How to harden Windows clients by preventing end-users from running unapproved software using AppLocker?

## Environment Context
- **Tenant Type:** On-premises Windows
- **Configuration:** Windows 7 or later

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use AppLocker to control which applications are allowed to run on Windows clients.
2. Define AppLocker rules based on attributes of the codesigning certificate, signed metadata (Original Filename, version, file hash), or file path.

## Validation
1. Open Local Group Policy Editor (gpedit.msc) and navigate to Computer Configuration > Windows Settings > Security Settings > Application Control Policies > AppLocker. 2. Confirm that AppLocker rules are configured under Executable Rules, Windows Installer Rules, Script Rules, and Packaged app Rules as needed. 3. Run 'Get-AppLockerPolicy -Effective' in PowerShell to verify the active policy. 4. Test by attempting to run an unapproved executable (e.g., a portable app not covered by any rule) and confirm it is blocked with an AppLocker event (Event ID 8003 or 8004 in Event Viewer under Applications and Services Logs/Microsoft/Windows/AppLocker).

## Rollback
1. Open Local Group Policy Editor (gpedit.msc) and navigate to Computer Configuration > Windows Settings > Security Settings > Application Control Policies > AppLocker. 2. For each rule collection (Executable Rules, Windows Installer Rules, Script Rules, Packaged app Rules), right-click and select 'Clear Policy' or delete individual rules that were added. 3. Alternatively, run 'Set-AppLockerPolicy -Policy $null -Merge $false' in PowerShell to remove all AppLocker rules. 4. Run 'gpupdate /force' to apply the change. 5. Verify that previously blocked applications now run without restriction.

## References
- <https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/wdac-and-applocker-overview>
