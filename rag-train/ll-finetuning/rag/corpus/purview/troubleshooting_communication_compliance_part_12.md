# Troubleshooting: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Troubleshooting

## Scenario / Query
How do I use the Conversation view to review Teams chat messages in Communication Compliance?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Communication Compliance policy configured for Teams chat messages

## Symptoms
- Image or text file attachments to messages aren't displayed in the Conversation view
- Notifications are automatically displayed for messages that have been edited or deleted from the Conversation window
- When a message is resolved, the associated conversational messages aren't retained with the resolved message

## Error Codes
N/A

## Root Causes
1. Conversation view only displays up to five messages before and after a message by default
2. Attachments are not supported in the Conversation view

## Remediation Steps
1. Select Load more to load up to 20 messages before and after a message
2. To download messages, select Download conversation to download an image file of everything seen in the user interface and a .csv file of all the message metadata (UserId, UserName, and so on)

## Validation
1. Open the Communication Compliance solution in the Microsoft Purview compliance portal. 2. Navigate to the policy configured for Teams chat messages. 3. Select a message that previously had missing attachments. 4. In the Conversation view, verify that image or text file attachments are not displayed (they are not supported). 5. Select 'Load more' and confirm that up to 20 messages before and after the selected message are now visible. 6. Select 'Download conversation' and verify that an image file of the UI and a .csv file with message metadata (UserId, UserName, etc.) are downloaded. 7. Confirm that notifications for edited or deleted messages still appear automatically. 8. Resolve a message and check that the associated conversational messages are not retained with the resolved message.

## Rollback
1. If 'Load more' causes performance issues, refresh the Conversation view to return to the default of five messages before and after. 2. If the downloaded conversation files are unwanted, delete them from the local machine. 3. No configuration changes were made, so no direct rollback of settings is required. 4. If the issue persists, verify that the Communication Compliance policy is still correctly configured for Teams chat messages by reviewing the policy settings in the Purview portal.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
