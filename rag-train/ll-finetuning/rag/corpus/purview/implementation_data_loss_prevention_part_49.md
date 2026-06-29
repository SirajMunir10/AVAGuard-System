# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How do I apply branding to encrypted messages in a DLP policy?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with action 'Apply branding to encrypted messages'

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. For the 'Apply branding to encrypted messages' action, if you already have Microsoft Purview Message Encryption implemented, the templates automatically show up in the drop-down list.
2. If you want to implement Microsoft Purview Message Encryption, see 'Add your organization's brand to your Microsoft Purview Message Encryption encrypted messages' for background on message encryption and how to create and configure your branding templates.

## Validation
1. Verify that the DLP policy with the 'Apply branding to encrypted messages' action is configured and enabled. Run: Get-DlpCompliancePolicy -Identity "PolicyName" | Format-List Name, Mode, ExchangeSender, ExchangeRecipient, ExchangeLocation, SharePointLocation, OneDriveLocation, TeamsLocation, EndpointDlpLocation. 2. Confirm that the branding template is applied by checking the policy's rule actions: Get-DlpComplianceRule -Policy "PolicyName" | Select-Object Name, Actions. 3. Send a test email that triggers the DLP policy and verify that the encrypted message displays the custom branding (e.g., logo, disclaimer text) in the recipient's email client. 4. Check the Microsoft Purview Message Encryption configuration: Get-IRMConfiguration | Format-List LicensingLocation, AzureRMSLicensingEnabled, SimplifiedClientAccessEnabled, DecryptAttachmentForEncryptOnly.

## Rollback
1. Remove the 'Apply branding to encrypted messages' action from the DLP policy rule. Run: Set-DlpComplianceRule -Identity "RuleName" -RemoveActions @("ApplyBrandingToEncryptedMessages"). 2. If the branding template was created specifically for this policy, delete the custom branding template in Microsoft Purview Message Encryption: Remove-RMSTemplate -Identity "TemplateName". 3. Revert the DLP policy to its previous state by disabling or removing the rule: Set-DlpComplianceRule -Identity "RuleName" -Disabled $true. 4. Verify that encrypted messages no longer display the custom branding by sending a test email and checking the encryption appearance.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
