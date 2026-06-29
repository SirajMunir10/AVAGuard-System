# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
What are the specific audit log activities for Microsoft 365 Copilot admin actions?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** N/A

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Review the following activities recorded in the audit log:
2. Created a new Copilot plugin (CreatePlugin) - A user (or admin or system on behalf of a user) created a new Copilot plugin.
3. Created a new Copilot promptbook (CreatePromptBook) - A user (or admin or system on behalf of a user) created a new promptbook in Copilot.
4. Deleted a Copilot plugin (DeletePlugin) - A user (or admin or system on behalf of a user) deleted a Copilot plugin.
5. Deleted a Copilot promptbook (DeletePromptBook) - A user (or admin or system on behalf of a user) deleted a Copilot promptbook.
6. Disabled a Copilot plugin (DisableCopilotPlugin) - A user (or admin or system on behalf of a user) disabled a Copilot plugin.
7. Disabled a Copilot promptbook (DisablePromptBook) - A user (or admin or system on behalf of a user) disabled a Copilot promptbook.
8. Enabled a Copilot plugin (EnablePlugin) - A user (or admin or system on behalf of a user) enabled a Copilot plugin.
9. Enabled a Copilot promptbook (EnablePromptBook) - A user (or admin or system on behalf of a user) enabled a Copilot promptbook.
10. Exported AI Interactions (AIEnterpriseInteractionsExported) - An admin exported interactions with Copilot.
11. Interacted with Copilot (CopilotInteraction) - A user (or admin or system on behalf of a user) entered prompts in Copilot.
12. Sent change notification for AI interaction creation (AIInteractionCreatedNotification) - A change notification was sent to notify a subscribed listener application of a new Copilot AI interaction.
13. Sent change notification for AI interaction deletion (AIInteractionDeletedNotification) - A change notification was sent to notify a subscribed listener application of a deleted Copilot AI interaction.
14. Sent change notification for AI interaction update (AIInteractionUpdatedNotification) - A change notification was sent to notify a subscribed listener application of an updated Copilot AI interaction.
15. Subscribed to AI interactions (SubscribedToAIInteractions) - A subscription was created by a listener application to receive change notifications for Copilot AI interactions.

## Validation
1. Connect to Exchange Online PowerShell: Connect-ExchangeOnline -UserPrincipalName admin@contoso.com
2. Search the audit log for Copilot admin activities: Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-7) -EndDate (Get-Date) -Operations CreatePlugin, CreatePromptBook, DeletePlugin, DeletePromptBook, DisableCopilotPlugin, DisablePromptBook, EnablePlugin, EnablePromptBook, AIEnterpriseInteractionsExported, CopilotInteraction, AIInteractionCreatedNotification, AIInteractionDeletedNotification, AIInteractionUpdatedNotification, SubscribedToAIInteractions -ResultSize 1000 | Format-Table CreationDate, Operation, UserIds, AuditData
3. Verify that the expected activities appear in the results. If no results, expand the date range or check that audit logging is enabled.

## Rollback
1. If audit log search fails due to permissions, ensure the account has the Audit Log role in the Microsoft Purview compliance portal.
2. If audit logging is disabled, enable it: Set-AdminAuditLogConfig -UnifiedAuditLogIngestionEnabled $true
3. If the issue is that specific operations are missing, verify that the workload (Copilot) is licensed and enabled for the tenant.
4. If the search returns too many results, refine the query by adding more specific filters (e.g., UserIds, Item).

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
