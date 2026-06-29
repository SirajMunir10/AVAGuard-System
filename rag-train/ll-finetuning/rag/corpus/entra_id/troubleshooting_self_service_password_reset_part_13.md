# Troubleshooting: Self-Service Password Reset (UserNotMemberOfScopedAccessGroup = 13)

**Domain:** Entra ID
**Subdomain:** Self-Service Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
A user sees error 'We're sorry, you can't reset your password at this time because your administrator hasn't configured your account to use password reset.' What is the cause and how to resolve?

## Environment Context
- **Tenant Type:** Microsoft Entra
- **Configuration:** User scoping for SSPR

## Symptoms
- User cannot reset password
- Error message: 'We're sorry, you can't reset your password at this time because your administrator hasn't configured your account to use password reset.'

## Error Codes
- `UserNotMemberOfScopedAccessGroup = 13`

## Root Causes
1. The user is not a member of the scoped access group for password reset.

## Remediation Steps
1. Contact your admin and ask them to configure your account for password reset.

## Validation
1. Confirm the user is not a member of the SSPR scoped group: `Get-MgGroupMember -GroupId "<SSPR_Group_Id>" | Where-Object {$_.Id -eq "<User_Object_Id>"}`. 2. Verify the user's authentication methods are registered: `Get-MgUserAuthenticationMethod -UserId "<User_Object_Id>"`. 3. Check SSPR policy scope in Entra admin center: Sign in to https://entra.microsoft.com > Protection > Password reset > Properties > ensure 'Selected' group includes the user's group.

## Rollback
1. If the user was added to the wrong group, remove them: `Remove-MgGroupMember -GroupId "<Group_Id>" -DirectoryObjectId "<User_Object_Id>"`. 2. If authentication methods were incorrectly modified, re-register required methods via https://aka.ms/ssprsetup. 3. If SSPR scope was changed, revert to previous group selection in Entra admin center > Protection > Password reset > Properties > Selected.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr>
