# Hardening: Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction
**Incident Type:** Hardening

## Scenario / Query
How do I enable and verify Attack Surface Reduction (ASR) rules using Microsoft Defender for Endpoint to harden endpoints against common malware and ransomware techniques?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Defender for Endpoint Plan 2
- **Configuration:** Attack Surface Reduction rules are managed via Microsoft Intune or Group Policy; this scenario uses Intune for deployment.

## Symptoms
- Endpoint remains vulnerable to known attack vectors such as Office macro execution, script-based downloads, and credential theft from LSASS.
- Security recommendations in Microsoft 365 Defender portal show 'Attack surface reduction rules' as 'Not configured' or 'Blocked' with low coverage.

## Error Codes
N/A

## Root Causes
1. ASR rules are not enabled or are configured in 'Audit only' mode instead of 'Block' mode.
2. Exclusions are too broad, allowing malicious behavior to bypass the rules.

## Remediation Steps
1. 1. In the Microsoft 365 Defender portal (https://security.microsoft.com), navigate to 'Endpoints' > 'Configuration management' > 'Endpoint security policies' > 'Attack surface reduction'.
2. 2. Create a new policy or edit an existing one. Set the desired ASR rules to 'Block' (e.g., rule GUIDs: 26190899-1602-49e8-8b27-eb1d0a1ce869 for Office macro, 9e6c4e1f-7d60-472f-ba1a-a39ef669e4b2 for credential theft from LSASS).
3. 3. Apply the policy to the appropriate device groups (e.g., 'All devices' or a pilot group).
4. 4. Verify enforcement by checking the 'Attack surface reduction' report in the Defender portal under 'Reports' > 'Attack surface reduction rules'.
5. 5. Use the following PowerShell cmdlet on a test device to confirm rule status: Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids

## Validation
Run the PowerShell command 'Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids' on a managed endpoint to confirm the rule GUIDs are present and set to '1' (block). Alternatively, in the Defender portal, navigate to 'Reports' > 'Attack surface reduction rules' and verify that the rule shows 'Blocked' events.

## Rollback
In the Defender portal, edit the ASR policy and change the rule action from 'Block' to 'Audit only' or 'Disabled'. Apply the updated policy to the device group. Alternatively, remove the device group assignment.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules?view=o365-worldwide>
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/enable-attack-surface-reduction-rules?view=o365-worldwide>
