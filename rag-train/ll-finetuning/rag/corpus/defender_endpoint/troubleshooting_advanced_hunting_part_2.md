# Troubleshooting: Advanced Hunting

**Domain:** Defender for Endpoint
**Subdomain:** Advanced Hunting
**Incident Type:** Troubleshooting

## Scenario / Query
Why can't a user access all advanced hunting data?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- User cannot access all advanced hunting data

## Error Codes
N/A

## Root Causes
1. User is not a member of one of the following Microsoft Entra roles: Global Administrator, Security Administrator, Security Reader, or Global Reader
2. User's access to endpoint data is not properly configured via role-based access control (RBAC) settings in Microsoft Defender for Endpoint

## Remediation Steps
1. Ensure the user is a member of one of the following Microsoft Entra roles: Global Administrator, Security Administrator, Security Reader, or Global Reader
2. Configure role-based access control (RBAC) settings in Microsoft Defender for Endpoint to grant access to endpoint data

## Validation
1. Confirm the user's Microsoft Entra role membership: run `Get-MgUserMemberOf -UserId <userPrincipalName> | Select-Object -ExpandProperty AdditionalProperties` and verify the user is assigned Global Administrator, Security Administrator, Security Reader, or Global Reader.
2. Verify RBAC permissions in Microsoft Defender for Endpoint: navigate to Microsoft 365 Defender > Settings > Endpoints > Permissions > Roles, select the role assigned to the user, and confirm that the role includes permissions to view endpoint data (e.g., 'View data - Endpoints').
3. Test advanced hunting access: sign in as the user, go to Microsoft 365 Defender > Hunting > Advanced Hunting, and run a sample query (e.g., `DeviceInfo | take 10`) to confirm results are returned.

## Rollback
1. Remove the user from the Microsoft Entra role: run `Remove-MgUserMemberOf -UserId <userPrincipalName> -DirectoryRoleId <roleId>` to revert role assignment.
2. Restore previous RBAC settings: in Microsoft Defender for Endpoint, edit the user's assigned role to remove the 'View data - Endpoints' permission or revert to the prior role configuration.
3. Confirm access is revoked: sign in as the user and verify that advanced hunting queries return no data or an access-denied message.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-overview>
