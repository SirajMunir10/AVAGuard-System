# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How do I configure a DLP policy to detect and block paste of sensitive text into supported browsers?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with Paste to supported browsers condition

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the Paste to supported browsers condition to detect when a user attempts to paste sensitive text into a text field or web form using Microsoft Edge, Google Chrome with Microsoft Purview extension, or Mozilla Firefox with Microsoft Purview extension.
2. Configure the action to block, block with override, or audit when users paste sensitive information into a text field or web form.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Select the DLP policy configured with 'Paste to supported browsers' condition. 3. Verify the condition is set to 'Content is pasted from Microsoft 365 into a supported browser' and the action is set to 'Block' or 'Block with override' as intended. 4. As a test user, copy sensitive text (e.g., a credit card number) from a Microsoft 365 app (e.g., Outlook) and attempt to paste it into a text field in Microsoft Edge, Google Chrome with Microsoft Purview extension, or Mozilla Firefox with Microsoft Purview extension. 5. Confirm that the paste action is blocked (or shows a policy tip with override option) and an audit event is generated in Activity Explorer.

## Rollback
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Select the DLP policy that includes the 'Paste to supported browsers' condition. 3. Edit the policy and remove or disable the 'Paste to supported browsers' condition by unchecking it in the condition list. 4. Alternatively, change the action from 'Block' to 'Audit only' to stop blocking pastes while still logging. 5. Save the policy and confirm the change is applied. 6. Verify that users can now paste sensitive text into supported browsers without restriction.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
