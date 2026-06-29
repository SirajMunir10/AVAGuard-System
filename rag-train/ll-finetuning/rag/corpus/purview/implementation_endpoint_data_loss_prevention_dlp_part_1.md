# Implementation: Endpoint Data Loss Prevention (DLP)

**Domain:** Purview
**Subdomain:** Endpoint Data Loss Prevention (DLP)
**Incident Type:** Implementation

## Scenario / Query
How to configure DLP policy actions for copying protected files to clipboard on onboarded devices?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP settings, onboarded Windows devices

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the 'Copy to clipboard' condition in DLP policy to detect when a user copies information from a protected file to the clipboard.
2. Select one of the following actions: Audit only, Block with override, or Block the activity.

## Validation
1. Open Microsoft Purview compliance portal (https://compliance.microsoft.com).
2. Navigate to Data Loss Prevention > Policies.
3. Select the DLP policy that was configured for endpoint devices.
4. Under 'Locations', confirm that 'Devices' is included and the correct onboarded Windows device groups are selected.
5. Under 'Rules', verify that a rule contains the condition 'Content is copied to clipboard' (or 'Copy to clipboard' as per the UI).
6. Confirm that the action for that rule is set to one of: 'Audit only', 'Block with override', or 'Block the activity'.
7. On a test onboarded Windows device, open a protected file (e.g., a document labeled as confidential) and attempt to copy content to the clipboard.
8. Verify that the configured action is enforced: if 'Block with override' or 'Block the activity' is selected, the copy should be blocked or show a policy tip; if 'Audit only', the copy should succeed but an audit event should be generated.
9. Check the DLP activity explorer for the test event to confirm the action was logged correctly.

## Rollback
1. In Microsoft Purview compliance portal, navigate to Data Loss Prevention > Policies.
2. Select the DLP policy that was modified.
3. Under 'Rules', locate the rule that contains the 'Copy to clipboard' condition.
4. Either remove the rule entirely, or change the action to 'Audit only' (least restrictive) to stop blocking.
5. If the policy was newly created, delete the entire policy.
6. Save the policy changes and wait for replication (typically up to 1 hour).
7. On a test onboarded Windows device, verify that copying from protected files to clipboard is no longer blocked or audited as per the original configuration.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
