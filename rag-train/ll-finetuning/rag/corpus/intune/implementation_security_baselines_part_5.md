# Implementation: Security Baselines

**Domain:** Intune
**Subdomain:** Security Baselines
**Incident Type:** Implementation

## Scenario / Query
How to implement and configure available security baselines in Intune for Windows 10 and later and Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Security Baseline for Windows 10 and later versions 25H2, 24H2, 23H2, November 2021, December 2020, August 2020; Microsoft Defender for Endpoint baseline versions 24H1, 6, 5, 4, 3

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the links to view the settings for recent instances of each baseline.
2. Ensure your environment meets the prerequisites for using Microsoft Defender for Endpoint before applying its baseline.
3. Note: The Microsoft Defender for Endpoint security baseline is optimized for physical devices and is currently not recommended for use on virtual machines (VMs) or VDI endpoints.

## Validation
1. Sign in to the Microsoft Intune admin center (https://intune.microsoft.com).
2. Navigate to Endpoint security > Security baselines.
3. Verify that the desired baseline profiles (e.g., 'Security Baseline for Windows 10 and later (version 25H2)' and 'Microsoft Defender for Endpoint baseline (version 24H1)') are listed and show a status of 'Active'.
4. Select each baseline profile and confirm that the assigned groups are correct and the profile is 'Assigned'.
5. On a Windows 10/11 device that is a member of the assigned group, open Settings > Accounts > Access work or school, and click 'Info' to verify the last sync time is recent.
6. On the same device, open a command prompt as administrator and run: 'dsregcmd /status'. Confirm that 'AzureAdJoined' is 'YES' and 'DomainJoined' is 'NO' (or as appropriate).
7. Run 'gpresult /r' and verify that the Intune security baseline policies are applied (look for 'Intune Management Extension' or 'MDM Policy' entries).
8. For Microsoft Defender for Endpoint baseline, on a physical device, open Windows Security > Device security and confirm that Core isolation details are present and settings match the baseline.

## Rollback
1. Sign in to the Microsoft Intune admin center (https://intune.microsoft.com).
2. Navigate to Endpoint security > Security baselines.
3. Select the baseline profile that caused issues (e.g., 'Security Baseline for Windows 10 and later (version 25H2)').
4. Click 'Properties' and then 'Assignments'.
5. Change the assignment to 'Not assigned' or remove the problematic group, then click 'Save'.
6. Alternatively, delete the profile entirely by selecting it and clicking 'Delete' > 'OK'.
7. If the baseline was applied via a group policy conflict, remove the device from the assigned group in Azure AD/Intune.
8. On affected devices, run 'gpupdate /force' to refresh policy and then 'gpresult /r' to confirm the baseline settings are removed.
9. For Microsoft Defender for Endpoint baseline issues on VMs, ensure the baseline is not assigned to any VM groups; if necessary, create a new exclusion group and reassign the baseline to physical devices only.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/security-baselines>
