# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to configure DLP policy rules including conditions, actions, user notifications, user overrides, incident reports, and additional options?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy configuration

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Define conditions that when matched trigger the policy.
2. Define actions that determine the activities included and outcomes of a match.
3. Configure user notifications to inform users when they trigger a policy and educate them on how the organization wants sensitive information treated.
4. Configure user overrides (when configured by an admin) to allow users to selectively override a blocking action.
5. Configure incident reports to notify admins and other key stakeholders when a rule match occurs.
6. Define additional options which define the priority for rule evaluation and can stop further rule and policy processing.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Select the newly created DLP policy and click 'Edit policy'. 3. Verify that the defined conditions (e.g., sensitive info types, content contains) are correctly listed under 'Locations and rules'. 4. Confirm that the specified actions (e.g., block access, restrict access) are applied to the rule. 5. Check that user notifications are enabled and the notification text matches the configured message. 6. Ensure user overrides are set to 'Allow override' or 'Require business justification' as intended. 7. Validate that incident reports are configured with the correct severity and recipients. 8. Review the 'Advanced DLP rules' section to confirm additional options (e.g., rule priority, stop processing more rules) are set.

## Rollback
1. In Microsoft Purview compliance portal > Data Loss Prevention > Policies, select the problematic DLP policy. 2. Click 'Edit policy' and navigate to the rule containing the issue. 3. To revert conditions, remove or modify the condition entries back to the previous state. 4. To revert actions, change the action settings (e.g., from 'Block' to 'Audit only'). 5. To revert user notifications, disable notifications or restore the original notification text. 6. To revert user overrides, set the override option to 'No override' or the previous setting. 7. To revert incident reports, adjust the severity or remove recipients. 8. To revert additional options, change the rule priority or uncheck 'Stop processing more rules'. 9. If the policy itself is causing issues, delete the policy and recreate it from a backup or previous configuration.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
