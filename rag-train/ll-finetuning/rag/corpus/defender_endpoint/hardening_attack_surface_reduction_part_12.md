# Hardening: Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction
**Incident Type:** Hardening

## Scenario / Query
How to block executable content downloaded from email and webmail clients using ASR rules?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** ASR rule for blocking executable content from email/webmail

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use Intune (Configuration Profiles) with rule: 'Execution of executable content (exe, dll, ps, js, vbs, etc.) dropped from email (webmail/mail client) (no exceptions)'
2. Use Configuration Manager with rule: 'Block executable content download from email and webmail clients'
3. Use Group Policy with rule: 'Block executable content from email client and webmail'

## Validation
1. Confirm the ASR rule is enabled: Run Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids and verify the GUID for 'Block executable content from email client and webmail' (e.g., be9ba2d3-4a91-4b5b-96a5-fb2c3cfa1e2c) is present with action 1 (block).
2. Test the rule: Attempt to download an executable (.exe) from a webmail client (e.g., Outlook Web Access) and verify the download is blocked and an event (e.g., Event ID 1121) is generated in Microsoft-Windows-Windows Defender/Operational log.
3. In Microsoft 365 Defender portal, navigate to Reports > Attack surface reduction rules and confirm the rule shows blocked events for the test user/device.

## Rollback
1. Disable the ASR rule: Set-MpPreference -AttackSurfaceReductionRules_Ids be9ba2d3-4a91-4b5b-96a5-fb2c3cfa1e2c -AttackSurfaceReductionRules_Actions Disabled
2. If using Intune, edit the configuration profile to set the rule to 'Not configured' or 'Audit only' and sync the device.
3. If using Group Policy, set the policy to 'Disabled' or 'Not configured' and run gpupdate /force.
4. Verify the rule is no longer enforced: Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids and confirm the GUID is absent or set to action 0 (audit) or 2 (warn).

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference>
