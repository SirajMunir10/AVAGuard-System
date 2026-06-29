# Implementation: Data Loss Prevention (DLP)

**Domain:** Purview
**Subdomain:** Data Loss Prevention (DLP)
**Incident Type:** Implementation

## Scenario / Query
How do I configure DLP policy actions for Microsoft 365 locations including devices, email, SharePoint, OneDrive, Teams, and Power BI?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with Devices location

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select the 'Restrict access or encrypt the content in Microsoft 365 locations' action for the Devices location.
2. Select 'Block users from receiving email, or accessing shared SharePoint, OneDrive, Teams files, and Power BI items' action.
3. Select 'Audit or restrict activities when users access sensitive sites in Microsoft Edge browsers on Windows devices' action.
4. Configure 'Sensitive site restrictions' as needed.
5. Select 'Audit or restrict activities on devices' action.
6. Configure 'Upload to a restricted cloud service domain or access from an unallowed browser' action.
7. Configure 'Paste to supported browsers' action.
8. Configure 'File activities for all apps' including: Copy to clipboard, Copy to removable USB device, Copy to a network share, Print, Copy or move using unallowed Bluetooth app, Copy or move using RDP.
9. Configure 'File activities for apps in restricted app groups'.
10. Configure 'App access restrictions' including: Access by restricted apps, Access by apps not included in restricted apps list or any restricted app groups added to rule in preview.
11. Configure 'Restrictions in Windows Recall in Copilot+ PCs'.
12. Configure 'Apply restrictions to only unsupported file extensions' (note: this option does NOT support scoping by Device and device groups in the policy location setting).
13. Select 'Start a Power Automate flow' action if needed.
14. For Windows devices, set actions to: Allow, Audit only, Block with override, or Block.
15. For macOS devices, set actions to: Audit only, Block with override, or Block.

## Validation
1. Verify the DLP policy is applied to the Devices location by running: Get-DlpCompliancePolicy -Identity "<PolicyName>" | Format-List Name, Mode, ExchangeLocation, SharePointLocation, OneDriveLocation, TeamsLocation, PowerBILocation, EndpointDlpLocation. 2. Confirm the 'Restrict access or encrypt the content in Microsoft 365 locations' action is enabled for Devices by checking the policy rule: Get-DlpComplianceRule -Policy "<PolicyName>" | Where-Object {$_.AccessScope -eq "Endpoint"} | Format-List Name, AccessScope, BlockAccess, BlockAccessScope. 3. Validate that 'Block users from receiving email, or accessing shared SharePoint, OneDrive, Teams files, and Power BI items' is set by reviewing the rule's BlockAccess property. 4. Ensure 'Audit or restrict activities when users access sensitive sites in Microsoft Edge' is configured by checking the rule's EdgeSensitiveSiteRestriction property. 5. Confirm device restrictions (USB, clipboard, network share, print, Bluetooth, RDP) are set by examining the rule's EndpointDlpAction properties. 6. Verify app restrictions (restricted apps, unallowed apps) are applied via the rule's RestrictedAppAccess property. 7. Check that Windows Recall restrictions are configured if applicable. 8. Validate that the 'Apply restrictions to only unsupported file extensions' option is not used with Device scoping. 9. Test the policy by simulating a sensitive data transfer on a Windows device and confirm the expected block or audit action occurs.

## Rollback
1. Remove the Devices location from the DLP policy by running: Set-DlpCompliancePolicy -Identity "<PolicyName>" -EndpointDlpLocation $null. 2. Alternatively, disable the specific actions by modifying the rule: Set-DlpComplianceRule -Identity "<RuleName>" -BlockAccess $false -BlockAccessScope $null. 3. To revert device restrictions, set each EndpointDlpAction to 'Audit only' or remove the action entirely. 4. To remove app restrictions, clear the RestrictedAppAccess property. 5. If a Power Automate flow was started, disable or delete the flow from Power Automate. 6. For Windows devices, change actions from 'Block' to 'Allow' or 'Audit only' as needed. 7. For macOS devices, change actions from 'Block' to 'Audit only' or 'Allow'. 8. If the policy was deployed broadly, consider setting the policy to 'Test' mode (Set-DlpCompliancePolicy -Identity "<PolicyName>" -Mode Test) to observe impact before full rollback.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
