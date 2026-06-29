# Implementation: Security Copilot

**Domain:** Defender for Endpoint
**Subdomain:** Security Copilot
**Incident Type:** Implementation

## Scenario / Query
How to use Security Copilot to consolidate and summarize threat intelligence for prioritizing and responding to threats in Microsoft 365 Defender?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Security Copilot enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ask Copilot to summarize the relevant threats impacting your environment.
2. Ask Copilot to prioritize resolving threats based on your exposure levels.
3. Ask Copilot to find threat actors that might be targeting your industry.

## Validation
1. Open the Microsoft 365 Defender portal (https://security.microsoft.com).
2. In the navigation pane, select 'Security Copilot' or locate the Copilot icon in the top-right corner.
3. In the Copilot prompt bar, enter: 'Summarize the relevant threats impacting my environment.'
4. Verify that Copilot returns a consolidated summary of active threats, including affected devices, users, and incident IDs.
5. Next, enter: 'Prioritize resolving threats based on my exposure levels.'
6. Confirm that Copilot provides a prioritized list of threats, ordered by severity or exposure score.
7. Finally, enter: 'Find threat actors that might be targeting my industry.'
8. Ensure Copilot returns relevant threat actor profiles, tactics, techniques, and procedures (TTPs) associated with your industry.
9. Check that all responses include citations to Microsoft Defender data and threat intelligence sources.

## Rollback
1. If Copilot fails to generate a summary or returns inaccurate results, clear the conversation history by selecting 'New session' or 'Clear chat' in the Copilot interface.
2. Verify that Security Copilot is enabled in the Microsoft 365 Defender settings: navigate to Settings > Microsoft 365 Defender > Security Copilot, and confirm the toggle is set to 'On'.
3. If Copilot is disabled, re-enable it by toggling the setting to 'On' and saving changes.
4. If Copilot still does not respond correctly, check that the user has the required permissions (e.g., Security Reader, Security Operator, or Security Administrator role) by reviewing role assignments in the Microsoft 365 Defender portal under Permissions > Roles.
5. If permissions are missing, assign the appropriate role via Microsoft Entra ID (Azure AD) or the Microsoft 365 Defender portal.
6. As a last resort, contact Microsoft Support to verify tenant-level enablement of Security Copilot and review service health in the Microsoft 365 admin center under Health > Service health.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/security-copilot-in-microsoft-365-defender>
