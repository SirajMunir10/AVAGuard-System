# Implementation: Antivirus

**Domain:** Intune
**Subdomain:** Antivirus
**Incident Type:** Implementation

## Scenario / Query
How to configure and manage antivirus protection settings using Intune endpoint security policies?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Antivirus policy

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use Antivirus policy type to configure and manage antivirus protection settings.
2. Platform support: Windows, macOS, Linux.
3. Available profiles: Defender Update controls, Microsoft Defender Antivirus, Microsoft Defender Antivirus exclusions, Windows Security experience, macOS Endpoint security antivirus.
4. Use case: Centrally manage Microsoft Defender Antivirus policies on Windows devices.

## Validation
1. In the Microsoft Intune admin center, navigate to Endpoint security > Antivirus and confirm the policy is listed with the intended profile (e.g., Microsoft Defender Antivirus).
2. Select the policy and review the assigned groups to ensure correct targeting.
3. On a Windows device in the assigned group, open Windows Security > Virus & threat protection > Manage settings and verify that real-time protection, cloud-delivered protection, and automatic sample submission are enabled as configured.
4. Run the PowerShell command: Get-MpPreference | Select-Object -Property DisableRealtimeMonitoring, DisableBehaviorMonitoring, DisableBlockAtFirstSeen, MAPSReporting, SubmitSamplesConsent. Confirm values match policy settings.
5. Check the device’s Microsoft Defender Antivirus event log (Event Viewer > Applications and Services Logs > Microsoft > Windows > Windows Defender > Operational) for Event ID 5001 (policy applied) or 5007 (configuration change).

## Rollback
1. In the Microsoft Intune admin center, go to Endpoint security > Antivirus, select the problematic policy, and choose Delete to remove it.
2. If the policy was recently modified, select the policy, click Properties, and under Configuration settings, revert each setting to its previous value (e.g., set DisableRealtimeMonitoring to Not configured).
3. On affected devices, run the PowerShell command: Update-MpSignature to ensure definitions are current after policy removal.
4. To force a policy refresh on a Windows device, run: Get-MgDeviceManagementConfigurationPolicy -DeviceManagementConfigurationPolicyId <policy-id> | Invoke-MgDeviceManagementConfigurationPolicyAssign.
5. Monitor the Windows Security app and event logs (Event ID 5007) to confirm the device has reverted to default or previous policy state.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/endpoint-security-policy>
