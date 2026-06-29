# Hardening: Microsoft Defender for Office 365

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Office 365
**Incident Type:** Hardening

## Scenario / Query
What is the recommended role assignment for accessing Microsoft Defender for Office 365 alerts to minimize security risks?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Microsoft Defender for Office 365

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use roles with fewer permissions for better security
2. Use the Global Administrator role only in emergencies when no other role fits

## Validation
1. Confirm that the user or service principal assigned to investigate alerts is not a Global Administrator. Run: Get-AzureADDirectoryRole | Where-Object {$_.DisplayName -eq 'Global Administrator'} | Get-AzureADDirectoryRoleMember | Select-Object DisplayName, UserPrincipalName. 2. Verify the assigned role has only the necessary permissions: Get-AzureADDirectoryRole | Where-Object {$_.DisplayName -eq 'Security Reader' -or $_.DisplayName -eq 'Security Operator' -or $_.DisplayName -eq 'Security Administrator'} | Get-AzureADDirectoryRoleMember | Select-Object DisplayName, UserPrincipalName. 3. Ensure no other high-privilege roles (e.g., Exchange Administrator, SharePoint Administrator) are assigned to the alert investigator. 4. Test alert access by navigating to https://security.microsoft.com/alerts and confirming the user can view alerts without errors.

## Rollback
1. If the user cannot access alerts after role change, temporarily assign the Global Administrator role: Add-AzureADDirectoryRoleMember -ObjectId <GlobalAdminRoleId> -RefObjectId <UserId>. 2. If the user was removed from a role, re-add them to the previous role: Add-AzureADDirectoryRoleMember -ObjectId <PreviousRoleId> -RefObjectId <UserId>. 3. Document the reason for rollback and escalate to security team for further analysis.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts>
