# Troubleshooting: Enterprise Applications

**Domain:** Entra ID
**Subdomain:** Enterprise Applications
**Incident Type:** Troubleshooting

## Scenario / Query
Where do I set the EntityID (User Identifier) format for SAML-based SSO in Microsoft Entra ID?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** SAML-based single sign-on configuration for enterprise applications

## Symptoms
- Unable to select the EntityID (User Identifier) format in Microsoft Entra ID for SAML responses

## Error Codes
N/A

## Root Causes
1. Microsoft Entra ID selects the format for the NameID attribute (User Identifier) based on the value selected or the format requested by the application in the SAML AuthRequest

## Remediation Steps
1. Review the SAML AuthRequest from the application to understand the requested NameID format
2. Configure the application to request the desired NameID format in the SAML AuthRequest
3. Refer to the article 'Single sign-on SAML protocol' under the section 'NameIDPolicy' for more information

## Validation
1. Use a SAML tracer or browser developer tools to capture the SAML AuthRequest sent by the application to Microsoft Entra ID. 2. In the AuthRequest, locate the <NameIDPolicy> element and verify the Format attribute (e.g., urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress). 3. Confirm that the Format value matches the desired User Identifier format. 4. In the Microsoft Entra admin center, navigate to Enterprise applications > select the application > Single sign-on > Attributes & Claims. 5. Under 'Required claim', verify that the 'Source attribute' for the Name identifier claim is set to the appropriate user attribute (e.g., user.mail) that corresponds to the requested format.

## Rollback
1. If the application's SAML AuthRequest was modified to request a different NameID format, revert the application configuration to its original AuthRequest settings. 2. In the Microsoft Entra admin center, go to Enterprise applications > select the application > Single sign-on > Attributes & Claims. 3. Under 'Required claim', reset the 'Source attribute' for the Name identifier claim to the previous value (e.g., user.userprincipalname). 4. Save the changes and test the SSO flow again to ensure the original behavior is restored.

## References
- <https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/troubleshoot-saml-based-sso>
