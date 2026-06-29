# Implementation: Admin Takeover

**Domain:** Entra ID
**Subdomain:** Admin Takeover
**Incident Type:** Implementation

## Scenario / Query
How to perform an admin takeover of an unmanaged directory using Power BI self-service sign-up?

## Environment Context
- **Tenant Type:** unmanaged
- **Configuration:** self-service sign-up enabled

## Symptoms
- Unmanaged directory exists with no global admin
- User accounts created via self-service subscriptions (e.g., Power BI)

## Error Codes
N/A

## Root Causes
1. No global administrator assigned to the tenant
2. Self-service user subscription created the unmanaged account

## Remediation Steps
1. Go to the Power BI site and select Start Free > Start free trial (in Share with Power BI Pro box)
2. Sign up with a user account that uses the domain name of your organization (like powerbiadmin@contoso.com)
3. If your account is already in use, sign in by using your current password
4. Check your email for the verification code and enter the code to validate your email address

## Validation
1. Sign in to https://admin.microsoft.com with the account used during the takeover (e.g., powerbiadmin@contoso.com).
2. Navigate to Users > Active users and verify that the account has the Global administrator role assigned.
3. Confirm that the tenant is no longer listed as 'unmanaged' by checking the organization profile in the Microsoft 365 admin center.
4. Run the following PowerShell command to verify the tenant has at least one Global administrator:
   Connect-MgGraph -Scopes 'Directory.Read.All'
   Get-MgDirectoryRole -Filter "displayName eq 'Global Administrator'" | Get-MgDirectoryRoleMember

## Rollback
1. If the takeover fails or causes issues, contact Microsoft Support to request a domain takeover reset or to recover the tenant.
2. If the account used for takeover is compromised, immediately reset its password and revoke any suspicious sessions via the Microsoft 365 admin center.
3. As a last resort, if the tenant remains unmanaged and no Global administrator can be assigned, consider deleting the tenant via Azure AD (requires verified domain ownership and support intervention).
4. Document the incident and escalate to Microsoft Support for further assistance.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/admin/misc/become-the-admin>
