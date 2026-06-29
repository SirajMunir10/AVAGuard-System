# Hardening: Application Control

**Domain:** Windows Security
**Subdomain:** Application Control
**Incident Type:** Hardening

## Scenario / Query
How to harden Windows clients by controlling which drivers and applications are allowed to run using App Control for Business?

## Environment Context
- **Tenant Type:** Windows 10 and later
- **Configuration:** App Control was designed as a security feature under the servicing criteria defined by the Microsoft Security Response Center (MSRC)

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
1. Run 'Get-CIPolicy' to export the current App Control policy and verify that rules based on code signing certificates, file attributes, ISG reputation, managed installer, path, or launching process are present. 2. Execute 'Get-AppLockerPolicy -Effective' to confirm the policy is applied. 3. Test by launching a blocked application and confirm it is denied with Event ID 3076 or 3077 in Event Viewer under Applications and Services Logs/Microsoft/Windows/AppLocker. 4. Verify that allowed applications run without error.

## Rollback
1. Run 'Set-RuleOption -FilePath <CurrentPolicy.xml> -Option 3' to enable audit mode temporarily. 2. Deploy the previous working policy using 'Set-AppLockerPolicy -PolicyObject $previousPolicy -Merge'. 3. If using MDM or GPO, revert the App Control policy configuration to the prior version. 4. Restart the device to ensure the rollback takes effect.

## References
- <https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/wdac-and-applocker-overview>
