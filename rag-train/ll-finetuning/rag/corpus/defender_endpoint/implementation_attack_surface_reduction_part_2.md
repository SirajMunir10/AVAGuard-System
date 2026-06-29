# Implementation: Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction
**Incident Type:** Implementation

## Scenario / Query
Which ASR rules are supported on Windows 10/11 version 1709 or later?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Standard protection rules and other ASR rules with version requirements.

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Block abuse of exploited vulnerable signed drivers (Device) - requires 1709 or later.
2. Block credential stealing from the Windows local security authority subsystem - requires 1803 or later.
3. Block persistence through WMI event subscription - requires 1903 or later.
4. Block Adobe Reader from creating child processes - requires 1809 or later.
5. Block all Office applications from creating child processes - requires 1709 or later.
6. Block executable content from email client and webmail - requires 1709 or later.
7. Block executable files from running unless they meet a prevalence, age, or trusted list criterion - requires 1803 or later.
8. Block execution of potentially obfuscated scripts - requires 1709 or later.
9. Block JavaScript or VBScript from launching downloaded executable content - requires 1709 or later.
10. Block Office applications from creating executable content - requires 1709 or later.
11. Block Office applications from injecting code into other processes - requires 1709 or later.
12. Block Office communication application from creating child processes - requires 1709 or later.
13. Block process creations originating from PSExec and WMI commands - requires 1803 or later.
14. Block rebooting machine in Safe Mode - requires 1709 or later.
15. Block untrusted and unsigned processes that run from USB - requires 1709 or later.
16. Block use of copied or impersonated system tools - requires 1709 or later.
17. Block Webshell creation for Servers - Exchange servers only.
18. Block Win32 API calls from Office macros - requires 1709 or later.
19. Use advanced protection against ransomware - requires 1803 or later.

## Validation
Run the following PowerShell command to list all ASR rules and their status on a Windows 10/11 device (version 1709 or later):

Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids

Then verify that each rule ID from the remediation list is present. For example, check that rule ID '56a863a9-875e-4185-98a7-b882c64b5ce5' (Block abuse of exploited vulnerable signed drivers) is included. Confirm the device meets the minimum OS version requirement for each rule by running:

(Get-CimInstance Win32_OperatingSystem).Version

For Windows 10/11, version 1709 corresponds to build 16299, version 1803 to 17134, version 1809 to 17763, version 1903 to 18362. Ensure the build number is equal to or greater than the required version for each rule.

## Rollback
If the remediation fails or causes issues, disable the problematic ASR rule(s) using PowerShell:

Set-MpPreference -AttackSurfaceReductionRules_Ids <RuleID> -AttackSurfaceReductionRules_Actions Disabled

For example, to disable the 'Block abuse of exploited vulnerable signed drivers' rule:

Set-MpPreference -AttackSurfaceReductionRules_Ids 56a863a9-875e-4185-98a7-b882c64b5ce5 -AttackSurfaceReductionRules_Actions Disabled

If multiple rules need to be disabled, repeat the command for each rule ID. To revert to the previous state, re-enable the rules with:

Set-MpPreference -AttackSurfaceReductionRules_Ids <RuleID> -AttackSurfaceReductionRules_Actions Enabled

Alternatively, if the entire ASR configuration was changed, restore from a backup of the Group Policy or Intune policy that defines the ASR rules.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference>
