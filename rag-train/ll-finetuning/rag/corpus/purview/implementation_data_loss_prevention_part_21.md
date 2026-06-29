# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to implement a DLP policy using the Custom policy template to build a policy when none of the predefined templates meet organizational needs?

## Environment Context
- **Tenant Type:** Purview
- **Configuration:** DLP policy templates

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select the Custom policy template from the list of predefined templates.
2. Use this template to build your own policy if none of the others meet your organization's needs.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Confirm the custom DLP policy appears in the list with status 'Enabled' or 'Test'. 3. Open the policy and verify the configured rules, conditions, and actions match the intended design. 4. Optionally, use the 'Test' mode to simulate policy evaluation and confirm expected alerts or actions are triggered without enforcement.

## Rollback
1. In Microsoft Purview compliance portal > Data Loss Prevention > Policies, select the custom DLP policy. 2. Click 'Delete policy' and confirm deletion. 3. If the policy was in test mode, ensure no residual test data remains by reviewing the Activity explorer for any test events. 4. Alternatively, disable the policy by setting its status to 'Disabled' if deletion is not desired.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
