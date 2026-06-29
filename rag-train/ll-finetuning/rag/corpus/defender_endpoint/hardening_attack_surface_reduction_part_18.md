# Hardening: Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction
**Incident Type:** Hardening

## Scenario / Query
How to block rebooting machine in Safe Mode using ASR rules?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Microsoft Defender Antivirus

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enable ASR rule with GUID 33ddedf1-c6e0-47cb-833e-de6133960387 via Intune or Configuration Manager.
2. Use Microsoft Intune name: Block rebooting machine in Safe Mode.
3. Note: Safe Mode is still manually accessible from the Windows Recovery Environment.

## Validation
1. Confirm the ASR rule is enabled: In Microsoft 365 Defender portal, go to Endpoints > Configuration management > Endpoint security policies > Attack surface reduction. Verify the rule 'Block rebooting machine in Safe Mode' (GUID: 33ddedf1-c6e0-47cb-833e-de6133960387) is set to 'Block' or 'Audit' as intended.
2. Test the rule: On a managed Windows device, attempt to restart into Safe Mode (e.g., via Shift+Restart or msconfig). Verify the action is blocked and an event (e.g., Event ID 1121) is generated in Microsoft Defender for Endpoint indicating the rule prevented the reboot.
3. Check reporting: In Microsoft 365 Defender, navigate to Reports > Attack surface reduction rules. Confirm the rule shows blocked events for the test device.

## Rollback
1. Disable the ASR rule: In Microsoft 365 Defender portal, go to Endpoints > Configuration management > Endpoint security policies > Attack surface reduction. Locate the rule 'Block rebooting machine in Safe Mode' (GUID: 33ddedf1-c6e0-47cb-833e-de6133960387) and set it to 'Disabled' or 'Not configured'.
2. If using Intune: In Microsoft Intune admin center, go to Endpoint security > Attack surface reduction. Edit the policy containing the rule, set the rule to 'Disabled', and save. Sync the device to apply changes.
3. If using Configuration Manager: In the Configuration Manager console, navigate to Assets and Compliance > Endpoint Protection > Windows Defender Exploit Guard > Attack Surface Reduction. Modify the policy to disable the rule and deploy the updated policy to affected devices.
4. Verify rollback: On a test device, confirm that rebooting into Safe Mode is no longer blocked and that no ASR events for this rule are generated.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference>
