# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to configure policy override options for DLP policies to allow users to bypass restrictions for valid business needs or false positives?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with user notifications enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Give people the option to override the policy, so that they're not blocked if they have a valid business need or if the policy is detecting a false positive.
2. Configure user notifications and policy tips to include an 'Allow' button for bypassing the policy.

## Validation
1. Open the Microsoft Purview compliance portal (https://compliance.microsoft.com).
2. Navigate to Data Loss Prevention > Policies and select the DLP policy that was configured with override options.
3. Click 'Edit policy' and go to the 'User notifications' section.
4. Verify that 'Notify users in Office 365 with a policy tip' is enabled.
5. Confirm that the policy tip includes an 'Allow' button or override option by checking the 'Override the rule' or 'Allow override' checkbox.
6. As a test user, send an email or share a file that matches the DLP rule. Observe that a policy tip appears with an option to override (e.g., 'Allow' or 'Override').
7. Click the override option and confirm that the action is permitted and logged in the DLP reports (Activity explorer).

## Rollback
1. Open the Microsoft Purview compliance portal (https://compliance.microsoft.com).
2. Navigate to Data Loss Prevention > Policies and select the DLP policy where override options were added.
3. Click 'Edit policy' and go to the 'User notifications' section.
4. Uncheck the 'Override the rule' or 'Allow override' checkbox to remove the override option.
5. If the policy tip text was customized, revert it to the default or remove any instructions about overriding.
6. Save the policy and wait for it to replicate (up to 1 hour).
7. Test by triggering the DLP rule again to confirm that users are now blocked without an override option.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
