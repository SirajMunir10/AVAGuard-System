# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
What actions are available for the Restricted apps list in Endpoint DLP and when do they apply?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP policy with Restricted apps list

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. The action (audit, block with override, or block) that you define for apps on the restricted apps list only applies when a user attempts to access a protected item.
2. When you select 'Access by restricted apps' in a policy and a user uses an app on the restricted apps list to access a protected file, the activity is audited, blocked, or blocked with override, depending on how you configured the Restricted apps list.
3. All activity is audited and available for review in activity explorer.

## Validation
1. Confirm that the Endpoint DLP policy includes the 'Access by restricted apps' rule. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies, select the policy, and verify under 'Rules' that 'Access by restricted apps' is configured with the desired action (Audit, Block with override, or Block).
2. On a test device, use an app listed in the restricted apps list (e.g., Notepad) to open a protected file. Verify that the configured action is enforced (e.g., file is blocked or an audit event is generated).
3. Check Activity Explorer in Microsoft Purview for the corresponding event. Filter by 'Endpoint DLP' and the test user/device to confirm the activity is logged with the expected action.

## Rollback
1. Remove or modify the 'Access by restricted apps' rule in the Endpoint DLP policy. In Microsoft Purview compliance portal > Data Loss Prevention > Policies, edit the policy, locate the rule, and either delete the rule or change the action to 'Audit only' to stop blocking.
2. If the restricted apps list itself needs adjustment, navigate to Endpoint DLP settings (https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings) and modify the list of restricted apps.
3. Wait for policy propagation (up to 1 hour) and then verify that the previous behavior is restored by repeating the validation steps.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
