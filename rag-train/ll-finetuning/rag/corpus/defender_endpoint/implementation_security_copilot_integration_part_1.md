# Implementation: Security Copilot Integration

**Domain:** Defender for Endpoint
**Subdomain:** Security Copilot Integration
**Incident Type:** Implementation

## Scenario / Query
What are the two ways to access Copilot in Microsoft Defender?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 or Defender for Endpoint Plan 2
- **Configuration:** Security Copilot provisioned and embedded in Defender portal.

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Access Copilot embedded in the Microsoft Defender portal.
2. Access the Defender Chat experience (preview) built into Microsoft Defender.

## Validation
1. Open a browser and navigate to https://security.microsoft.com. Sign in with credentials that have Security Copilot permissions. 2. In the Microsoft Defender portal, verify that the Copilot icon (lightning bolt) is visible in the top navigation bar. Click the icon to confirm the Copilot panel opens and responds to queries. 3. In the same portal, locate the 'Defender Chat' experience (preview) by clicking the chat icon or accessing it from the navigation menu. Send a test prompt (e.g., 'Summarize recent alerts') and confirm a valid response is returned.

## Rollback
1. If Copilot is not accessible in the Defender portal, verify that the user has the required license (Microsoft 365 E5 or Defender for Endpoint Plan 2) and that Security Copilot is provisioned in the tenant. 2. If the Copilot icon is missing, check that the 'Security Copilot' service plan is enabled in the Microsoft 365 admin center under Billing > Licenses. 3. If the Defender Chat experience fails, ensure that the preview feature is enabled in the Defender portal settings under 'Microsoft Defender XDR > Preview features'. 4. If issues persist, contact Microsoft support to confirm the tenant's Security Copilot provisioning status.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/security-copilot-in-microsoft-365-defender>
