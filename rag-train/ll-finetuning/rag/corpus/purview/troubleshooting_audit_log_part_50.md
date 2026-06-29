# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify when sharing inheritance is restored for an item in audit logs?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log search enabled

## Symptoms
- Item inherits sharing permissions from its parent after a change

## Error Codes
N/A

## Root Causes
1. A change was made to restore inheritance

## Remediation Steps
1. Search for all activities in the audit log
2. Look for the activity 'Restored sharing inheritance' with the operation 'SharingInheritanceReset'

## Validation
1. Go to Microsoft Purview compliance portal > Audit > Search. 2. Set the Date range to cover the time of the change. 3. In the Activities list, select 'Restored sharing inheritance' (operation 'SharingInheritanceReset'). 4. Run the search and confirm that at least one audit record appears with the operation 'SharingInheritanceReset' and the affected item's details.

## Rollback
1. In the same audit search, locate the specific 'SharingInheritanceReset' event for the item. 2. Note the item's path and the previous inheritance state. 3. To revert, break inheritance for that item (e.g., via SharePoint UI or PowerShell: `Set-PnPListItem -List 'Documents' -Identity 'itemId' -BreakRoleInheritance`). 4. Confirm the item no longer inherits permissions by checking its unique permissions in the site settings.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
