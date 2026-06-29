# Implementation: Incident Management

**Domain:** Defender for Endpoint
**Subdomain:** Incident Management
**Incident Type:** Implementation

## Scenario / Query
How do I use the Copilot tab in Microsoft 365 Defender to manage incidents in a unified experience?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Copilot tab enabled on incident page

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select the Copilot tab on the incident page to view the incident summary, get recommendations, or generate a report.
2. Select Summarize to generate the incident summary or view it if it already exists.
3. You can run multiple summary requests in parallel for different entities (such as users and devices), and the results are cached unless regenerated.
4. When you close a summary panel, the summary process stops.
5. Incident chats persist across incidents. When you switch to a different incident, the chat automatically closes, but when you reopen the Copilot panel you see the chat history.
6. Select Recommendations to get AI-powered recommendations for next steps on how to investigate and remediate the incident.
7. Select Report to generate a comprehensive report of the incident that includes the summary, timelines, involved entities, and more.

## Validation
1. Open the Microsoft 365 Defender portal (https://security.microsoft.com).
2. Navigate to Incidents & alerts > Incidents.
3. Select an incident to open its details page.
4. Verify that the Copilot tab is visible on the incident page.
5. Click the Copilot tab and confirm that the incident summary is displayed (or that the 'Summarize' button appears if no summary exists yet).
6. Click 'Summarize' and verify that a summary is generated and displayed.
7. Click 'Recommendations' and confirm that AI-powered recommendations appear.
8. Click 'Report' and verify that a comprehensive report is generated, including summary, timeline, and involved entities.
9. Close the summary panel and confirm that the summary process stops.
10. Switch to a different incident and then return to the original incident; verify that the Copilot panel shows the previous chat history.

## Rollback
1. If the Copilot tab is missing or not functioning, ensure that the user has the required permissions (e.g., Security Reader, Security Operator, or Security Administrator role).
2. If the summary fails to generate, refresh the incident page and try again.
3. If recommendations are not displayed, verify that Microsoft 365 Defender has sufficient data and that the incident is not too old.
4. If the report generation fails, check that the incident contains the necessary entities (users, devices) and that the Copilot service is available.
5. If the chat history is lost, note that chat persistence is automatic; if it does not appear, close and reopen the Copilot panel.
6. If issues persist, review the service health dashboard for any known incidents with Microsoft 365 Defender or Security Copilot.
7. As a last resort, disable and re-enable the Copilot integration via the Microsoft 365 Defender settings (if applicable) or contact Microsoft support.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/security-copilot-in-microsoft-365-defender>
