# Troubleshooting: Enterprise Applications

**Domain:** Entra ID
**Subdomain:** Enterprise Applications
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve issues when unable to add the Identifier or Reply URL during SAML-based SSO configuration?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** SAML-based single sign-on configuration for enterprise applications

## Symptoms
- Unable to configure the Identifier or Reply URL in the SAML-based SSO settings
- Red exclamation mark appears when entering a value in the Identifier or Reply URL textbox

## Error Codes
N/A

## Root Causes
1. Identifier and Reply URL values do not match the patterns preconfigured for the application in Microsoft Entra ID

## Remediation Steps
1. Sign in to the Microsoft Entra admin center as at least a Cloud Application Administrator.
2. Browse to Entra ID > Enterprise apps > All applications.
3. Select the application you want to configure single sign-on.
4. Once the application loads, select the Single sign-on from the application's left-hand navigation menu.
5. Select SAML-based Sign-on from the Mode dropdown.
6. Go to the Identifier or Reply URL textbox, under the Domain and URLs section.
7. Check the supported pattern shown as a placeholder in the textbox (e.g., https://contoso.com).
8. If the pattern isn't supported, hover over the red exclamation mark to see the supported patterns.
9. Alternatively, refer to the tutorial for the application under the Configure Microsoft Entra single sign-on section for supported patterns.
10. If the values don't match the patterns preconfigured in Microsoft Entra ID, work with the application vendor to get values that match the pattern preconfigured in Microsoft Entra ID.

## Validation
1. Sign in to the Microsoft Entra admin center as at least a Cloud Application Administrator.
2. Browse to Identity > Applications > Enterprise applications > All applications.
3. Select the application configured for SAML-based SSO.
4. In the left navigation, select Single sign-on.
5. Ensure the Mode is set to SAML-based Sign-on.
6. Under Domain and URLs, check the Identifier and Reply URL textboxes.
7. Verify that the entered values match the supported pattern shown as a placeholder (e.g., https://contoso.com) or the pattern displayed when hovering over the red exclamation mark.
8. Confirm that no red exclamation mark appears next to the Identifier or Reply URL.
9. Optionally, refer to the application’s tutorial under Configure Microsoft Entra single sign-on to confirm the correct pattern.

## Rollback
1. If the Identifier or Reply URL values were changed to match a pattern that later causes issues, revert to the original values provided by the application vendor.
2. If the application vendor provided new values that match the preconfigured pattern but the application fails to work, contact the vendor to obtain the correct values that align with the patterns supported by Microsoft Entra ID.
3. If the changes were made in error, delete the current Identifier or Reply URL and re-enter the original values that were previously working.
4. Save the configuration and test SAML-based SSO again.

## References
- <https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/troubleshoot-saml-based-sso>
