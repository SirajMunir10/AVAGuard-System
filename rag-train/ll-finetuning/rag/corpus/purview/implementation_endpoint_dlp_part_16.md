# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How do DLP restrictions apply to file activities when using restricted app groups and the restricted app activities list in the same rule?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP policy with restricted app groups and restricted app activities list

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Configure File activities for apps in restricted app groups to override configurations in the Restricted app activities list and File activities for all apps in the same rule.
2. Set Restricted app activities to either Audit only or Block with override to allow File activities for all apps to apply in concert.
3. Add Notepad.exe to Restricted apps and configure File activities for all apps to Apply restrictions to specific activity.
4. Configure Restricted app activities for Access a DLP protected item.
5. Configure File activities for all apps for Copy to clipboard, Copy to a USB removable device, Copy to a network share, Copy or move using unallowed Bluetooth app, and Remote desktop services.
6. Set the action for Restricted app activities to Block with override to block all access and prevent any activities on the file.

## Validation
1. Open the Microsoft Purview compliance portal and navigate to Data Loss Prevention > Policies. Select the policy that includes both restricted app groups and restricted app activities. 2. In the policy rule, confirm that 'File activities for apps in restricted app groups' is set to 'Override' and 'File activities for all apps' is configured with specific restrictions (e.g., Copy to clipboard, Copy to USB). 3. Verify that 'Restricted app activities' is set to 'Block with override' for 'Access a DLP protected item'. 4. On a test endpoint, add Notepad.exe to the restricted apps list. 5. Attempt to open a DLP-protected file with Notepad.exe; the action should be blocked with an override option. 6. Attempt to copy the file’s content to clipboard using Notepad.exe; this should be blocked per the 'File activities for all apps' setting. 7. Check the DLP activity explorer for matching events showing the block actions.

## Rollback
1. In the same policy rule, set 'File activities for apps in restricted app groups' back to 'Inherit' or remove the override. 2. Change 'Restricted app activities' from 'Block with override' to 'Audit only' or remove the action. 3. Remove Notepad.exe from the restricted apps list. 4. Reset 'File activities for all apps' to 'Audit only' or remove the specific restrictions. 5. Save the policy and allow up to 1 hour for changes to propagate. 6. On a test endpoint, verify that previous blocks are no longer enforced and file activities are audited only.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
