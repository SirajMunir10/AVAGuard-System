# Implementation: Security Copilot

**Domain:** Defender for Endpoint
**Subdomain:** Security Copilot
**Incident Type:** Implementation

## Scenario / Query
How do I ensure access to Copilot in Defender and make its key features available in the Microsoft Defender portal?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Security Copilot licensing

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Review the Security Copilot purchase and licensing information to ensure you have access.
2. After access is granted, key features become available in the Microsoft Defender portal.

## Validation
1. Confirm Security Copilot license assignment: In the Microsoft 365 admin center, navigate to Billing > Licenses, select 'Security Copilot', and verify that the appropriate users are assigned licenses.
2. Verify access in Microsoft Defender portal: Sign in to https://security.microsoft.com, check for the 'Copilot' icon or 'Security Copilot' pane in the navigation menu or incident/alert details page.
3. Test key features: Open an incident or alert and look for the 'Summarize' or 'Analyze with Copilot' button; click it to confirm a response is generated.
4. Validate via PowerShell (if applicable): Use `Get-MgUserLicenseDetail -UserId <user> | Where-Object {$_.SkuPartNumber -eq 'SPE_E5'}` (or the relevant SKU for Security Copilot) to confirm license assignment.

## Rollback
1. Remove Security Copilot license assignments: In the Microsoft 365 admin center, go to Billing > Licenses, select 'Security Copilot', and unassign licenses from users who should not have access.
2. Disable Security Copilot in Defender (if needed): In the Microsoft Defender portal, navigate to Settings > Endpoints > General > Security Copilot, and toggle off 'Enable Security Copilot'.
3. Clear any cached or test data: If Copilot was used for testing, no specific rollback of AI-generated content is required; simply stop using the feature.
4. Revert any configuration changes: If any custom settings were modified to enable Copilot, restore them to previous values (e.g., reset any RBAC roles or permissions that were changed).

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/security-copilot-in-microsoft-365-defender>
