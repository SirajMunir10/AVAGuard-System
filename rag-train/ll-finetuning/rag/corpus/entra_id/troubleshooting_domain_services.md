# Troubleshooting: Domain Services

**Domain:** Entra ID
**Subdomain:** Domain Services
**Incident Type:** Troubleshooting

## Scenario / Query
How to check for missing service principals in Microsoft Entra ID for Azure AD Domain Services?

## Environment Context
- **Tenant Type:** Azure Global or other Azure clouds
- **Configuration:** Azure AD Domain Services

## Symptoms
- Missing service principal alert in Azure AD Domain Services

## Error Codes
N/A

## Root Causes
1. Service principal not found for Azure AD Domain Services

## Remediation Steps
1. In the Microsoft Entra admin center, search for and select Enterprise applications.
2. Choose All applications from the Application Type drop-down menu, then select Apply.
3. Search for each of the following application IDs: For Azure Global, search for AppId value 2565bd9d-da50-47d4-8b85-4c97f669dc36. For other Azure clouds, search for AppId value 6ba9a5d4-8456-4118-b521-9c5ca10cdf84.
4. If no existing application is found, follow the Resolution steps to create the service principal or re-register the namespace.
5. For AppId 2565bd9d-da50-47d4-8b85-4c97f669dc36: Recreate a missing service principal.
6. For AppId 443155a6-77f3-45e3-882b-22b3a8d431fb: Re-register the Microsoft.AAD namespace.
7. For AppId abba844e-bc0e-44b0-947a-dc74e5d09022: Re-register the Microsoft.AAD namespace.
8. For AppId d87dcbc6-a371-462e-88e3-28ad15ec4e64: Re-register the Microsoft.AAD namespace.

## Validation
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) as a Global Administrator. 2. Navigate to Identity > Applications > Enterprise applications. 3. Set 'Application type' to 'All applications' and select 'Apply'. 4. In the search box, enter AppId 2565bd9d-da50-47d4-8b85-4c97f669dc36 (for Azure Global) or 6ba9a5d4-8456-4118-b521-9c5ca10cdf84 (for other Azure clouds). 5. Confirm that an application with the matching AppId appears in the results. 6. Repeat the search for each of the following AppIds: 443155a6-77f3-45e3-882b-22b3a8d431fb, abba844e-bc0e-44b0-947a-dc74e5d09022, d87dcbc6-a371-462e-88e3-28ad15ec4e64. 7. Verify that all required service principals are listed. 8. In the Azure AD Domain Services resource, check that the 'Missing service principal' alert is no longer active.

## Rollback
1. If a service principal was recreated using the Resolution steps, delete the newly created service principal: a. In Enterprise applications, search for the AppId that was recreated. b. Select the application, then select 'Properties'. c. Set 'Enabled for users to sign-in?' to 'No' and save. d. Select 'Delete', confirm the deletion. 2. If the Microsoft.AAD namespace was re-registered, unregister it: a. In the Azure portal, navigate to Subscriptions, select the subscription used by Azure AD Domain Services. b. Go to Resource providers, search for 'Microsoft.AAD'. c. Select 'Microsoft.AAD' and choose 'Unregister'. 3. Wait a few minutes, then re-register the namespace only if required by the original remediation steps. 4. Verify that the 'Missing service principal' alert reappears in Azure AD Domain Services.

## References
- <https://learn.microsoft.com/en-us/entra/identity/domain-services/alert-service-principal>
