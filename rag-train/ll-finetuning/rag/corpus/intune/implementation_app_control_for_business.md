# Implementation: App Control for Business

**Domain:** Intune
**Subdomain:** App Control for Business
**Incident Type:** Implementation

## Scenario / Query
How to implement application allowlisting using Windows Defender Application Control (WDAC) in Intune?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** App Control for Business policy

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use App Control for Business policy type to control which applications can run on Windows devices using Windows Defender Application Control (WDAC).
2. Platform support: Windows.
3. Available profiles: Windows Defender Application Control (WDAC).
4. Use case: Implement application allowlisting and control software execution.

## Validation
1. In the Microsoft Intune admin center, navigate to Endpoint Security > App Control for Business and confirm the policy is assigned to the target device group. 2. On a Windows device in the group, open Event Viewer and navigate to Applications and Services Logs > Microsoft > Windows > CodeIntegrity > Operational. Verify Event ID 3076 (audit) or 3077 (enforce) appears, indicating WDAC policy application. 3. Run the PowerShell command 'Get-CIPolicy' to list active WDAC policies and confirm the policy name matches the deployed policy. 4. Attempt to run a non-allowlisted application (e.g., a portable executable not in the policy) and confirm it is blocked with an error message referencing Windows Defender Application Control.

## Rollback
1. In the Microsoft Intune admin center, go to Endpoint Security > App Control for Business, select the policy, and choose 'Delete' to remove the policy assignment. 2. On affected devices, run the PowerShell command 'Reset-WDACPolicy' to clear any locally cached WDAC policies. 3. Reboot the device to ensure the policy is fully removed. 4. Verify removal by checking Event Viewer for Event ID 3079 (policy removed) and confirming non-allowlisted applications can run.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/endpoint-security-policy>
