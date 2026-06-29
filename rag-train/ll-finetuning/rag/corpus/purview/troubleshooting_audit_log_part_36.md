# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to monitor changes to Send To connections for records management?

## Environment Context
- **Tenant Type:** SharePoint
- **Configuration:** Records management, Send To connections

## Symptoms
- Documents not being routed to the correct document repository or records center
- Content Organizer submissions failing

## Error Codes
N/A

## Root Causes
1. A SharePoint or global administrator created or deleted a Send To connection on the Records management page

## Remediation Steps
1. Review audit log for SendToConnectionAdded or SendToConnectionRemoved activity
2. Verify the settings of the Send To connection
3. Recreate the connection if it was deleted unintentionally

## Validation
1. Connect to the Microsoft Purview compliance portal using the Security & Compliance Center PowerShell module. Run: Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-90) -EndDate (Get-Date) -Operations 'SendToConnectionAdded', 'SendToConnectionRemoved' | Format-Table CreationTime, Operation, UserIds, ObjectId, ResultStatus -AutoSize. 2. Navigate to the Records management page in the Microsoft Purview compliance portal (https://compliance.microsoft.com/recordsmanagement). Select 'Send to connections' and verify that all expected connections are listed with correct settings (URL, label, etc.). 3. For each connection, test by submitting a document via Content Organizer or a manual send-to action to confirm routing to the correct repository.

## Rollback
1. If a Send To connection was unintentionally deleted, recreate it using the same settings as before: In the Microsoft Purview compliance portal, go to Records management > Send to connections > + Add. Enter the connection name, target URL (e.g., records center or document repository), and any required label or property mapping. 2. If a connection was incorrectly added, remove it by selecting the connection and clicking 'Delete' on the Send to connections page. 3. After changes, re-run the validation steps to confirm the correct state is restored.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
