# Hardening: Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction
**Incident Type:** Hardening

## Scenario / Query
How do I enable and verify Attack Surface Reduction (ASR) rules via Microsoft Intune to harden endpoints against common malware and ransomware techniques?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Microsoft Defender for Endpoint Plan 2
- **Configuration:** Intune endpoint security policies for Attack Surface Reduction rules

## Symptoms
- Security report shows low ASR rule coverage
- Repeated alerts for blocked or allowed suspicious behaviors that ASR rules could prevent

## Error Codes
N/A

## Root Causes
1. ASR rules not deployed via Intune or Group Policy
2. ASR rules set to 'Audit only' instead of 'Block'
3. Exclusions incorrectly configured allowing malicious activity

## Remediation Steps
1. In Microsoft Intune, navigate to Endpoint security > Attack surface reduction.
2. Create or edit a policy for 'Attack Surface Reduction Rules' targeting the relevant device groups.
3. Set desired ASR rules to 'Block' (e.g., rule GUID 9e6c4e1f-7d60-472f-ba1a-a39ef669e4b2 for ransomware behavior).
4. Ensure exclusions are limited and reviewed per Microsoft guidance.
5. Assign the policy and monitor compliance in the Intune console.

## Validation
Verify in Microsoft 365 Defender portal under Reports > Attack surface reduction rules that the rule state is 'Block' and events are recorded.

## Rollback
Set the ASR rule to 'Not configured' or 'Audit only' in the Intune policy, then force a sync on affected devices.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules?view=o365-worldwide>
