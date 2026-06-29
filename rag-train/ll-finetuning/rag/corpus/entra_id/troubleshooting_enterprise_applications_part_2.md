# Troubleshooting: Enterprise Applications

**Domain:** Entra ID
**Subdomain:** Enterprise Applications
**Incident Type:** Troubleshooting

## Scenario / Query
Can't add another instance of the application

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Unable to add a second instance of an application

## Error Codes
N/A

## Root Causes
1. The application does not support configuring a unique identifier for the second instance
2. The application does not support configuring a different certificate than the one used for the first instance

## Remediation Steps
1. Configure a unique identifier for the second instance (cannot use the same identifier as the first instance)
2. Configure a different certificate than the one used for the first instance

## Validation
1. Sign in to the Entra admin center as a Global Administrator. 2. Browse to Identity > Applications > Enterprise applications. 3. Select the second instance of the application. 4. Under Manage, select Single sign-on. 5. In the SAML-based Sign-on section, confirm that the Identifier (Entity ID) is unique and does not match the identifier used for the first instance. 6. In the same section, confirm that the Certificate (Base64) or Thumbprint is different from the certificate used for the first instance. 7. Save the configuration and test the SSO flow to ensure the second instance works independently.

## Rollback
1. Sign in to the Entra admin center as a Global Administrator. 2. Browse to Identity > Applications > Enterprise applications. 3. Select the second instance of the application. 4. Under Manage, select Single sign-on. 5. Revert the Identifier (Entity ID) to the original value that was used before remediation. 6. Revert the Certificate (Base64) or Thumbprint to the original certificate that was used before remediation. 7. Save the configuration and verify that the first instance continues to function correctly.

## References
- <https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/troubleshoot-saml-based-sso>
