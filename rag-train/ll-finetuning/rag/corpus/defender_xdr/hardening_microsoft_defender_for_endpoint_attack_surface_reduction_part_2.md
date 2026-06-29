# Hardening: Microsoft Defender for Endpoint â€“ Attack Surface Reduction

**Domain:** Defender XDR
**Subdomain:** Microsoft Defender for Endpoint â€“ Attack Surface Reduction
**Incident Type:** Hardening

## Scenario / Query
How can I verify and enable the Attack Surface Reduction (ASR) rule 'Block executable files from running unless they meet a prevalence, age, or trusted list criterion' (GUID: 01443614-cd74-433a-b99e-2ecdc07bfc25) in Microsoft Defender for Endpoint using Microsoft Intune, and what is the documented impact of enabling this rule?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Defender for Endpoint Plan 2
- **Configuration:** Intune endpoint security policies for Attack Surface Reduction rules; ASR rule GUID 01443614-cd74-433a-b99e-2ecdc07bfc25

## Symptoms
- Users report that legitimate executables are blocked without clear notification
- Security team observes high number of ASR rule blocks in Microsoft 365 Defender portal under Incidents & Alerts
- Help desk receives tickets about applications failing to launch on managed Windows 10/11 devices

## Error Codes
N/A

## Root Causes
1. ASR rule 'Block executable files from running unless they meet a prevalence, age, or trusted list criterion' is enabled in Block mode
2. The rule blocks executables that do not meet Microsoft's prevalence, age, or trusted publisher criteria
3. No exclusions have been configured for line-of-business applications that are not widely prevalent

## Remediation Steps
1. 1. In Microsoft Intune, navigate to Endpoint security > Attack surface reduction > Create policy > Platform: Windows 10 and later > Profile: Attack Surface Reduction Rules.
2. 2. Set the ASR rule GUID 01443614-cd74-433a-b99e-2ecdc07bfc25 to 'Audit mode' initially to assess impact without blocking.
3. 3. Review the audit events in Microsoft 365 Defender (https://security.microsoft.com) under Reports > Attack surface reduction rules > Add filter for rule GUID 01443614-cd74-433a-b99e-2ecdc07bfc25.
4. 4. Add file or folder exclusions for trusted line-of-business applications using the 'Exclude files and paths from Attack Surface Reduction Rules' setting in the same policy.
5. 5. After validation, change the rule from Audit mode to 'Block mode' for production deployment.
6. 6. Monitor the rule's performance via the ASR report in Microsoft 365 Defender.

## Validation
After enabling the rule in Audit mode, verify that no critical applications are blocked by checking the Attack surface reduction rules report in Microsoft 365 Defender. Then switch to Block mode and confirm that only untrusted executables are blocked.

## Rollback
Set the ASR rule to 'Disabled' in the Intune policy, or remove the rule assignment from the policy. The change takes effect at the next device check-in.

## References
- Microsoft Learn: 'Attack surface reduction rules reference' â€“ Rule: Block executable files from running unless they meet a prevalence, age, or trusted list criterion (GUID: 01443614-cd74-433a-b99e-2ecdc07bfc25). URL: https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide#block-executable-files-from-running-unless-they-meet-a-prevalence-age-or-trusted-list-criterion
- Microsoft Learn: 'Use attack surface reduction rules to prevent malware infection' â€“ https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules?view=o365-worldwide
