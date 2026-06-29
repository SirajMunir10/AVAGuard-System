# Implementation: Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction
**Incident Type:** Implementation

## Scenario / Query
What are the Intune and Configuration Manager names for the ASR rule that blocks executable content from email and webmail?

## Environment Context
- **Tenant Type:** Microsoft Intune or Configuration Manager
- **Configuration:** N/A

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. In Microsoft Intune, use the name: Block executable content from email client and webmail
2. In Microsoft Configuration Manager, use the name: Block executable content from email client and webmail

## Validation
1. In Microsoft Intune, navigate to Endpoint Security > Attack Surface Reduction > Policies. Select the policy containing the ASR rule and verify the rule is set to 'Block executable content from email client and webmail' with the desired action (e.g., Block, Audit, or Warn).
2. In Microsoft Configuration Manager, go to Assets and Compliance > Endpoint Protection > Windows Defender Exploit Guard > Attack Surface Reduction. Confirm the rule named 'Block executable content from email client and webmail' is enabled with the appropriate action.
3. On a test device, send an email with an executable attachment (e.g., .exe, .scr) to a monitored mailbox. Verify the attachment is blocked and an event (e.g., Event ID 1121) is generated in the Microsoft-Windows-Windows Defender/Operational log.

## Rollback
1. In Microsoft Intune, edit the ASR policy and change the rule 'Block executable content from email client and webmail' to 'Not configured' or 'Audit' to revert to previous state.
2. In Microsoft Configuration Manager, disable or remove the rule 'Block executable content from email client and webmail' from the ASR policy.
3. Force a policy sync on affected devices: In Intune, use 'Sync' from the device management portal; in Configuration Manager, trigger a machine policy retrieval cycle.
4. Confirm the change by sending a test executable attachment to verify it is no longer blocked.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference>
