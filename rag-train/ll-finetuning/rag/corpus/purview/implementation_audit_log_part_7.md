# Implementation: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Implementation

## Scenario / Query
How to audit Microsoft 365 Copilot admin activities using the Microsoft 365 audit log?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Access the Microsoft 365 audit log to record activities related to Microsoft 365 Copilot and Microsoft 365 Copilot Chat.
2. Use the audit log to see how and when users interact with Copilot, including the Microsoft service where the activity took place and references to files accessed during the interaction.
3. To access the text from the user's prompt during the interaction, use Content Search or view the AI interaction event from the activity explorer in Data Security Posture Management for AI.

## Validation
1. Run the following command in the Microsoft 365 Security & Compliance PowerShell: Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-1) -EndDate (Get-Date) -Operations 'CopilotInteraction','CopilotChatInteraction' -ResultSize 10. 2. Verify that the output includes entries with details such as UserId, Operation, AuditData (containing Copilot-specific fields like 'ServiceName' and 'FileReferences'). 3. Confirm that at least one entry shows a non-empty 'AuditData' field with a 'PromptText' or 'ResponseText' property (if available). 4. In the Microsoft Purview compliance portal, navigate to Audit > Search and run a search for the same date range and operations; confirm that the results match the PowerShell output and include AI interaction events.

## Rollback
1. If the audit log search returns no results or incomplete data, verify that audit logging is enabled: Get-AdminAuditLogConfig | Format-List UnifiedAuditLogIngestionEnabled. 2. If disabled, enable it: Set-AdminAuditLogConfig -UnifiedAuditLogIngestionEnabled $true. 3. If the issue persists, check that the user performing the search has the 'Audit Logs' role assigned (e.g., via the Compliance Center role groups). 4. As a last resort, contact Microsoft Support to confirm that the tenant is properly licensed for Purview Audit (Standard or Premium) and that Copilot events are being generated.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
