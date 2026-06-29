# Troubleshooting: Self-Service Password Reset

**Domain:** Entra ID
**Subdomain:** Self-Service Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
A user reports they cannot use SSPR and sees the error 'Your administrator has not enabled you to use this feature.' What are the possible causes and remediation steps?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** SSPR enabled for a group; nested groups supported; licensing required

## Symptoms
- User sees error: 'Your administrator has not enabled you to use this feature.'

## Error Codes
N/A

## Root Causes
1. User does not have a Microsoft Entra ID license assigned.
2. Only one Microsoft Entra group can currently be enabled for SSPR using the Microsoft Entra admin center.
3. Administrator performing configuration options may not have a license assigned.

## Remediation Steps
1. Ensure users in the groups you choose are assigned the appropriate licenses.
2. Review the previous troubleshooting step to enable SSPR as required.
3. Review troubleshooting steps to make sure that the administrator performing the configuration options has a license assigned.
4. To assign a license to the administrator account in question, follow the steps to Assign, verify, and resolve problems with licenses.

## Validation
1. Confirm the user has a valid Microsoft Entra ID license assigned: Run `Get-MgUserLicenseDetail -UserId <userPrincipalName>` in Microsoft Graph PowerShell. 2. Verify the user is a member of the SSPR-enabled group: Run `Get-MgGroupMember -GroupId <SSPRGroupId> | Where-Object {$_.Id -eq (Get-MgUser -UserId <userPrincipalName>).Id}`. 3. Ensure the administrator account used to configure SSPR has a license: Run `Get-MgUserLicenseDetail -UserId <adminUserPrincipalName>`. 4. Check that only one group is enabled for SSPR in the Microsoft Entra admin center: Navigate to Protection > Password reset > Properties and confirm the 'Self-service password reset enabled' setting is set to 'Selected' and only one group is listed.

## Rollback
1. If a license was incorrectly assigned, remove it: Run `Set-MgUserLicense -UserId <userPrincipalName> -RemoveLicenses @('<skuId>')`. 2. If the user was incorrectly added to the SSPR group, remove them: Run `Remove-MgGroupMember -GroupId <SSPRGroupId> -DirectoryObjectId <userId>`. 3. If the administrator's license was incorrectly assigned, remove it: Run `Set-MgUserLicense -UserId <adminUserPrincipalName> -RemoveLicenses @('<skuId>')`. 4. If a different group was mistakenly enabled for SSPR, revert to the original group: In the Microsoft Entra admin center, go to Protection > Password reset > Properties, set 'Self-service password reset enabled' to 'Selected', and choose the correct group.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr>
