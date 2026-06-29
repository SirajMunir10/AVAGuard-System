# Hardening: Authentication Policies

**Domain:** Exchange Online
**Subdomain:** Authentication Policies
**Incident Type:** Hardening

## Scenario / Query
How do I harden Exchange Online by disabling legacy authentication protocols (Basic Auth) for all users and applications?

## Environment Context
- **Tenant Type:** Microsoft 365 enterprise tenant with Exchange Online
- **Configuration:** Exchange Online authentication policies and tenant-wide Basic Auth settings

## Symptoms
- Users or applications still able to authenticate using legacy protocols (POP3, IMAP4, SMTP AUTH, etc.) despite attempts to disable them
- Security alerts or reports showing Basic Auth usage in the tenant

## Error Codes
N/A

## Root Causes
1. Legacy authentication protocols are enabled at the tenant level or via individual authentication policies
2. No explicit block policy applied to disable Basic Auth for all protocols

## Remediation Steps
1. 1. Connect to Exchange Online PowerShell using the EXO V2 module.
2. 2. Run the cmdlet: Set-OrganizationConfig -DefaultAuthenticationPolicy "Block Basic Auth" (after creating the policy if it does not exist).
3. 3. Alternatively, disable Basic Auth per protocol using: Set-OrganizationConfig -DisableBasicAuth $true (this is a tenant-wide setting that disables Basic Auth for all protocols).
4. 4. Verify the change with: Get-OrganizationConfig | Format-List *BasicAuth*

## Validation
Run Get-OrganizationConfig | Format-List *BasicAuth* and confirm that all protocol-specific BasicAuthEnabled properties are set to False. Also check that the DefaultAuthenticationPolicy is applied and blocks Basic Auth.

## Rollback
Re-enable Basic Auth by running Set-OrganizationConfig -DisableBasicAuth $false, or remove the authentication policy by setting -DefaultAuthenticationPolicy $null.

## References
- <https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/disable-basic-authentication-in-exchange-online>
