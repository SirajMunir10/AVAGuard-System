# Troubleshooting: Enterprise Applications

**Domain:** Entra ID
**Subdomain:** Enterprise Applications
**Incident Type:** Troubleshooting

## Scenario / Query
How to download Microsoft Entra metadata or certificate for SAML SSO configuration when the metadata URL is not available?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** SAML-based single sign-on for enterprise applications

## Symptoms
- Cannot find the Microsoft Entra metadata to complete the configuration with the application

## Error Codes
N/A

## Root Causes
1. Microsoft Entra does not provide a URL to get the metadata; the metadata can only be retrieved as an XML file

## Remediation Steps
1. Sign in to the Microsoft Entra admin center as at least a Cloud Application Administrator
2. Browse to Entra ID > Enterprise apps > All applications
3. Select the application you configure for single sign-on
4. Once the application loads, select Single sign-on from the application's left-hand navigation menu
5. Go to SAML Signing Certificate section, then select Download column value
6. Depending on what the application requires configuring single sign-on, you see either the option to download the Metadata XML or the Certificate

## Validation
1. Sign in to the Microsoft Entra admin center as at least a Cloud Application Administrator. 2. Browse to Identity > Applications > Enterprise applications > All applications. 3. Select the application you configured for single sign-on. 4. From the application's left-hand navigation menu, select Single sign-on. 5. In the SAML Signing Certificate section, confirm that the Download column contains either 'Metadata XML' or 'Certificate (Base64 or Raw)'. 6. Click the download link and verify that the file is downloaded successfully and contains valid XML or certificate content.

## Rollback
1. If the metadata or certificate download fails or the file is corrupted, sign in to the Microsoft Entra admin center as at least a Cloud Application Administrator. 2. Browse to Identity > Applications > Enterprise applications > All applications. 3. Select the same application. 4. From the left-hand navigation menu, select Single sign-on. 5. In the SAML Signing Certificate section, click 'Create new certificate' to generate a fresh certificate and metadata. 6. After creation, download the new metadata XML or certificate. 7. Update the application's SAML configuration with the new metadata or certificate. 8. If the application still fails, consider re-uploading the original certificate or metadata if a backup exists.

## References
- <https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/troubleshoot-saml-based-sso>
