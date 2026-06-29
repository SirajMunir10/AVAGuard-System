# Implementation: Device Identity

**Domain:** Entra ID
**Subdomain:** Device Identity
**Incident Type:** Implementation

## Scenario / Query
What are the prerequisites for Microsoft Entra hybrid join on downlevel Windows devices?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Downlevel Windows devices (Windows 8.1, Windows Server 2008 R2, Windows Server 2012, Windows Server 2012 R2)

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Configure AD FS for federated domains or Seamless SSO for managed domains
2. Ensure Service Connection Point (SCP) is configured correctly (for federated domains, point to federated domain name, not managed domain name)
3. Install KB4284842 on Windows 7 SP1 or Windows Server 2008 R2 SP1

## Validation
1. Verify that the Service Connection Point (SCP) is configured correctly by running the following command on a domain-joined machine: `certutil -scinfo` and checking that the SCP value matches the federated domain name (e.g., `adfs.contoso.com`) for federated domains, or the managed domain name (e.g., `contoso.onmicrosoft.com`) for managed domains. 2. For downlevel devices, confirm that the required update KB4284842 is installed by running `wmic qfe list brief /format:texttable` and verifying the presence of KB4284842 in the list. 3. Test hybrid join by signing in with a domain user on a downlevel device and running `dsregcmd /status` to confirm the device state shows `AzureAdJoined : YES` and `DomainJoined : YES`.

## Rollback
1. If SCP was misconfigured, revert to the previous SCP value using ADSI Edit or by restoring the original configuration from backup. 2. If Seamless SSO was enabled, disable it by running `Set-AADSSOConfig -Enable $false` in the Azure AD module. 3. If KB4284842 was installed and causes issues, uninstall it via Control Panel > Programs > View Installed Updates, or by running `wusa /uninstall /kb:4284842`.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-legacy>
