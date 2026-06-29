# Troubleshooting: Password Writeback

**Domain:** Entra ID
**Subdomain:** Password Writeback
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve password writeback failure due to missing LDAP password policy control on domain controllers?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Password writeback enabled, Azure AD Connect sync

## Symptoms
- Event: MMS(3040): admaexport.cpp(2837): The server doesn't contain the LDAP password policy control

## Error Codes
N/A

## Root Causes
1. LDAP_SERVER_POLICY_HINTS_OID control (1.2.840.113556.1.4.2066) is not enabled on the domain controllers

## Remediation Steps
1. Ensure domain controllers are running Windows Server 2016 or later
2. Enable the LDAP_SERVER_POLICY_HINTS_OID control on the DCs

## Validation
1. Verify domain controller OS version: `Get-ADDomainController | Select-Object Name, OperatingSystem`
2. Confirm LDAP policy hints control is enabled: `Get-ADObject -SearchBase (Get-ADRootDSE).DefaultNamingContext -LDAPFilter '(objectClass=domainDNS)' -Properties * | Select-Object -ExpandProperty msDS-Other-Settings | Select-String '1.2.840.113556.1.4.2066'`
3. Test password writeback: Trigger a password reset from Entra ID and check for success events (Event ID 31002) in the Azure AD Connect server's Application log.

## Rollback
1. If domain controllers were upgraded, revert to previous OS version using backup or snapshot.
2. Disable the LDAP policy hints control: `Set-ADObject -Identity (Get-ADRootDSE).DefaultNamingContext -Remove @{'msDS-Other-Settings'='LDAP_SERVER_POLICY_HINTS_OID:1.2.840.113556.1.4.2066'}`
3. Restart the Azure AD Connect service: `Restart-Service -Name 'ADSync'`

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
