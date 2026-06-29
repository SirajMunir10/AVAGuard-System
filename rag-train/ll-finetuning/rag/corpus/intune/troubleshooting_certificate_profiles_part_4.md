# Troubleshooting: Certificate Profiles

**Domain:** Intune
**Subdomain:** Certificate Profiles
**Incident Type:** Troubleshooting

## Scenario / Query
How to collect console logs from iOS/iPadOS devices for troubleshooting SCEP certificate profiles?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** SCEP certificate profiles for iOS/iPadOS

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Connect the iOS/iPadOS device to Mac, and then go to Applications > Utilities to open the Console app.
2. Under Action, select Include Info Messages and Include Debug Messages.
3. Reproduce the problem, and then save the logs to a text file: Select Edit > Select All to select all the messages on the current screen, and then select Edit > Copy to copy the messages to the clipboard.
4. Open the TextEdit application, paste the copied logs into a new text file, and then save the file.

## Validation
1. Confirm the iOS/iPadOS device is connected to a Mac via USB. 2. Open Console app (Applications > Utilities). 3. Under Action menu, verify 'Include Info Messages' and 'Include Debug Messages' are checked. 4. Reproduce the SCEP certificate issue. 5. Select all messages (Edit > Select All), copy (Edit > Copy). 6. Open TextEdit, paste logs, save as .txt. 7. Verify the saved file contains detailed SCEP-related entries (e.g., 'SCEP', 'certificate', 'error').

## Rollback
1. Disconnect the iOS/iPadOS device from the Mac. 2. Close the Console app. 3. Delete any saved log text files from the Mac. 4. Revert to previous troubleshooting method (e.g., use Apple Configurator or MDM logs).

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-scep-certificate-profiles>
