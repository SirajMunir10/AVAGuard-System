# Troubleshooting: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Troubleshooting

## Scenario / Query
Why does Conditional Access policy with 'Require approved client app' fail when using Microsoft Edge InPrivate mode or WebViews hosted outside Microsoft Edge?

## Environment Context
- **Tenant Type:** Microsoft Entra ID tenant with Conditional Access policy requiring approved client app
- **Configuration:** Policy uses 'Require approved client app' grant

## Symptoms
- Conditional Access policy fails when using Microsoft Edge InPrivate mode
- App protection policies fail when app loads SharePoint in a webview hosted outside Microsoft Edge

## Error Codes
N/A

## Root Causes
1. Conditional Access cannot consider Microsoft Edge in InPrivate mode an approved client app
2. WebViews hosted outside of Microsoft Edge do not satisfy the approved client app policy

## Remediation Steps
1. Avoid using Microsoft Edge InPrivate mode when accessing resources protected by 'Require approved client app' policy
2. Ensure webviews used are hosted within Microsoft Edge or use approved client apps directly

## Validation
1. Confirm that the Conditional Access policy with 'Require approved client app' is assigned to the test user or group.
2. Attempt to access the protected resource (e.g., SharePoint Online) using Microsoft Edge InPrivate mode. Verify that access is blocked and a message indicating the client app is not approved appears.
3. Attempt to access the same resource using a non-Microsoft Edge WebView (e.g., a custom app that loads SharePoint in a WebView). Verify that access is blocked with a similar message.
4. As a positive control, access the resource using Microsoft Edge in normal (non-InPrivate) mode or using an approved client app (e.g., Microsoft Outlook mobile). Verify that access is granted.
5. Check the Microsoft Entra sign-in logs for the blocked attempts. Filter by user, application, and date. Confirm that the failure reason includes 'Client app is not approved' or equivalent.

## Rollback
1. If the remediation (avoiding InPrivate mode or non-Microsoft Edge WebViews) is not feasible, modify the Conditional Access policy to remove the 'Require approved client app' grant control. For example, change the grant to 'Require multifactor authentication' or 'Require device to be marked as compliant'.
2. Alternatively, create a new Conditional Access policy that excludes the affected users or apps from the 'Require approved client app' requirement, and assign a less restrictive grant control.
3. If the policy was recently changed, revert to the previous policy configuration using the Microsoft Entra admin center or PowerShell (e.g., `New-AzureADMSConditionalAccessPolicy` with the old settings).
4. Notify users that they can resume using InPrivate mode or WebViews, but note that the protected resource will no longer enforce the approved client app requirement.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant>
