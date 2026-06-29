# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How do I configure restricted app groups in endpoint DLP settings to allow specific apps and block all others?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP settings, Restricted Apps and app groups

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Go to endpoint DLP settings.
2. Define allowed or sanctioned apps in the Restricted Apps and app groups list.
3. In your existing or new endpoint DLP policy, locate the File activities for apps in restricted app groups setting.
4. Add the desired restricted app group.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Endpoint DLP settings > Restricted Apps and app groups. Confirm the desired app group is listed with the correct apps. 2. Create or edit an endpoint DLP policy, go to 'File activities for apps in restricted app groups', and verify the restricted app group is selected. 3. On a test endpoint, attempt to copy sensitive data to an app NOT in the restricted group; confirm the action is blocked. 4. Attempt to copy sensitive data to an app that IS in the restricted group; confirm the action is allowed (if policy permits).

## Rollback
1. In Microsoft Purview > Data Loss Prevention > Endpoint DLP settings > Restricted Apps and app groups, remove the newly added app group or edit it to remove specific apps. 2. In the associated endpoint DLP policy, under 'File activities for apps in restricted app groups', remove the restricted app group or change its action to 'Audit only' or 'Block'. 3. On a test endpoint, verify that the previous blocking behavior is reverted (e.g., copying to previously blocked apps is no longer restricted). 4. If the policy change caused unintended blocks, disable the policy temporarily or set it to 'Audit mode'.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
