# Implementation: Security Baselines

**Domain:** Intune
**Subdomain:** Security Baselines
**Incident Type:** Implementation

## Scenario / Query
How to deploy a recommended security posture to managed Windows devices using Microsoft Intune security baselines?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Windows 10 version 1809 and later

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Access the Microsoft Intune security baselines feature to rapidly deploy a recommended security posture to managed Windows devices.
2. Navigate the large number of controls using Microsoft's guidance in the form of security baselines.

## Validation
1. In the Microsoft Intune admin center, go to 'Endpoint security' > 'Security baselines'. 2. Select the baseline profile that was deployed (e.g., 'Windows 10 and later (version 1809+)'). 3. Review the 'Profile status' to confirm it shows 'Succeeded' for the targeted devices. 4. On a managed Windows 10 device (version 1809 or later), open 'Settings' > 'Accounts' > 'Access work or school' and verify the device is connected to Intune. 5. Run the following PowerShell command as Administrator: Get-MpComputerStatus | Select-Object -Property AntivirusEnabled, RealTimeProtectionEnabled. Confirm both properties are 'True' as per baseline settings.

## Rollback
1. In the Microsoft Intune admin center, go to 'Endpoint security' > 'Security baselines'. 2. Select the deployed baseline profile. 3. Click 'Properties' and then 'Assignments'. 4. Change the assignment to 'Not assigned' for all groups to remove the baseline. 5. Alternatively, create a new baseline profile with default or less restrictive settings and assign it to the same groups to override the previous baseline. 6. On affected devices, run 'gpupdate /force' from an elevated command prompt to refresh policy. 7. Verify the device returns to its previous security state by checking the same settings used in validation.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/security-baselines>
