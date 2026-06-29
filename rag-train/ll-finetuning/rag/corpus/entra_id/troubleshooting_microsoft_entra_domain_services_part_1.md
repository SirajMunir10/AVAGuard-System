# Troubleshooting: Microsoft Entra Domain Services

**Domain:** Entra ID
**Subdomain:** Microsoft Entra Domain Services
**Incident Type:** Troubleshooting

## Scenario / Query
How to recreate a missing service principal for Microsoft Entra Domain Services when application ID 2565bd9d-da50-47d4-8b85-4c97f669dc36 is missing from the Microsoft Entra directory in Azure Global?

## Environment Context
- **Tenant Type:** Azure Global
- **Configuration:** Application ID 2565bd9d-da50-47d4-8b85-4c97f669dc36

## Symptoms
- Service principal with application ID 2565bd9d-da50-47d4-8b85-4c97f669dc36 is missing from Microsoft Entra directory

## Error Codes
N/A

## Root Causes
1. Service principal required for Microsoft Entra Domain Services has been deleted or is missing

## Remediation Steps
1. Install the Microsoft Graph PowerShell module: Install-Module Microsoft.Graph -Scope CurrentUser
2. Recreate the service principal using the New-MgServicePrincipal cmdlet: New-MgServicePrincipal -AppId "2565bd9d-da50-47d4-8b85-4c97f669dc36"

## Validation
The managed domain's health automatically updates itself within two hours and removes the alert.

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/domain-services/alert-service-principal>
