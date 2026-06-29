# Implementation: Automatic Attack Disruption

**Domain:** Defender for Endpoint
**Subdomain:** Automatic Attack Disruption
**Incident Type:** Implementation

## Scenario / Query
How does the Disable user action in automatic attack disruption behave for different user hosting environments (Active Directory, synced, or cloud-native)?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Defender for Identity sensor deployment, Microsoft Entra ID integration

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. For user accounts hosted in Active Directory: Defender for Identity triggers the disable user action on domain controllers running the Defender for Identity sensor.
2. For user accounts hosted in Active Directory and synced to Microsoft Entra ID: Defender for Identity triggers the disable user action via onboarded domain controllers, and attack disruption also disables the user account in Microsoft Entra ID.
3. For user accounts hosted in Microsoft Entra ID only (cloud-native account): Defender for Identity executes the disable user action in Microsoft Entra ID by using a Microsoft-managed enterprise application. This application validates the signed-in user's assigned roles and permissions through role-based access control (RBAC) before the account is disabled. The enterprise application is named Microsoft Defender for Identity and uses application ID 60ca1954-583c-4d1f-86de-39d835f3e452. In older tenants, this application might appear as Radius Aad Syncer.

## Validation
1. For AD-only users: On a domain controller with the Defender for Identity sensor, run 'Get-ADUser -Identity <username> | Select-Object Enabled' to confirm the account is disabled. 2. For synced users: Run the same AD command and also check in Microsoft Entra ID via 'Get-MgUser -UserId <userPrincipalName> | Select-Object AccountEnabled' to confirm both are disabled. 3. For cloud-native users: In Microsoft Entra ID, run 'Get-MgUser -UserId <userPrincipalName> | Select-Object AccountEnabled' to confirm the account is disabled. 4. Verify the enterprise application 'Microsoft Defender for Identity' (App ID 60ca1954-583c-4d1f-86de-39d835f3e452) exists in the tenant and has appropriate permissions assigned.

## Rollback
1. For AD-only users: On a domain controller, run 'Enable-ADAccount -Identity <username>' to re-enable the account. 2. For synced users: Re-enable the AD account with 'Enable-ADAccount -Identity <username>' and then trigger a sync or wait for the next sync cycle to re-enable the Microsoft Entra ID account. 3. For cloud-native users: In Microsoft Entra ID, run 'Update-MgUser -UserId <userPrincipalName> -AccountEnabled $true' to re-enable the account. 4. If the enterprise application was removed or permissions altered, re-create or re-grant permissions per the Defender for Identity documentation.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption>
