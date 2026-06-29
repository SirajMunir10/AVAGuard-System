# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How to enable Endpoint DLP for Windows Servers after onboarding?

## Environment Context
- **Tenant Type:** Microsoft Purview
- **Configuration:** Endpoint DLP support for onboarded servers

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. In the Microsoft Purview portal, go to Data loss prevention > Overview.
2. Choose Settings in the upper right corner.
3. On Settings, select Endpoint settings and expand Endpoint DLP support for onboarded servers.
4. Set the toggle to On.

## Validation
1. In the Microsoft Purview portal, navigate to Data loss prevention > Overview. 2. Select Settings (upper right), then Endpoint settings. 3. Expand 'Endpoint DLP support for onboarded servers' and confirm the toggle is set to On. 4. Verify that a test file with sensitive content (e.g., credit card number) copied to an onboarded Windows Server triggers a DLP policy audit event in Activity Explorer within 30 minutes.

## Rollback
1. In the Microsoft Purview portal, go to Data loss prevention > Overview. 2. Select Settings (upper right), then Endpoint settings. 3. Expand 'Endpoint DLP support for onboarded servers' and set the toggle to Off. 4. Confirm the change by checking that no new DLP policy matches appear for server endpoints in Activity Explorer.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
