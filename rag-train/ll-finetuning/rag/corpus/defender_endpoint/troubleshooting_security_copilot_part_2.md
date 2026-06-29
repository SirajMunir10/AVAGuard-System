# Troubleshooting: Security Copilot

**Domain:** Defender for Endpoint
**Subdomain:** Security Copilot
**Incident Type:** Troubleshooting

## Scenario / Query
How do I manage conversation history in Security Copilot in Microsoft 365 Defender?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Conversations are not synced across devices
- Conversations are not shared with other users
- Only the last ten conversations are stored locally in the browser

## Error Codes
N/A

## Root Causes
1. Conversations are stored locally in the browser and not synced across devices or shared with other users

## Remediation Steps
1. Use the Conversations panel on the left side of the chat to resume a previous conversation
2. Use the Conversations panel on the left side of the chat to start a new session
3. Use the Conversations panel on the left side of the chat to delete a conversation
4. Use the Conversations panel on the left side of the chat to clear all conversations

## Validation
Open the Security Copilot chat in Microsoft 365 Defender. Confirm that the Conversations panel on the left side displays the expected list of previous conversations. Verify that you can click on a conversation to resume it, and that the chat history loads correctly. Check that you can start a new session by clicking 'New session' in the Conversations panel. Ensure that the 'Delete' and 'Clear all conversations' options are available and functional. If possible, test on a different device or browser to confirm that conversations are not synced (as expected per the root cause).

## Rollback
If the Conversations panel is missing or not functioning, refresh the browser page. If the issue persists, clear the browser cache and cookies for the Microsoft 365 Defender site, then reload the page. If conversations are accidentally deleted, note that deleted conversations cannot be recovered because they are stored locally in the browser. To restore a previous state, you may need to restore from a browser backup if available, or accept that the data is lost. If the panel itself is broken, try accessing Security Copilot from a different browser or device to isolate the issue.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/security-copilot-in-microsoft-365-defender>
