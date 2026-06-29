# Implementation: Application Control

**Domain:** Windows Security
**Subdomain:** Application Control
**Incident Type:** Implementation

## Scenario / Query
How to deploy AppLocker as a complement to Windows Defender Application Control (WDAC) for shared device scenarios?

## Environment Context
- **Tenant Type:** On-premises or hybrid Windows environment
- **Configuration:** Shared computers with different user or group restrictions

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. AppLocker can also be deployed as a complement to App Control to add user or group-specific rules for shared device scenarios, where it's important to prevent some users from running specific apps.
2. As a best practice, you should enforce App Control at the most restrictive level possible for your organization, and then you can use AppLocker to further fine-tune the restrictions.

## Validation
1. Verify that AppLocker rules are applied correctly by running 'Get-AppLockerPolicy -Effective' on a shared device and confirming that user/group-specific rules are present. 2. Test by logging in as a restricted user and attempting to launch a blocked application; confirm the application is blocked with an AppLocker event in Event Viewer under 'Applications and Services Logs/Microsoft/Windows/AppLocker'. 3. Confirm that WDAC policies remain intact by running 'Get-CIPolicy' and checking that the base policy is still enforced.

## Rollback
1. Remove or disable the AppLocker rules that were added by running 'Set-AppLockerPolicy -Policy $null -Merge' to clear user-defined rules, or use 'Remove-AppLockerRule' for specific rules. 2. If AppLocker service was enabled, stop it with 'Stop-Service AppIDSvc' and set startup type to disabled via 'Set-Service AppIDSvc -StartupType Disabled'. 3. Reboot the device to ensure changes take effect, then re-validate that only WDAC policies are active.

## References
- <https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/wdac-and-applocker-overview>
