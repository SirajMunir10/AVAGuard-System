# Troubleshooting: Microsoft 365 Defender

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft 365 Defender
**Incident Type:** Troubleshooting

## Scenario / Query
How can I use Copilot to summarize an incident in Microsoft 365 Defender to quickly understand an attack?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Copilot enabled in Microsoft 365 Defender

## Symptoms
- Multiple alerts in an incident make it daunting to understand the attack

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to an incident's page in Microsoft 365 Defender
2. Copilot automatically creates a summary of the incident
3. The overview contains essential information about what transpired in the attack, what assets are involved, and the timeline of the attack
4. Use suggested prompts about related identities, devices, IPs, and so on to understand assets involved and how to act

## Validation
1. Open a browser and navigate to https://security.microsoft.com/incidents. 2. Select any incident from the list. 3. Verify that the incident page loads and that a Copilot-generated summary is displayed at the top of the page. 4. Confirm the summary includes essential information such as attack description, affected assets, and timeline. 5. Click on suggested prompts (e.g., 'Related identities', 'Related devices', 'Related IPs') and verify that each prompt returns relevant, contextual data. 6. Ensure no error messages or missing summary sections appear.

## Rollback
1. If the Copilot summary does not appear, verify that Copilot is enabled in Microsoft 365 Defender by navigating to Settings > Microsoft 365 Defender > Copilot and ensuring the toggle is turned on. 2. If Copilot is already enabled, check that the user has the required permissions (e.g., Security Reader, Security Administrator) by reviewing role assignments in Microsoft Entra ID. 3. If the summary is incomplete or incorrect, refresh the incident page after a few minutes to allow Copilot to regenerate the summary. 4. If issues persist, clear the browser cache and cookies, then reload the incident page. 5. As a last resort, disable and re-enable Copilot in the settings, then navigate back to the incident to trigger a fresh summary generation.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/security-copilot-in-microsoft-365-defender>
