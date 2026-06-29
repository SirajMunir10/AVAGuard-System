# Troubleshooting: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot access issues when the DLP alert management dashboard shows 'Access to this page requires authorization'?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP alert management dashboard in Microsoft Purview portal

## Symptoms
- Access to this page requires authorization
- Prompt to sign in or change directories

## Error Codes
N/A

## Root Causes
1. Insufficient permissions to view DLP alerts

## Remediation Steps
1. Try signing in with appropriate credentials
2. Try changing directories to the correct tenant

## Validation
1. Sign in to the Microsoft Purview portal (https://purview.microsoft.com) using credentials that have the 'DLP Compliance Management' or 'Security Reader' role assigned. 2. Navigate to Data Loss Prevention > Alerts. 3. Confirm the DLP alert management dashboard loads without the 'Access to this page requires authorization' error. 4. Verify that the tenant directory shown in the portal matches the expected tenant (e.g., the tenant where DLP policies are configured). 5. If the error persists, run the following PowerShell command to check the current user's role assignments: Get-RoleGroupMember -Identity 'DLP Compliance Management' | Where-Object {$_.WindowsLiveID -eq (Get-MgUser -UserId (Get-MgContext).Account).UserPrincipalName}

## Rollback
1. If the user was assigned a new role to resolve the issue, remove that role assignment using: Remove-RoleGroupMember -Identity 'DLP Compliance Management' -Member <user@domain.com> -Confirm:$false. 2. If the user changed directories, sign out of the portal and sign back in using the original directory credentials. 3. If the user was using a different browser or incognito session, close that session and revert to the original browser profile. 4. If the issue persists after rollback, verify that the user's original permissions are intact by checking role assignments via Get-RoleGroupMember.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-learn>
