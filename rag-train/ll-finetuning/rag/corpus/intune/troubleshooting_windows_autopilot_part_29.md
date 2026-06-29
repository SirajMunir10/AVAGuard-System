# Troubleshooting: Windows Autopilot

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
What are known policies that conflict with Windows Autopilot during OOBE?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Windows Autopilot profiles, Group Policy, MDM policies

## Symptoms
- Autologon experience impacted during OOBE
- Enrollment Status Page (ESP) triggers reboot
- OOBE or user desktop autologon fails
- Increased prompts when modifying UAC settings during OOBE
- Windows Autopilot profile not retrieved

## Error Codes
N/A

## Root Causes
1. Disallow changing of language/region/keyboard GPO conflicts with autologon
2. AppLocker CSP triggers reboot when policy applied or deleted
3. DeviceLock policies (minimum password length, password complexity) cause autologon failure
4. Windows Security Baseline policies (administrator elevation prompt, admin approval mode, virtualization based security) require reboot causing extra prompts
5. Microsoft Account sign-in assistant (wlidsvc) disabled breaks Autopilot profile retrieval
6. AutoAdminLogon registry key set to 0 (disabled) breaks Autopilot
7. MDM wins over Group Policy setting may cause conflicts
8. Four specific GPO policy settings enabled break pre-provisioning

## Remediation Steps
1. Configure policies to not conflict: hide language/region/keyboard pages in Windows Autopilot profile if GPO must be set
2. Avoid using AppLocker CSP during ESP
3. Avoid DeviceLock policies (minimum password length, password complexity) during OOBE, especially for kiosk scenarios
4. Target Windows Security Baseline policies to users instead of devices to apply later
5. Ensure Microsoft Account sign-in assistant (wlidsvc) is not disabled
6. Ensure AutoAdminLogon registry key is not set to 0
7. Review and disable conflicting GPOs for pre-provisioned deployment

## Validation
1. Verify that the Windows Autopilot profile is retrieved by checking the deployment profile status in Intune (Devices > Windows > Windows enrollment > Deployment profiles > select profile > Monitor).
2. Confirm that the autologon experience works by reviewing the Autopilot deployment report for 'Autopilot success' and no 'Autopilot failure' entries.
3. Check that the Enrollment Status Page (ESP) does not trigger unexpected reboots by reviewing the ESP logs in %ProgramData%\Microsoft\Windows\EnrollmentStatusPage\logs.
4. Validate that no conflicting Group Policy objects are applied by running 'gpresult /h gpresult.html' on a test device and reviewing the output for the specific policies listed (e.g., Disallow changing of language/region/keyboard, DeviceLock policies, Windows Security Baseline policies).
5. Ensure the Microsoft Account sign-in assistant (wlidsvc) is running by executing 'Get-Service wlidsvc' and confirming Status is 'Running'.
6. Check the AutoAdminLogon registry key by running 'Get-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon' -Name AutoAdminLogon' and confirming the value is '1'.

## Rollback
1. If the Autopilot profile is not retrieved, re-enable the Microsoft Account sign-in assistant by running 'Set-Service wlidsvc -StartupType Automatic' and 'Start-Service wlidsvc'.
2. If autologon fails, set the AutoAdminLogon registry key to 1 by running 'Set-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon' -Name AutoAdminLogon -Value 1'.
3. If ESP triggers reboots, remove or disable the AppLocker CSP policy by navigating to Intune > Devices > Configuration profiles, selecting the policy, and setting 'Assignments' to 'None'.
4. If DeviceLock policies cause autologon failure, remove or disable the policy in Intune (Devices > Configuration profiles > select policy > Assignments > Exclude all groups).
5. If Windows Security Baseline policies cause extra prompts, change the policy assignment from devices to users in Intune (Devices > Configuration profiles > select policy > Assignments > Edit > Change 'Assign to' to 'All users').
6. If conflicting GPOs are identified, disable them in Group Policy Management Console (GPMC) by right-clicking the GPO and selecting 'Enforced' > 'No' or deleting the GPO link.

## References
- <https://learn.microsoft.com/en-us/autopilot/troubleshoot-oobe>
