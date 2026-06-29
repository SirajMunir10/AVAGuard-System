# Implementation: Application Control

**Domain:** Windows Security
**Subdomain:** Application Control
**Incident Type:** Implementation

## Scenario / Query
How to implement App Control for Business to control which drivers and applications are allowed to run on Windows clients?

## Environment Context
- **Tenant Type:** Windows 10 and later
- **Configuration:** App Control policies apply to the managed computer as a whole and affect all users of the device

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Define App Control rules based on attributes of the codesigning certificate used to sign an app and its binaries
2. Define App Control rules based on attributes of the app's binaries that come from the signed metadata for the files, such as Original Filename and version, or the hash of the file
3. Define App Control rules based on the reputation of the app as determined by Microsoft's Intelligent Security Graph
4. Define App Control rules based on the identity of the process that initiated the installation of the app and its binaries (managed installer)
5. Define App Control rules based on the path where the app or file exists on disk (beginning with Windows 10 version 1903)
6. Define App Control rules based on the process that launched the app or binary

## Validation
1. Run `Get-CimInstance -ClassName Win32_DeviceGuard -Namespace root\Microsoft\Windows\DeviceGuard` to confirm that App Control for Business is enabled (e.g., 'AppControlCodeIntegrityPolicyEnforcementStatus' is 2).
2. Run `Get-AppLockerPolicy -Effective | Test-AppLockerPolicy -Path C:\Windows\System32\notepad.exe -User Everyone` to verify that a known allowed app is permitted.
3. Run `Get-AppLockerPolicy -Effective | Test-AppLockerPolicy -Path C:\Windows\Temp\malicious.exe -User Everyone` to confirm that an untrusted binary is blocked.
4. Review the Event Viewer under 'Applications and Services Logs > Microsoft > Windows > CodeIntegrity > Operational' for events 3076 (allowed) and 3077 (blocked) to validate policy enforcement.

## Rollback
1. If the policy causes issues, run `Set-RuleOption -FilePath C:\Policies\AppControlPolicy.xml -Option 3` to enable audit mode temporarily.
2. Deploy the audit-mode policy using `ConvertFrom-CIPolicy -XmlFilePath C:\Policies\AppControlPolicy.xml -BinaryFilePath C:\Policies\AppControlPolicy.bin` and then apply via Group Policy or MDM.
3. To fully remove the policy, delete the App Control policy XML from the Group Policy Object or MDM profile and force a policy refresh with `gpupdate /force` or sync the device.
4. Reboot the device to ensure the policy is no longer enforced.

## References
- <https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/wdac-and-applocker-overview>
