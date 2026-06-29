# Implementation: Endpoint Security Policy

**Domain:** Intune
**Subdomain:** Endpoint Security Policy
**Incident Type:** Implementation

## Scenario / Query
How to configure Attack Surface Reduction (ASR) policy in Intune?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Microsoft Defender Antivirus must be the primary antivirus solution

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure Microsoft Defender Antivirus is the primary antivirus solution.
2. Configure ASR rules as native Microsoft Defender Antivirus features that integrate with Defender for Endpoint.
3. Use advanced device control policies with Defender's peripheral monitoring capabilities.

## Validation
1. Confirm Microsoft Defender Antivirus is active and the primary antivirus solution by running on a test device: 'Get-MpComputerStatus | Select-Object AMRunningMode, AMServiceEnabled, AntivirusEnabled'. Verify 'AMRunningMode' is 'Normal' and 'AMServiceEnabled' and 'AntivirusEnabled' are 'True'.
2. In the Microsoft Intune admin center, navigate to 'Endpoint security' > 'Attack surface reduction' and verify the ASR policy is assigned to the correct device groups and its 'Assignment status' shows 'Succeeded'.
3. On a test device, run 'Get-MpPreference | Select-Object AttackSurfaceReductionRules_Ids, AttackSurfaceReductionRules_Actions' to confirm the expected ASR rule IDs and actions (e.g., 1 for Block, 2 for Audit) are applied.
4. Validate that advanced device control policies with Defender's peripheral monitoring are active by checking 'Device control' policies under 'Endpoint security' > 'Attack surface reduction' and confirming the policy is assigned and enforced.

## Rollback
1. In the Microsoft Intune admin center, navigate to 'Endpoint security' > 'Attack surface reduction', select the ASR policy, and choose 'Delete' to remove it. Alternatively, change the policy assignment to 'Not assigned' for the affected device groups.
2. If Microsoft Defender Antivirus was not the primary antivirus, re-enable the previous antivirus solution and disable Defender by setting 'DisableAntiSpyware' to 'True' via registry or Group Policy (not recommended unless necessary).
3. For advanced device control policies, navigate to 'Endpoint security' > 'Attack surface reduction', select the device control policy, and either delete it or modify its assignments to exclude affected devices.
4. On test devices, run 'Set-MpPreference -AttackSurfaceReductionRules_Ids @() -AttackSurfaceReductionRules_Actions @()' to clear all ASR rules, or use specific rule IDs to revert to previous states.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/endpoint-security-policy>
