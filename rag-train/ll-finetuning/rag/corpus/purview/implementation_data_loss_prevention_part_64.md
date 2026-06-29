# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to configure DLP policy actions for forwarding messages to specific approvers?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with action 'Forward the message for approval to specific approvers'

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Note: Groups are not supported for this action.
2. Configure the DLP policy action: 'Forward the message for approval to specific approvers'.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Select the DLP policy that was configured. 3. Under 'Actions', verify that 'Forward the message for approval to specific approvers' is listed. 4. Confirm that the approver list contains only individual user email addresses (no groups). 5. Send a test email that triggers the DLP rule and verify the message is forwarded to the specified approver for approval.

## Rollback
1. In the DLP policy, edit the action by removing 'Forward the message for approval to specific approvers'. 2. If needed, replace with a different action such as 'Block the message' or 'Notify the sender with a policy tip'. 3. Save the policy and confirm the change is applied. 4. Send a test email to ensure the previous forwarding behavior is stopped.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
