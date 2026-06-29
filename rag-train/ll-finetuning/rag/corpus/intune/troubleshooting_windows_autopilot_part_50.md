# Troubleshooting: Windows Autopilot

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
Why is the web sign-in option missing at the Windows sign-in screen after Windows Autopilot pre-provisioning completes?

## Environment Context
- **Tenant Type:** Azure AD/Entra ID tenant with Intune
- **Configuration:** Security Baseline applied during Autopilot pre-provisioning

## Symptoms
- Web sign-in option missing at Windows sign-in screen after pre-provisioning completes

## Error Codes
N/A

## Root Causes
1. Device password policies in the Security Baseline cause issues after pre-provisioning

## Remediation Steps
1. Change the password settings in Security Baseline to Not Configured
2. Assign the baseline to a user group instead of a device group

## Validation
1. Verify that the security baseline policy has been updated: In the Intune admin center, navigate to 'Endpoint Security' > 'Security baselines' and select the baseline assigned during Autopilot. Confirm that password-related settings (e.g., 'Minimum password length', 'Password complexity', 'Password history') are set to 'Not configured'. 2. Check the policy assignment: Under the same baseline, go to 'Assignments' and ensure the baseline is assigned to a user group (not a device group). 3. On a test device that has completed pre-provisioning, trigger a policy sync by going to 'Settings' > 'Accounts' > 'Access work or school' > select the MDM enrollment > 'Info' > 'Sync'. 4. After sync completes, restart the device and observe the Windows sign-in screen. Confirm that the 'Sign in with a web account' or 'Web sign-in' option is now visible. 5. Optionally, run the command 'dsregcmd /status' in an elevated command prompt and verify that 'AzureAdPrt' is 'YES' and 'WebSignIn' is 'YES'.

## Rollback
1. In the Intune admin center, navigate to 'Endpoint Security' > 'Security baselines' and select the baseline that was modified. 2. Revert the password settings to their original values (e.g., set 'Minimum password length' to 8, 'Password complexity' to 'Require', etc.) as per the original security baseline configuration. 3. Change the assignment back to the original device group if it was changed to a user group. 4. On a test device, force a policy sync via 'Settings' > 'Accounts' > 'Access work or school' > select the MDM enrollment > 'Info' > 'Sync'. 5. Restart the device and confirm that the web sign-in option is no longer present at the sign-in screen, indicating the rollback has taken effect.

## References
- <https://learn.microsoft.com/en-us/autopilot/troubleshoot-oobe>
