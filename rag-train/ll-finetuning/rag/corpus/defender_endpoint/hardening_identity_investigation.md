# Hardening: Identity Investigation

**Domain:** Defender for Endpoint
**Subdomain:** Identity Investigation
**Incident Type:** Hardening

## Scenario / Query
How to review identity context and account tags on the Identity page in Microsoft Defender?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Identity page top section shows org information and tags

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Review the top section of the Identity page for identity context such as org information and tags
2. Use the Actions menu for remediation actions
3. Use tabs to review summary details, related alerts, and deeper investigation views

## Validation
1. Navigate to the Microsoft 365 Defender portal (https://security.microsoft.com).
2. Go to 'Identities' under the 'Investigation & response' section.
3. Select a specific user identity to open the Identity page.
4. Verify that the top section displays the organization information (e.g., domain, company name) and any assigned account tags (e.g., 'Admin', 'VIP').
5. Confirm that the 'Actions' menu is present and contains remediation options such as 'Disable user', 'Reset password', or 'Require MFA'.
6. Check that the tabs (e.g., 'Summary', 'Alerts', 'Timeline') are functional and show relevant data, including related alerts and investigation details.

## Rollback
1. If the Identity page does not load or shows incorrect data, clear the browser cache and cookies, then reload the portal.
2. If account tags are missing or incorrect, verify that the user's Azure AD attributes are correctly synchronized and that the appropriate tag policies are applied in Microsoft Defender for Identity.
3. If the 'Actions' menu is missing or options are grayed out, ensure the user has the required permissions (e.g., 'Security Administrator' or 'Security Operator') assigned in Azure AD.
4. If tabs fail to display content, check that the Microsoft 365 Defender service is healthy by visiting the Service Health dashboard in the Microsoft 365 admin center.
5. If issues persist, refer to the official documentation at https://learn.microsoft.com/en-us/defender-xdr/investigate-users for troubleshooting steps.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-users>
