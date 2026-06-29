# Troubleshooting: Enterprise Applications

**Domain:** Entra ID
**Subdomain:** Enterprise Applications
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot SAML-based single sign-on configuration issues in Microsoft Entra ID?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** SAML-based SSO configuration for enterprise applications

## Symptoms
- Access to configuration page requires authorization
- Unable to configure application

## Error Codes
N/A

## Root Causes
1. Steps in the tutorial for the application were not followed completely

## Remediation Steps
1. Verify you followed all the steps in the tutorial for the application
2. Check the inline documentation on how to configure the application in the application's configuration
3. Access the List of tutorials on how to integrate SaaS apps with Microsoft Entra ID for detailed step-by-step guidance

## Validation
1. Confirm that the user has the required permissions (e.g., Cloud Application Administrator or Application Administrator) to access the enterprise application configuration page. Use: `Get-MgDirectoryRole -Filter "displayName eq 'Cloud Application Administrator'"` and verify membership. 2. Navigate to the specific enterprise application in the Microsoft Entra admin center (Identity > Applications > Enterprise applications > [App Name]) and verify that the SAML-based Sign-On settings are visible and editable. 3. Cross-check the application’s configuration against the official tutorial for that application (e.g., from the list at https://learn.microsoft.com/en-us/entra/identity/saas-apps/tutorial-list). Ensure all required fields (Identifier, Reply URL, Sign-on URL, etc.) are correctly populated. 4. Use the Test this application feature in the SAML-based Sign-On blade to confirm the SSO flow works without errors.

## Rollback
1. If the configuration page remains inaccessible, verify the user’s role assignment and re-add the necessary role (e.g., `Add-MgDirectoryRoleMember -DirectoryRoleId <roleId> -DirectoryObjectId <userId>`). 2. If the application configuration is incorrect, revert to the previous known-good settings by restoring from a backup or manually resetting the SAML URLs to the values documented in the application’s tutorial. 3. If the issue persists, remove and re-add the enterprise application from the gallery following the tutorial steps exactly: delete the application (Identity > Applications > Enterprise applications > [App Name] > Delete) and re-add it via the gallery (Identity > Applications > Enterprise applications > New application > [App Name]). 4. As a last resort, contact Microsoft Support for assistance with authorization or configuration issues.

## References
- <https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/troubleshoot-saml-based-sso>
