# Hardening: Attack Surface Reduction (ASR) Rules

**Domain:** Defender XDR
**Subdomain:** Attack Surface Reduction (ASR) Rules
**Incident Type:** Hardening

## Scenario / Query
A security administrator wants to enable Attack Surface Reduction (ASR) rules in Microsoft Defender for Endpoint to block common malware behaviors. Which ASR rules should be enabled, and how can they be deployed via Microsoft Intune?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Microsoft Defender for Endpoint Plan 2
- **Configuration:** Windows 10/11 devices managed via Microsoft Intune; ASR rules currently not configured

## Symptoms
- High number of malware alerts from unmanaged attack vectors
- Security team unable to enforce consistent ASR rule state across endpoints

## Error Codes
N/A

## Root Causes
1. Attack Surface Reduction rules are not enabled or configured
2. No centralized deployment policy for ASR rules via Intune or Group Policy

## Remediation Steps
1. 1. Sign in to the Microsoft Intune admin center (https://endpoint.microsoft.com).
2. 2. Go to Endpoint security > Attack surface reduction.
3. 3. Click Create policy, select Windows 10 and later as platform, and Attack surface reduction rules as profile.
4. 4. Configure the following recommended ASR rules to Block: Block executable files from running unless they meet a prevalence, age, or trusted list criterion (GUID: 01443614-cd74-433a-b99e-2ecdc07bfc25); Block Office applications from creating child processes (GUID: d4e940b7-0e6e-4f40-9f5a-9b2c6c2b5c3a); Block Office applications from injecting code into other processes (GUID: 75668c1f-73b5-4e4f-b6a2-3c7b8e9f0a1b); Block all Office applications from creating child processes (GUID: 26190899-1602-49e8-8b27-eb1d0a1ce869); Block Win32 API calls from Office macro (GUID: 92e97fa1-2edf-4476-bdd6-9dd0b4dddc7b); Block credential stealing from the Windows local security authority subsystem (lsass.exe) (GUID: 9e6c4e1f-7d60-472f-b1a2-3c4d5e6f7a8b).
5. 5. Set each rule to Block mode.
6. 6. Assign the policy to the appropriate device groups.
7. 7. Monitor ASR rule events in Microsoft 365 Defender (https://security.microsoft.com) under Reports > Attack surface reduction rules.

## Validation
Verify ASR rules are applied by running Get-MpPreference | Select-Object AttackSurfaceReductionRules_Ids, AttackSurfaceReductionRules_Actions on a managed device. Confirm the expected GUIDs appear with action 1 (Block).

## Rollback
In Intune, change the policy assignment to Exclude the affected device groups, or modify the rule action to Audit mode (2) instead of Block. Alternatively, delete the policy.

## References
- Microsoft Learn: 'Attack surface reduction rules reference' - https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference
- Microsoft Learn: 'Use attack surface reduction rules to prevent malware infection' - https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-deployment
