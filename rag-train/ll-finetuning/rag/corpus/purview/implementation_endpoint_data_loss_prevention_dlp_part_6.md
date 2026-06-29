# Implementation: Endpoint Data Loss Prevention (DLP)

**Domain:** Purview
**Subdomain:** Endpoint Data Loss Prevention (DLP)
**Incident Type:** Implementation

## Scenario / Query
How to configure restricted app activities in Endpoint DLP to block access by unallowed apps?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP settings, restricted apps list

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Define restricted apps in a list in Endpoint DLP settings.
2. When a user attempts to access a DLP protected file using an app on the list, select one of the following actions: Audit only, Block with override, or Block the activity.
3. Note: DLP actions defined in Restricted app activities are overridden if the app is a member of a restricted app group; then the actions defined in the restricted app group are applied.

## Validation
1. Confirm that the restricted app list is populated: Run `Get-DlpCompliancePolicy -Identity "YourPolicyName" | Format-List` in Exchange Online PowerShell to verify the 'RestrictedApps' parameter contains the intended app names.
2. Validate the action for restricted apps: Use `Get-DlpComplianceRule -Policy "YourPolicyName" | Where-Object {$_.RestrictedAppActivities -ne $null} | Format-List Name,RestrictedAppActivities` to ensure the rule has the correct action (AuditOnly, BlockWithOverride, or Block).
3. Test the policy: Attempt to access a DLP-protected file using an app listed in the restricted apps list and confirm the expected behavior (e.g., block or audit).
4. Check audit logs: In the Microsoft 365 Defender portal, go to Audit > Search and look for DLP rule matches to verify the action was triggered.

## Rollback
1. Remove apps from the restricted app list: Run `Set-DlpCompliancePolicy -Identity "YourPolicyName" -RestrictedApps @{Remove="AppName1","AppName2"}` in Exchange Online PowerShell.
2. Reset the action for restricted app activities: Use `Set-DlpComplianceRule -Identity "YourRuleName" -RestrictedAppActivities $null` to clear the action.
3. If the policy was blocking legitimate access, temporarily disable the rule: Run `Set-DlpComplianceRule -Identity "YourRuleName" -State Disabled`.
4. Monitor user feedback and audit logs to confirm the rollback resolved the issue.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
