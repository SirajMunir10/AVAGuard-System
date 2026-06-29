# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to customize policy tip notification text using parameters like %%FileName%%, %%ProcessName%%, %%PolicyName%%, and %%AppliedActions%%?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with custom policy tips

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the following parameters in the title and body of the notification: %%FileName%%, %%ProcessName%%, %%PolicyName%%, %%AppliedActions%%.
2. Example: '%%AppliedActions%% File Name: %%FileName%% via %%ProcessName%% isn't allowed by your organization. Select 'Allow' if you want to bypass the policy %%PolicyName%%' produces text like: 'pasting from the clipboard File Name: Contoso doc 1 via WINWORD.EXE isn't allowed by your organization. Select the 'Allow' button if you want to bypass the policy Contoso highly confidential'.
3. %%AppliedActions%% substitutes values: copy to removable storage, writing to removable storage, copy to network share, writing to a network share, paste from clipboard, pasting from the clipboard, copy via bluetooth, transferring via Bluetooth, open with an unallowed app, opening with this app, copy to a remote desktop (RDP), transferring to remote desktop, uploading to an unallowed website, uploading to this site, accessing the item via an unallowed browser, opening with this browser.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Select the DLP policy where custom policy tips were configured. 3. Under 'Policy settings', review the 'User notifications' section to confirm the custom notification title and body include the parameters %%FileName%%, %%ProcessName%%, %%PolicyName%%, and %%AppliedActions%%. 4. Trigger the DLP policy by performing an action that matches the policy rule (e.g., copying a sensitive file to a removable device). 5. Verify that the policy tip notification displays the correct dynamic values for each parameter (e.g., file name, process name, policy name, and applied action). 6. Confirm that the notification text matches the expected format and that %%AppliedActions%% resolves to one of the documented values (e.g., 'copy to removable storage').

## Rollback
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Select the DLP policy where custom policy tips were modified. 3. Under 'Policy settings', edit the 'User notifications' section. 4. Remove or revert the custom notification title and body to the default text or to the previous custom text that did not include the problematic parameters. 5. Save the policy changes. 6. Test the policy again to ensure the notification now displays the intended text without the parameters that caused issues.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
