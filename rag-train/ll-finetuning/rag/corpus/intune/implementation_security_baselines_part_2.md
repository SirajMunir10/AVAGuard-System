# Implementation: Security Baselines

**Domain:** Intune
**Subdomain:** Security Baselines
**Incident Type:** Implementation

## Scenario / Query
How do I deploy a security baseline profile in Intune to enforce recommended security settings on Windows devices?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Security baseline profiles for Windows 10 and later

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Create a security baseline profile in Intune by selecting the baseline template that consists of multiple device configuration profiles.
2. Deploy the security baseline to groups of users or devices in Intune.
3. Customize the baseline to apply only the settings and values you require if the default configuration does not work for your environment.

## Validation
1. Sign in to the Microsoft Intune admin center (https://intune.microsoft.com).
2. Navigate to Endpoint security > Security baselines.
3. Select the deployed baseline profile (e.g., 'Windows 10 and later security baseline').
4. On the profile overview page, confirm the 'Status' shows 'Succeeded' for the assigned groups.
5. Click 'Device status' and verify that devices report 'Succeeded' or 'Compliant'.
6. On a targeted Windows device, open Settings > Accounts > Access work or school > click the connected account > Info. Confirm the 'Last successful sync' time is recent.
7. On the device, run 'dsregcmd /status' in Command Prompt and verify 'AzureAdJoined' is 'YES' and 'DomainJoined' is appropriate.
8. Check that the baseline settings are applied by reviewing local policy or using the 'Get-MpComputerStatus' PowerShell cmdlet for Microsoft Defender settings if included.

## Rollback
1. Sign in to the Microsoft Intune admin center (https://intune.microsoft.com).
2. Navigate to Endpoint security > Security baselines.
3. Select the deployed baseline profile.
4. Click 'Properties' > 'Assignments'.
5. Change the assignment to 'Unassigned' or remove the targeted groups, then click 'Save' to stop enforcement.
6. Alternatively, delete the baseline profile entirely by selecting it and clicking 'Delete' > 'OK'.
7. If devices need to revert to previous settings, wait for the next Intune sync (up to 8 hours) or manually trigger a sync from the device: Settings > Accounts > Access work or school > select the account > Sync.
8. For immediate rollback, create a new configuration profile that explicitly sets the affected settings to 'Not configured' and assign it to the same groups with a higher priority.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/security-baselines>
