# Implementation: Security Copilot

**Domain:** Defender for Endpoint
**Subdomain:** Security Copilot
**Incident Type:** Implementation

## Scenario / Query
How do I use Security Copilot in Microsoft 365 Defender to investigate an incident with a proposed step-by-step plan?

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
1. Ask the chat to investigate an incident, for example: 'Investigate incident 12345 and summarize the key findings'.
2. Review the proposed plan that outlines the steps it intends to take, such as: Retrieve incident details, Fetch associated alerts, Collect evidence and impacted entities, Summarize findings.
3. Approve or reject the plan before any actions are taken.
4. After approval, the chat executes each step and shows its progress in real time.

## Validation
1. Open the Microsoft 365 Defender portal (https://security.microsoft.com) and navigate to Incidents & alerts > Incidents. 2. Select an incident (e.g., incident 12345) and click 'Investigate in Security Copilot' or open the Security Copilot chat pane. 3. Send the prompt: 'Investigate incident 12345 and summarize the key findings.' 4. Verify that Security Copilot responds with a proposed plan that includes steps such as: Retrieve incident details, Fetch associated alerts, Collect evidence and impacted entities, Summarize findings. 5. Confirm that you can approve or reject the plan before any actions are taken. 6. After approval, observe that the chat executes each step and shows its progress in real time. 7. Validate that the final summary includes key findings from the incident.

## Rollback
1. If the investigation plan is not as expected, reject the proposed plan before any actions are executed. 2. If the plan was already approved and executed, review the incident details manually by navigating to Incidents & alerts > Incidents and selecting the incident. 3. Manually inspect associated alerts, evidence, and impacted entities from the incident page. 4. If Security Copilot is not functioning correctly, disable the Security Copilot integration by going to Settings > Microsoft 365 Defender > Security Copilot and toggling off the integration. 5. Re-enable the integration after troubleshooting or contacting support.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/security-copilot-in-microsoft-365-defender>
