# Implementation: Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction
**Incident Type:** Implementation

## Scenario / Query
What are the operating system support requirements for configuring and managing ASR rules in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** ASR rules are available on any edition of Windows that includes Microsoft Defender Antivirus. Centralized management requires Microsoft Defender for Endpoint with Intune, Configuration Manager, or the Defender portal.

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Configure ASR rules locally using PowerShell or Group Policy.
2. For centralized management, reporting, and alerting, use Microsoft Intune, Microsoft Configuration Manager, or the Microsoft Defender portal.

## Validation
1. On a Windows device running a supported edition (e.g., Windows 10 Pro, Enterprise, or Education), open PowerShell as Administrator and run: Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids. Verify that the output lists the GUIDs of the ASR rules you configured. 2. Run: Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Actions. Confirm that each rule's action (e.g., 1 = Block, 2 = Audit) matches your intended configuration. 3. If using centralized management, sign in to the Microsoft Defender portal (https://security.microsoft.com), navigate to Endpoints > Attack surface reduction rules, and verify that the rules are listed with the correct state and scope. 4. For Intune-managed devices, go to the Microsoft Intune admin center (https://intune.microsoft.com), select Endpoint security > Attack surface reduction, and confirm the policy is assigned and shows a 'Succeeded' status for targeted devices.

## Rollback
1. To remove a locally configured ASR rule via PowerShell, run: Remove-MpPreference -AttackSurfaceReductionRules_Ids <GUID>. Repeat for each rule you need to remove. 2. To revert to default ASR rule state (not configured), run: Set-MpPreference -AttackSurfaceReductionRules_Ids @() -AttackSurfaceReductionRules_Actions @(). 3. If using Group Policy, navigate to Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Microsoft Defender Exploit Guard > Attack Surface Reduction, set the policy to 'Not Configured', and run gpupdate /force on affected devices. 4. For Intune, edit the ASR policy in the Microsoft Intune admin center, change the rule actions to 'Not configured' or delete the policy assignment, then sync devices. 5. In the Microsoft Defender portal, remove or disable the ASR rule configuration from the Attack surface reduction rules blade.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference>
