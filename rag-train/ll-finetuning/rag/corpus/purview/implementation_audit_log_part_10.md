# Implementation: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Implementation

## Scenario / Query
What Viva Engage activities are recorded in the Microsoft 365 audit log?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit (Premium) activities are highlighted with an asterisk (*)

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Added corporate communicator: AddUserRole - A user is assigned as a corporate communicator.
2. Changed custom usage policy: UsagePolicyUpdated - A tenant admin updates a custom usage policy.
3. Changed data retention policy: SoftDeleteSettingsUpdated - Verified admin updates the setting for the network data retention policy to either Hard Delete or Soft Delete.
4. Changed network configuration: NetworkConfigurationUpdated - Network or verified admin changes the Viva Engage network's configuration.
5. Changed network profile settings: ProcessProfileFields - Network or verified admin changes the information that appears on member profiles for network users.
6. Changed private content mode: SupervisorAdminToggled - Verified admin turns Private Content Mode on or off.
7. Changed security configuration: NetworkSecurityConfigurationUpdated - Verified admin updates the Viva Engage network's security configuration.
8. Conversation closed: CloseConversation - The Viva Engage thread was closed, preventing users from replying to it.
9. Conversation opened: OpenConversation - The Viva Engage thread conversation was opened which allows users to reply to the thread.
10. Create a segment: SegmentCreated - Admin creates a segmentation.
11. Created file: FileCreated - User uploads a file.
12. Created group: GroupCreation - User creates a group.
13. Created message: MessageCreation - User creates a message.
14. Delete a segment: SegmentDeleted - Admin deletes a segmentation.
15. Deleted group: GroupDeletion - A group is deleted from Viva Engage.
16. Deleted message: MessageDeleted - User deletes a message.
17. Download segmentation admin reports: SegmentationReportDownloaded - Admin reports are downloaded.

## Validation
1. Run the following command in Exchange Online PowerShell to search the audit log for Viva Engage activities: Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-7) -EndDate (Get-Date) -Operations AddUserRole, UsagePolicyUpdated, SoftDeleteSettingsUpdated, NetworkConfigurationUpdated, ProcessProfileFields, SupervisorAdminToggled, NetworkSecurityConfigurationUpdated, CloseConversation, OpenConversation, SegmentCreated, FileCreated, GroupCreation, MessageCreation, SegmentDeleted, GroupDeletion, MessageDeleted, SegmentationReportDownloaded -ResultSize 1000. 2. Verify that the output includes records for each of the listed operations, confirming that these activities are being captured in the audit log. 3. For Audit (Premium) activities (marked with * in the documentation), confirm that the AuditLogId field is populated and the record includes extended properties.

## Rollback
1. If the remediation introduced unintended changes to audit log capture, restore the previous audit log configuration by reverting any modified audit policies or settings. 2. If custom usage policies or data retention policies were changed, restore them to their previous state using the Viva Engage admin center or PowerShell cmdlets (e.g., Set-VivaEngagePolicy). 3. If network configuration or security configuration was altered, revert to the prior configuration using the Viva Engage admin center. 4. If segments were created or deleted, remove or recreate them as needed via the Viva Engage admin center. 5. If groups or messages were deleted, restore them from the Viva Engage recycle bin or backup if available. 6. If private content mode was toggled, switch it back to the previous setting. 7. If a conversation was closed or opened, reopen or close it as appropriate.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
