# Troubleshooting: Microsoft Entra Domain Services

**Domain:** Entra ID
**Subdomain:** Microsoft Entra Domain Services
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve a service principal alert in Microsoft Entra Domain Services related to credential synchronization?

## Environment Context
- **Tenant Type:** Microsoft Entra ID tenant with Domain Services enabled
- **Configuration:** Microsoft Entra Domain Services managed domain

## Symptoms
- Alert indicating issues with the service principal used for credential synchronization

## Error Codes
N/A

## Root Causes
1. The Microsoft Entra application used for credential synchronization may be missing or corrupted

## Remediation Steps
1. Install the Microsoft Graph PowerShell module: Install-Module Microsoft.Graph -Scope CurrentUser
2. Connect to Microsoft Graph with required permissions: Connect-MgGraph -Scopes 'Application.ReadWrite.All'
3. Retrieve the old application: $app = Get-MgApplication -Filter "DisplayName eq 'Azure AD Domain Services Sync'"
4. Delete the old application: Remove-MgApplication -ApplicationId $app.Id
5. After deletion, the Azure platform automatically recreates the application and resumes password synchronization

## Validation
The managed domain's health automatically updates itself within two hours and removes the alert

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/domain-services/alert-service-principal>
