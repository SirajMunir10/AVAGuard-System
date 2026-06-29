# Implementation: Endpoint Data Loss Prevention (DLP)

**Domain:** Purview
**Subdomain:** Endpoint Data Loss Prevention (DLP)
**Incident Type:** Implementation

## Scenario / Query
How to configure restricted app groups in Endpoint DLP policies?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP settings, restricted app groups

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Define restricted app groups in Endpoint DLP settings.
2. Add restricted app groups to your policies.
3. When adding a restricted app group to a policy, select one of these options: Don't restrict file activity, Apply restrictions to all activity, or Apply restrictions to specific activity.
4. When selecting either of the Apply restrictions options, and a user attempts to access a DLP protected file using an app in the restricted app group, select one of the following actions: Audit only, Block with override, or Block by activity.
5. Note: DLP actions defined here override actions defined in Restricted app activities and File activities for all apps for the app.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Endpoint DLP settings > Restricted app groups. 2. Confirm the restricted app group is listed with the correct apps. 3. Open the DLP policy that includes the restricted app group and verify the action selected (e.g., 'Block with override') under 'Restricted app activities'. 4. On a test endpoint, attempt to open a DLP-protected file using an app in the restricted group and confirm the expected action (e.g., block with override prompt) occurs. 5. Check DLP activity explorer for the test event showing the action taken.

## Rollback
1. In Microsoft Purview compliance portal > Data Loss Prevention > Endpoint DLP settings > Restricted app groups, remove the app group or edit its membership. 2. In the DLP policy, change the action for the restricted app group to 'Don't restrict file activity' or remove the group from the policy. 3. Save the policy and allow up to 1 hour for changes to propagate. 4. On a test endpoint, verify that the previously restricted app can now access DLP-protected files without restriction.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
