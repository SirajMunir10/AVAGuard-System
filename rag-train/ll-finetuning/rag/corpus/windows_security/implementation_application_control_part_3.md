# Implementation: Application Control

**Domain:** Windows Security
**Subdomain:** Application Control
**Incident Type:** Implementation

## Scenario / Query
How to choose between Windows Defender Application Control (WDAC) and AppLocker for application control in an organization?

## Environment Context
- **Tenant Type:** On-premises or hybrid Windows environment
- **Configuration:** Mixed Windows OS versions (Windows 10 and earlier); shared computers with different user/group policies

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Generally, customers who are able to implement application control using App Control, rather than AppLocker, should do so.
2. AppLocker is best when: You have a mixed Windows operating system (OS) environment and need to apply the same policy controls to Windows 10 and earlier versions of the OS.
3. AppLocker is best when: You need to apply different policies for different users or groups on shared computers.
4. As a best practice, you should enforce App Control at the most restrictive level possible for your organization, and then you can use AppLocker to further fine-tune the restrictions.

## Validation
1. Verify that WDAC policies are applied by running 'Get-CIPolicy' on a Windows 10 or later device to confirm the active policy. 2. Check AppLocker rules are enforced by running 'Get-AppLockerPolicy -Effective' on a Windows 10 or earlier device. 3. Confirm that the combined policy (WDAC base + AppLocker fine-tuning) is active by reviewing Event Viewer logs under 'Applications and Services Logs/Microsoft/Windows/AppLocker' and 'CodeIntegrity/Operational' for no errors. 4. Test application execution for a blocked app to ensure it is denied, and for an allowed app to ensure it runs.

## Rollback
1. Remove or disable the WDAC policy by running 'Set-RuleOption -FilePath <policy.xml> -Option 3' to switch to audit mode, then reboot. 2. Delete or disable AppLocker rules via 'Set-AppLockerPolicy -Policy $null' on affected machines. 3. Restore previous application control settings from backup using Group Policy or Local Security Policy. 4. Reboot all affected systems to apply the rollback.

## References
- <https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/wdac-and-applocker-overview>
