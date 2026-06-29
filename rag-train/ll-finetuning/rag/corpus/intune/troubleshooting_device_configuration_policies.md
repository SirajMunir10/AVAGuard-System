# Troubleshooting: Device Configuration Policies

**Domain:** Intune
**Subdomain:** Device Configuration Policies
**Incident Type:** Troubleshooting

## Scenario / Query
How to change security policies for enrolled Windows 10 devices when unassigning the policy does not remove the security settings?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Windows 10 devices with security policies assigned

## Symptoms
- Windows 10 devices may not remove security policies when you unassign the policy (stop deployment)

## Error Codes
N/A

## Root Causes
1. Security policies may persist on Windows 10 devices after unassignment

## Remediation Steps
1. Leave the policy assigned, and then change the security settings back to the default values
2. Depending on the device platform, if you want to change the policy to a less secure value, you may need to reset the security policies. For example, in Windows 8.1, on the desktop, swipe in from right to open the Charms bar. Choose Settings > Control Panel > User Accounts. On the left, select Reset Security Policies link, and choose Reset Policies.
3. Other platforms, such as Android, and iOS/iPadOS may need to be retired and re-enrolled to apply a less restrictive policy

## Validation
1. Confirm the policy is still assigned to the device group in the Intune console: Devices > Configuration policies > select the policy > Assignments > verify the group is listed. 2. On a Windows 10 device, open Command Prompt as administrator and run 'gpresult /h C:\gpresult.html' to export the resulting policy set. 3. Open the exported HTML file and search for the specific security settings that were changed; verify they now show the default values (e.g., 'Not Defined' or the default state). 4. Alternatively, on the device, navigate to Settings > Accounts > Access work or school > click the connected account > Info > check that the policy compliance status shows 'Compliant' and the policy name appears under 'Policies managed by your organization' with the updated settings.

## Rollback
1. In the Intune console, navigate to Devices > Configuration policies and select the policy. 2. Under Assignments, remove the device group from the 'Included groups' list and add it to 'Excluded groups' to stop the policy deployment. 3. On the affected Windows 10 device, open Command Prompt as administrator and run 'gpupdate /force' to force a Group Policy refresh. 4. If the security settings persist, on the device go to Settings > Accounts > Access work or school > click the connected account > Disconnect, then re-enroll the device in Intune by going to Settings > Accounts > Access work or school > Connect and signing in with the organization credentials. 5. After re-enrollment, reassign the original policy to the device group and verify the settings revert to the intended state.

## References
- <https://learn.microsoft.com/en-us/mem/intune/configuration/troubleshoot-policies-in-microsoft-intune>
