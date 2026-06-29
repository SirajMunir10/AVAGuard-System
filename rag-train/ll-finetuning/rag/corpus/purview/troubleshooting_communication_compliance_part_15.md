# Troubleshooting: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate and remediate hidden content matches in Communication Compliance policies when a message doesn't appear to match policy conditions?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Communication Compliance policy with keyword conditions

## Symptoms
- A message is flagged by a Communication Compliance policy but the plain text view does not show the matching keywords
- The message appears not to match the conditions set for the policy

## Error Codes
N/A

## Root Causes
1. Keywords are hidden and embedded in nonvisible metadata such as HTML tags, alternative text for images, encoded strings, filenames of attachments, or OCR text

## Remediation Steps
1. Select and download the message with the policy match
2. Extract the contents of the zipped folder
3. Locate the .eml file
4. Open the .eml file with any text editor
5. Use the Find function to search for the individual keywords in the policy conditions to identify where the match occurs

## Validation
1. Download the flagged message from the Communication Compliance policy. 2. Extract the contents of the downloaded zip folder. 3. Locate the .eml file within the extracted folder. 4. Open the .eml file with a text editor (e.g., Notepad). 5. Use the Find function (Ctrl+F) to search for each keyword defined in the policy conditions. 6. Confirm that at least one keyword is found in the .eml file content, including hidden or nonvisible metadata such as HTML tags, alt text, encoded strings, attachment filenames, or OCR text. 7. Verify that the keyword match location explains why the message was flagged despite not appearing in the plain text view.

## Rollback
1. If the remediation (downloading and inspecting the .eml file) reveals no hidden keyword match, re-upload the original message to the Communication Compliance policy review queue. 2. Escalate the case to Microsoft Support if the policy conditions appear correct but the message still shows no match after inspection. 3. No configuration changes were made during remediation, so no rollback of settings is required. 4. If the policy conditions were inadvertently modified during investigation, restore the original keyword list from backup or policy history.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
