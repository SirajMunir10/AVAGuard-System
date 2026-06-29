# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to configure user notifications and policy tips for DLP policies across different monitoring locations?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with monitoring locations: Teams Chat and Channel, Devices, Exchange, SharePoint, OneDrive

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. For Teams Chat and Channel: Enable/disable user notifications for various Microsoft apps, see Data Loss Prevention policy tips reference. Enable/disable notifications with a policy tip. Enable email notifications to the user who sent, shared, or last modified the content OR notify specific people. Customize the email text, subject, and the policy tip text.
2. For Devices only: All options available for Exchange, SharePoint, OneDrive, Teams Chat and Channel, and Instances, plus customize the notification title, content, and add a hyperlink in the form of a Get Support button that appears on the Windows 10/11 device.
3. Custom policy tip notifications are subject to character limits: JUSTIFICATION has no character limit but is limited to the remaining space available in the entire DLP package. The hyperlink must be a resolvable URL, and it's abstracted behind a selectable control.
4. Customize the title and body of text using parameters: %%FileName%%, %%ProcessName%%, %%PolicyName%%, %%AppliedActions%%.
5. Localize custom policy tips using the Set-DlpComplianceRule -NotifyPolicyTipCustomTextTranslations cmdlet.

## Validation
1. Verify DLP policy user notifications are enabled for Teams Chat and Channel: Run `Get-DlpCompliancePolicy | Format-List Name,Mode,NotifyUser` and confirm NotifyUser is set to 'On' for the relevant policy. 2. Confirm policy tip is configured for Exchange, SharePoint, OneDrive: Run `Get-DlpComplianceRule -Policy <PolicyName> | Select-Object Name,NotifyPolicyTipCustomText` and ensure NotifyPolicyTipCustomText is not empty. 3. For Devices, check notification title and body customization: Run `Get-DlpComplianceRule -Policy <PolicyName> | Format-List Name,NotifyPolicyTipCustomText,NotifyPolicyTipCustomTextTranslations` and verify custom text includes allowed parameters (%%FileName%%, %%ProcessName%%, %%PolicyName%%, %%AppliedActions%%). 4. Validate email notifications are sent to the user or specific people: Run `Get-DlpComplianceRule -Policy <PolicyName> | Select-Object Name,NotifyUser,NotifyUserEmailAddress` and confirm NotifyUser is 'On' and NotifyUserEmailAddress contains the correct recipients. 5. Test the policy by sending a sensitive email or file in the monitored locations and confirm the policy tip appears and email notification is delivered.

## Rollback
1. Disable user notifications for Teams Chat and Channel: Run `Set-DlpCompliancePolicy -Identity <PolicyName> -NotifyUser $false`. 2. Remove custom policy tip text for Exchange, SharePoint, OneDrive: Run `Set-DlpComplianceRule -Identity <RuleName> -NotifyPolicyTipCustomText $null`. 3. For Devices, reset notification title and body to default: Run `Set-DlpComplianceRule -Identity <RuleName> -NotifyPolicyTipCustomText $null -NotifyPolicyTipCustomTextTranslations $null`. 4. Disable email notifications: Run `Set-DlpComplianceRule -Identity <RuleName> -NotifyUser $false`. 5. If localized custom tips were added, remove them: Run `Set-DlpComplianceRule -Identity <RuleName> -NotifyPolicyTipCustomTextTranslations $null`. 6. Verify rollback by running the validation commands and confirming notifications and policy tips are no longer active.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
- <https://learn.microsoft.com/en-us/purview/dlp-policy-tips-reference>
- <https://learn.microsoft.com/en-us/purview/custom-email-notifications>
