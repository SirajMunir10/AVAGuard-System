# Troubleshooting: Security Copilot

**Domain:** Defender for Endpoint
**Subdomain:** Security Copilot
**Incident Type:** Troubleshooting

## Scenario / Query
How does Security Copilot handle ambiguous requests in Microsoft 365 Defender?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Security Copilot chat interface

## Symptoms
- Chat asks a clarifying question when request is ambiguous
- Quick-select options (up to four suggestions) are offered

## Error Codes
N/A

## Root Causes
1. Ambiguous user request

## Remediation Steps
1. Select an option from the quick-select suggestions
2. Type your own response

## Validation
1. Open the Security Copilot chat interface in Microsoft 365 Defender. 2. Submit an ambiguous request (e.g., 'show alerts'). 3. Verify that the chat responds with a clarifying question and displays up to four quick-select options. 4. Select one of the options and confirm the chat proceeds with the chosen context. 5. Submit another ambiguous request and type your own response instead of selecting a quick-select option. 6. Confirm the chat processes your typed response correctly.

## Rollback
1. If the chat does not display clarifying questions or quick-select options, ensure the Security Copilot feature is enabled in the Microsoft 365 Defender settings. 2. If the issue persists, clear the browser cache and cookies, then reload the Microsoft 365 Defender portal. 3. If the chat still fails to handle ambiguous requests, contact Microsoft Support for further assistance.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/security-copilot-in-microsoft-365-defender>
