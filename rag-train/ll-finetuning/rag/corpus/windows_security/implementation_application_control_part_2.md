# Implementation: Application Control

**Domain:** Windows Security
**Subdomain:** Application Control
**Incident Type:** Implementation

## Scenario / Query
How to implement AppLocker to control which applications are allowed to run on Windows clients?

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
1. Define AppLocker policies based on attributes of the codesigning certificate used to sign an app and its binaries.
2. Define AppLocker policies based on attributes of the app's binaries that come from the signed metadata for the files, such as Original Filename and version, or the hash of the file.
3. Define AppLocker policies based on the path where the app or file exists on disk.
4. Apply AppLocker policies to all users on a computer, or to individual users and groups.

## Validation
1. Run 'Get-AppLockerPolicy -Effective' to confirm the policy is applied. 2. Check Event Viewer > Applications and Services Logs > Microsoft > Windows > AppLocker for event ID 8003 (allowed) or 8004 (blocked). 3. Test by launching a blocked app and verifying it fails to start. 4. Verify policy scope: 'Get-AppLockerPolicy -Local | Test-AppLockerPolicy -Path C:\Windows\System32\notepad.exe -User Everyone' to confirm rule behavior.

## Rollback
1. Run 'Set-AppLockerPolicy -Policy $null -Merge' to remove local policies. 2. Delete custom rules: 'Remove-AppLockerPolicy -RuleType Publisher,Path,FileHash -Force'. 3. Restore default policy: 'Set-AppLockerPolicy -Policy (Get-AppLockerPolicy -Default) -Merge'. 4. Reboot or run 'gpupdate /force' to apply changes.

## References
- <https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/wdac-and-applocker-overview>
