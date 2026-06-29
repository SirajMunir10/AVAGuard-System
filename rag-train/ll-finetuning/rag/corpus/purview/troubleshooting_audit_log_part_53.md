# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to search for Teams Shifts activities in the Microsoft 365 audit log?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Shifts app in Microsoft Teams enabled

## Symptoms
- Unable to find Shifts-related activities in audit log search
- Activities picker does not show Shifts activity group

## Error Codes
N/A

## Root Causes
1. Environment not configured to support Shifts apps

## Remediation Steps
1. Ensure your organization uses the Shifts app in Microsoft Teams
2. Configure environment to support Shifts apps so that the Activities picker includes the additional activity group for Shifts activities

## Validation
1. Confirm that the Shifts app is enabled in the Microsoft Teams admin center: navigate to Teams admin center > Teams apps > Manage apps, search for 'Shifts', and verify its status is 'Allowed'.
2. Verify that the audit log is capturing Shifts activities: run `Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-1) -EndDate (Get-Date) -Operations 'ShiftsScheduledShiftCreated','ShiftsScheduledShiftModified','ShiftsScheduledShiftDeleted'` in Exchange Online PowerShell.
3. In the Microsoft Purview compliance portal, go to Audit > Search, click 'Activities' picker, and confirm that 'Shifts activities' group appears under the 'Teams activities' section.

## Rollback
1. If the Shifts app was enabled and needs to be disabled: in Teams admin center > Teams apps > Manage apps, select Shifts, set 'Status' to 'Blocked', and click 'Save'.
2. If any custom audit log retention policies were modified, revert them to previous settings via the Purview compliance portal > Audit > Audit retention policies.
3. If the environment configuration change caused issues, restore the previous configuration from a backup or by reapplying the original settings documented in your change management records.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
