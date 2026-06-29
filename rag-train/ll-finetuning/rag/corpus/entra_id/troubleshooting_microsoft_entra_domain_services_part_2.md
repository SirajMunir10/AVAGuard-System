# Troubleshooting: Microsoft Entra Domain Services

**Domain:** Entra ID
**Subdomain:** Microsoft Entra Domain Services
**Incident Type:** Troubleshooting

## Scenario / Query
How to re-register the Microsoft.AAD resource provider when application IDs 443155a6-77f3-45e3-882b-22b3a8d431fb, abba844e-bc0e-44b0-947a-dc74e5d09022, or d87dcbc6-a371-462e-88e3-28ad15ec4e64 are missing from the Microsoft Entra directory?

## Environment Context
- **Tenant Type:** Azure subscription with Microsoft Entra Domain Services managed domain
- **Configuration:** Microsoft.AAD resource provider

## Symptoms
- Application ID 443155a6-77f3-45e3-882b-22b3a8d431fb is missing from Microsoft Entra directory
- Application ID abba844e-bc0e-44b0-947a-dc74e5d09022 is missing from Microsoft Entra directory
- Application ID d87dcbc6-a371-462e-88e3-28ad15ec4e64 is missing from Microsoft Entra directory

## Error Codes
N/A

## Root Causes
1. The Microsoft.AAD resource provider is not registered or needs re-registration

## Remediation Steps
1. In the Azure portal, search for and select Subscriptions
2. Choose the subscription associated with your managed domain
3. From the left-hand navigation expand Settings, then select Resource Providers
4. Search for Microsoft.AAD, then select Re-register

## Validation
The managed domain's health automatically updates itself within two hours and removes the alert

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/domain-services/alert-service-principal>
