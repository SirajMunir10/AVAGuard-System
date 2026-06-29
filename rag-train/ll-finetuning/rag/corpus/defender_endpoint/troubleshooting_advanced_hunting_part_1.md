# Troubleshooting: Advanced Hunting

**Domain:** Defender for Endpoint
**Subdomain:** Advanced Hunting
**Incident Type:** Troubleshooting

## Scenario / Query
Why can't a user access email data tables in advanced hunting?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- User cannot access email data tables in advanced hunting

## Error Codes
N/A

## Root Causes
1. User is not a member of the required Email & Collaboration role groups: Security Administrator, Security Operator, or Security Reader
2. User is not a member of the required Exchange Online role groups: View-Only Organization Management, View-Only Configuration, Security Reader, or Global Reader
3. User is not a member of the required Microsoft Entra roles: Global Administrator, Security Administrator, Security Reader, or Global Reader

## Remediation Steps
1. Ensure the user is a member of one of the following Email & Collaboration role groups: Security Administrator, Security Operator, or Security Reader
2. Ensure the user is a member of one of the following Exchange Online role groups: View-Only Organization Management, View-Only Configuration, Security Reader, or Global Reader
3. Ensure the user is a member of one of the following Microsoft Entra roles: Global Administrator, Security Administrator, Security Reader, or Global Reader

## Validation
1. Verify the user's Email & Collaboration role group membership: Connect to Exchange Online PowerShell and run 'Get-RoleGroupMember -Identity "Security Administrator" | Where-Object {$_.Name -eq "<user@domain.com>"}' (repeat for Security Operator and Security Reader). 2. Verify the user's Exchange Online role group membership: Run 'Get-RoleGroupMember -Identity "View-Only Organization Management" | Where-Object {$_.Name -eq "<user@domain.com>"}' (repeat for View-Only Configuration, Security Reader, and Global Reader). 3. Verify the user's Microsoft Entra role membership: Run 'Get-MgDirectoryRoleMember -DirectoryRoleId (Get-MgDirectoryRole -Filter "DisplayName eq 'Global Administrator'").Id | Where-Object {$_.AdditionalProperties.userPrincipalName -eq "<user@domain.com>"}' (repeat for Security Administrator, Security Reader, and Global Reader). 4. Have the user sign out and sign back in to Microsoft 365 Defender, then navigate to Advanced Hunting and attempt to query email data tables (e.g., EmailEvents, EmailAttachmentInfo, EmailUrlInfo).

## Rollback
1. If the user was added to a role group in error, remove the user from that role group: For Exchange Online role groups, run 'Remove-RoleGroupMember -Identity "<RoleGroupName>" -Member "<user@domain.com>" -Confirm:$false'. 2. If the user was added to a Microsoft Entra role in error, remove the user from that role: Run 'Remove-MgDirectoryRoleMember -DirectoryRoleId "<RoleId>" -DirectoryObjectId "<UserObjectId>"'. 3. If the user was added to multiple roles, repeat removal for each role. 4. Have the user sign out and sign back in to Microsoft 365 Defender to ensure role changes take effect.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-overview>
