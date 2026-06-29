# Implementation: Microsoft 365 Defender

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft 365 Defender
**Incident Type:** Implementation

## Scenario / Query
How to use interactive conversations with Security Copilot in Microsoft 365 Defender to ask follow-up questions about incidents?

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
1. Start with 'Show me high-severity incidents from the past week'
2. Follow up with 'Tell me more about the first one'

## Validation
1. Open Microsoft 365 Defender portal (https://security.microsoft.com).
2. In the left navigation, select 'Security Copilot'.
3. In the conversation pane, type 'Show me high-severity incidents from the past week' and press Enter.
4. Verify that the response lists high-severity incidents from the past week.
5. Type 'Tell me more about the first one' and press Enter.
6. Confirm that the response provides detailed information about the first incident in the list.
7. Ensure that the conversation history shows both prompts and their corresponding responses.

## Rollback
1. If the interactive conversation does not respond as expected, close the Security Copilot pane and reopen it.
2. If issues persist, verify that Security Copilot is enabled in the tenant by navigating to Settings > Microsoft 365 Defender > Security Copilot and ensuring the toggle is on.
3. If Security Copilot is disabled, enable it and retry the conversation.
4. If the problem continues, check the service health dashboard for any ongoing incidents related to Security Copilot.
5. As a last resort, contact Microsoft support for further assistance.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/security-copilot-in-microsoft-365-defender>
