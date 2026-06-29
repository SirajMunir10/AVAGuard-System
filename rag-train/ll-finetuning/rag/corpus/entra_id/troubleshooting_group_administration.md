# Troubleshooting: Group Administration

**Domain:** Entra ID
**Subdomain:** Group Administration
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify group administration activities recorded in the Microsoft 365 audit log?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- Need to review group creation, deletion, or membership changes
- Audit log contains group administration events

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Search the audit log for group administration activities such as 'Added group', 'Added member to group', 'Deleted group', 'Removed member from group', 'Updated group'
2. Use the Microsoft 365 admin center or Azure management portal to view audit log entries

## Validation
1. Sign in to the Microsoft 365 admin center (https://admin.microsoft.com) with appropriate permissions. 2. Navigate to 'Audit' under 'Security & Compliance' or go directly to the Microsoft Purview compliance portal (https://compliance.microsoft.com). 3. In the audit log search, set the 'Activities' filter to include group administration activities: 'Added group', 'Added member to group', 'Deleted group', 'Removed member from group', 'Updated group'. 4. Set the date range to cover the period of interest. 5. Run the search and confirm that the expected group administration events appear in the results. 6. Optionally, use the Azure portal (https://portal.azure.com) > 'Microsoft Entra ID' > 'Audit logs' and filter by 'Activity' for group-related operations to cross-verify.

## Rollback
1. If the audit log search returns no results or incorrect data, verify that audit logging is enabled in the Microsoft 365 organization (Settings > Org settings > Security & privacy > Audit log). 2. Ensure the user account performing the search has the 'Audit Logs' role or equivalent permissions (e.g., Global Administrator, Compliance Administrator, or Audit Administrator). 3. Check the date range and time zone settings in the audit log search; adjust if necessary. 4. If using the Azure portal, confirm that the directory is the correct tenant and that the 'Activity' filter includes the exact group operation names. 5. As a fallback, use the Search-UnifiedAuditLog cmdlet in Exchange Online PowerShell with the same activity filters to retrieve the events. 6. If no events are found, consider that group administration activities may not have occurred in the selected timeframe or that audit log retention policies have expired.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
