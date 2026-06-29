# Implementation: Attack Surface Reduction

**Domain:** Intune
**Subdomain:** Attack Surface Reduction
**Incident Type:** Implementation

## Scenario / Query
How to harden devices against common attack methods using attack surface reduction policies in Intune?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Attack surface reduction policy

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use Attack surface reduction policy type to reduce potential attack vectors and system vulnerabilities.
2. Platform support: Windows.
3. Available profiles: App and browser isolation, Attack surface reduction rules, Device control, Exploit protection, Application control.
4. Use case: Harden devices against common attack methods and techniques.
5. Requirements: Microsoft Defender Antivirus must be the primary antivirus solution.

## Validation
1. In the Microsoft Intune admin center, navigate to Endpoint security > Attack surface reduction. 2. Confirm that the policy you created appears in the list with a status of 'Succeeded' or 'Active'. 3. On a Windows device that is targeted by the policy, open the Microsoft Defender for Endpoint security center and verify that the attack surface reduction rules are enabled and configured as expected. 4. Run the PowerShell command 'Get-MpPreference' on the device and check that the AttackSurfaceReductionRules_Ids and AttackSurfaceReductionRules_Actions properties match your policy settings. 5. Review the device's Event Viewer logs under 'Applications and Services Logs/Microsoft/Windows/Windows Defender/Operational' for event ID 1121 (block) or 1122 (audit) to confirm the rules are being applied.

## Rollback
1. In the Microsoft Intune admin center, navigate to Endpoint security > Attack surface reduction. 2. Select the policy you deployed and choose 'Delete' to remove it. 3. If you need to revert to a previous configuration, reassign a previously saved backup policy or create a new policy with the original settings. 4. On affected devices, run the PowerShell command 'Set-MpPreference -AttackSurfaceReductionRules_Ids <list of rule GUIDs> -AttackSurfaceReductionRules_Actions Disabled' to disable any rules that were enabled. 5. Monitor the devices for any residual effects and confirm that the original behavior is restored.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/endpoint-security-policy>
