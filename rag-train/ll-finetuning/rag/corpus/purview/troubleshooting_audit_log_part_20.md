# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate programmatic listing of restore items in a restore task in Microsoft 365 Backup?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit logging enabled

## Symptoms
- User programmatically got all artifacts in a restore task

## Error Codes
N/A

## Root Causes
1. User accessed GetAllRestoreArtifactsInTask

## Remediation Steps
1. Review the audit log for GetAllRestoreArtifactsInTask activity
2. Verify user permissions and access controls

## Validation
1. Run the following command in Exchange Online PowerShell to search the audit log for GetAllRestoreArtifactsInTask activity within the relevant time range:
   Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-7) -EndDate (Get-Date) -Operations GetAllRestoreArtifactsInTask -ResultSize 1000
2. Confirm that the output includes the expected user, timestamp, and details of the programmatic listing.
3. Verify that the user’s permissions are correctly scoped by checking the user’s role assignments in the Microsoft 365 Defender portal under Roles & scopes > Azure AD roles or custom roles.
4. Ensure that access controls (e.g., Conditional Access policies) are applied as intended by reviewing the sign-in logs for the user.

## Rollback
1. If the audit log review reveals unauthorized access, immediately revoke the user’s permissions by removing the relevant role assignment in the Microsoft 365 Defender portal or via PowerShell:
   Remove-RoleGroupMember -Identity "Backup Administrator" -Member user@contoso.com
2. If the issue is due to overly permissive access, adjust the user’s role to a more restrictive custom role that excludes the GetAllRestoreArtifactsInTask operation.
3. If the remediation caused service disruption, re-enable the user’s access by adding them back to the appropriate role group:
   Add-RoleGroupMember -Identity "Backup Administrator" -Member user@contoso.com
4. Monitor the audit log for any recurrence of the activity after rollback.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
