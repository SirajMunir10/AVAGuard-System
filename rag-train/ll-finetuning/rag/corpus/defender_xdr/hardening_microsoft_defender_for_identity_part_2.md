# Hardening: Microsoft Defender for Identity

**Domain:** Defender XDR
**Subdomain:** Microsoft Defender for Identity
**Incident Type:** Hardening

## Scenario / Query
How do I harden Active Directory against DCSync attacks by configuring the 'Replicating Directory Changes' permission using Microsoft Defender for Identity recommendations?

## Environment Context
- **Tenant Type:** on-premises Active Directory integrated with Microsoft Defender for Identity
- **Configuration:** Domain controllers are monitored by Microsoft Defender for Identity sensors; the organization has not yet restricted the 'Replicating Directory Changes All' permission to only authorized accounts.

## Symptoms
- Microsoft Defender for Identity generates a security alert for 'Suspicious DCSync attack' or 'Directory Replication Services request'
- Unauthorized accounts are observed making replication requests to domain controllers

## Error Codes
N/A

## Root Causes
1. The 'Replicating Directory Changes' and 'Replicating Directory Changes All' permissions are granted to accounts that do not require them for legitimate replication purposes
2. Default Active Directory configuration allows members of the 'Pre-Windows 2000 Compatible Access' group to replicate directory changes

## Remediation Steps
1. Identify all accounts that have the 'Replicating Directory Changes' and 'Replicating Directory Changes All' permissions using Active Directory Users and Computers or PowerShell (Get-ACL on the domain root).
2. Remove these permissions from any accounts that are not authorized domain controllers or Microsoft tools (e.g., Azure AD Connect, Microsoft Entra Connect).
3. Ensure only the following accounts retain the permissions: Domain Controllers (for the domain), Enterprise Domain Controllers, and authorized service accounts (e.g., Azure AD Connect).
4. Monitor Microsoft Defender for Identity alerts to confirm no further unauthorized replication attempts.

## Validation
After applying the changes, verify that no new 'Suspicious DCSync attack' alerts appear in Microsoft Defender for Identity. Additionally, run the Microsoft Defender for Identity health check to confirm the configuration is compliant.

## Rollback
If legitimate replication fails, re-add the required accounts to the 'Replicating Directory Changes All' permission using the same ACL management tools.

## References
- <https://learn.microsoft.com/en-us/defender-for-identity/security-alerts#suspicious-dcsync-attack>
