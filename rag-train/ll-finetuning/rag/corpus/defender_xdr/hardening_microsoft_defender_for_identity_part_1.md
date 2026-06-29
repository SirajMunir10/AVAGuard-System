# Hardening: Microsoft Defender for Identity

**Domain:** Defender XDR
**Subdomain:** Microsoft Defender for Identity
**Incident Type:** Hardening

## Scenario / Query
How can I harden my environment against NTLM relay attacks by configuring SMB signing and LDAP channel binding using Microsoft Defender for Identity recommendations?

## Environment Context
- **Tenant Type:** Enterprise hybrid Active Directory
- **Configuration:** Domain Controllers running Windows Server 2016 or later, with Microsoft Defender for Identity sensor installed and configured

## Symptoms
- Microsoft Defender for Identity alerts indicating potential NTLM relay or overpass-the-hash activity
- Security events 4624 (An account was successfully logged on) with LogonType 3 and elevated privileges from non-domain-joined machines

## Error Codes
N/A

## Root Causes
1. SMB signing not enforced on domain controllers
2. LDAP channel binding not enabled or not enforced
3. NTLM authentication not restricted where possible

## Remediation Steps
1. Enable SMB signing on all domain controllers via Group Policy: Computer Configuration > Windows Settings > Security Settings > Local Policies > Security Options > Microsoft network server: Digitally sign communications (always)
2. Enable LDAP channel binding and LDAP signing on all domain controllers via Group Policy: Computer Configuration > Administrative Templates > System > Directory Services > Domain controller > LDAP server signing requirements = 'Require signing' and LDAP server channel binding token requirements = 'Always'
3. Restrict NTLM authentication to domain controllers using Group Policy: Computer Configuration > Windows Settings > Security Settings > Local Policies > Security Options > Network security: Restrict NTLM: Incoming NTLM traffic = 'Deny all domain accounts' (or 'Deny all accounts' if feasible)

## Validation
Run the following PowerShell command on a domain controller to verify SMB signing is enabled: Get-SmbServerConfiguration | Select-Object RequireSecuritySignature. Confirm the value is True. For LDAP channel binding, check the registry key HKLM\System\CurrentControlSet\Services\NTDS\Parameters\LdapEnforceChannelBinding has a value of 2 (enforce).

## Rollback
Set SMB signing back to 'Disabled' via Group Policy, set LDAP server signing requirements to 'None', and change LDAP channel binding enforcement to 'Never' (registry value 0). Restrict NTLM policy can be set back to 'Allow all'.

## References
- <https://learn.microsoft.com/en-us/defender-for-identity/security-alerts>
- <https://learn.microsoft.com/en-us/defender-for-identity/hardening>
