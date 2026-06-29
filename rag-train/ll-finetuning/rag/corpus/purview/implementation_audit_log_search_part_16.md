# Implementation: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Implementation

## Scenario / Query
How do I configure scoped access to audit logs using administrative units in Microsoft Purview?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Administrative units assigned to users in the Microsoft Purview portal

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Assign administrative units to users in the Microsoft Purview portal to restrict access to audit logs.
2. Use the Search-UnifiedAuditLog cmdlet to access scoped activity logs from any Microsoft service, including Exchange mailbox activity logs.
3. For unrestricted admin access, set administrative units to None (Default).
4. For restricted admin access, assign one or more administrative units to the admin.

## Validation
1. Sign in to the Microsoft Purview portal (https://purview.microsoft.com) with an account that has the Audit Logs role. 2. Navigate to Solutions > Audit > Search. 3. Verify that the audit log search results only show activities from users or resources within the assigned administrative units. 4. Run the following Exchange Online PowerShell command to confirm scoped access: Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-1) -EndDate (Get-Date) -ResultSize 10. 5. Confirm that the output does not include entries from users or resources outside the assigned administrative units.

## Rollback
1. Sign in to the Microsoft Purview portal (https://purview.microsoft.com) with an account that has the necessary permissions to modify administrative units. 2. Navigate to Roles & Scopes > Administrative units. 3. For each admin who needs unrestricted access, remove all assigned administrative units by selecting the admin and clicking 'Remove administrative unit'. 4. Alternatively, set the administrative unit assignment to 'None (Default)' for the admin. 5. Verify the change by running Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-1) -EndDate (Get-Date) -ResultSize 10 and confirming that audit log results now include all users and resources.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-search>
