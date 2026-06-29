# Implementation: Threat Analytics

**Domain:** Defender for Endpoint
**Subdomain:** Threat Analytics
**Incident Type:** Implementation

## Scenario / Query
How do I set up the Threat Intelligence Briefing Agent in Microsoft Defender XDR?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** Threat Intelligence Briefing Agent

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Set up the Threat Intelligence Briefing Agent to get timely, relevant threat intelligence reports with detailed technical analysis based on the latest threat actor activity and both internal and external vulnerability exposure.
2. The agent correlates Microsoft threat data and customer signals to add critical context to threat information in a matter of minutes, saving analyst teams hours or even days spent on intelligence gathering and correlation.
3. Once deployed, the Threat Intelligence Briefing Agent appears as a banner at the top of the Threat analytics page.

## Validation
1. Navigate to the Microsoft Defender XDR portal (https://security.microsoft.com).
2. Go to Threat analytics under the Endpoints section.
3. Confirm that a banner appears at the top of the Threat analytics page indicating the Threat Intelligence Briefing Agent is active.
4. Verify that the banner displays timely threat intelligence reports with technical analysis based on threat actor activity and vulnerability exposure.
5. Check that the reports include correlation of Microsoft threat data and customer signals, providing critical context to threat information.

## Rollback
1. In the Microsoft Defender XDR portal, go to Settings > Endpoints > General > Advanced features.
2. Locate the Threat Intelligence Briefing Agent toggle and set it to Off.
3. Confirm the change by selecting Save.
4. Navigate back to Threat analytics to ensure the banner is no longer displayed at the top of the page.
5. If the agent was deployed via a group policy or script, reverse those deployment steps (e.g., remove the policy or uninstall the agent).

## References
- <https://learn.microsoft.com/en-us/defender-xdr/threat-analytics>
