# Implementation: Security Baselines

**Domain:** Intune
**Subdomain:** Security Baselines
**Incident Type:** Implementation

## Scenario / Query
How to implement Microsoft security baselines in Intune for Windows devices?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Windows security baseline settings

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. The Microsoft security team has years of experience working directly with Windows developers and the security community to create these recommendations.
2. The settings in this baseline are considered the most relevant security-related configuration options.
3. In each new build of Windows, the team adjusts its recommendations based on newly released features.

## Validation
1. In the Microsoft Intune admin center, navigate to 'Endpoint security' > 'Security baselines'. 2. Select the baseline profile that was assigned (e.g., 'Windows 10 and later' or 'Windows 11'). 3. Review the 'Assigned' status to confirm the profile is applied to the intended device groups. 4. On a target Windows device, open 'Settings' > 'Accounts' > 'Access work or school', click the Intune enrollment entry, then 'Info' to verify the last policy sync. 5. Run 'dsregcmd /status' in Command Prompt as Administrator and confirm 'AzureAdJoined' is YES and 'DomainJoined' is NO (for Azure AD-joined devices). 6. Run 'gpresult /h C:\gpresult.html' and open the HTML file to check that security baseline settings (e.g., BitLocker, firewall rules) are applied under 'Administrative Templates'.

## Rollback
1. In the Microsoft Intune admin center, go to 'Endpoint security' > 'Security baselines'. 2. Select the baseline profile that was assigned. 3. Click 'Properties' and then 'Assignments'. 4. Remove the device groups from the 'Included groups' list, or change the assignment to 'Not configured'. 5. Alternatively, create a new baseline profile with the default settings (no customizations) and assign it to the same groups to overwrite the previous baseline. 6. On affected devices, force a sync by going to 'Settings' > 'Accounts' > 'Access work or school', selecting the Intune enrollment, and clicking 'Sync'. 7. Verify rollback by repeating the validation steps to confirm the baseline settings are no longer enforced.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/security-baselines>
