# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify and investigate site permissions changes in the Microsoft 365 audit log?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- Unexpected changes to site permissions
- Users gaining or losing access to sites without clear reason

## Error Codes
N/A

## Root Causes
1. Site collection admin added or removed
2. User or group added to SharePoint group
3. Permission level inheritance broken
4. Sharing inheritance broken
5. Group created or deleted
6. Members Can Share setting modified
7. Access request setting modified
8. Permission level modified or removed

## Remediation Steps
1. Search audit log for SiteCollectionAdminAdded or SiteCollectionAdminRemoved events
2. Search audit log for AddedToGroup or GroupRemoved events
3. Search audit log for PermissionLevelsInheritanceBroken or SharingInheritanceBroken events
4. Search audit log for WebMembersCanShareModified or WebRequestAccessModified events
5. Search audit log for PermissionLevelModified or PermissionLevelRemoved events
6. Review the app@sharepoint user context for activities performed on behalf of users

## Validation
1. Go to Microsoft Purview compliance portal > Audit > Search audit log. 2. Set Date range to cover the incident period. 3. For each root cause, run a separate search: a) Activities: SiteCollectionAdminAdded, SiteCollectionAdminRemoved. b) Activities: AddedToGroup, GroupRemoved. c) Activities: PermissionLevelsInheritanceBroken, SharingInheritanceBroken. d) Activities: WebMembersCanShareModified, WebRequestAccessModified. e) Activities: PermissionLevelModified, PermissionLevelRemoved. 4. In each search, verify that the expected events appear with correct User, Item, and Date. 5. Confirm that no unexpected events of these types exist outside the remediation window. 6. Optionally, export the audit log results and review the app@sharepoint user context entries to ensure activities performed on behalf of users are legitimate.

## Rollback
1. If an unauthorized SiteCollectionAdminAdded event is found, remove the added admin: In SharePoint Admin Center > Active sites > select site > Permissions > Site collection administrators > remove the unauthorized user. 2. If an unauthorized AddedToGroup event is found, remove the user from the SharePoint group: In site Settings > Site permissions > select group > remove user. 3. If PermissionLevelsInheritanceBroken or SharingInheritanceBroken was unintended, restore inheritance: In site Settings > Site permissions > select the list/library > Permissions > Delete unique permissions > Inherit permissions. 4. If WebMembersCanShareModified was changed, revert the setting: In site Settings > Site permissions > Change sharing settings > select the original sharing level. 5. If WebRequestAccessModified was changed, revert the setting: In site Settings > Site permissions > Access requests > set to original value. 6. If PermissionLevelModified or PermissionLevelRemoved was unintended, recreate or restore the permission level: In site Settings > Site permissions > Permission Levels > Add a permission level or select a level and restore default settings. 7. For any app@sharepoint user context activity that is suspicious, review and revoke delegated permissions via Azure AD > Enterprise applications > SharePoint Online > Permissions.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
