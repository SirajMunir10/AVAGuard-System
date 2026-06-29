# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How do I configure DLP actions for Exchange Online, SharePoint Online, and OneDrive for Business?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with EXO/SPO/ODB actions

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the Restrict access or encrypt content in Microsoft 365 EXO/SPO/ODB action.
2. Use the Block access for specific external domains or users sub-option (note: image files aren't protected; multiple audit records can be generated for certain actions on a blocked file by a blocked user, public preview, SPO/ODB only).
3. Set headers.
4. Remove header.
5. Redirect the message to specific users.

## Validation
1. Verify DLP policy actions are applied: Run `Get-DlpCompliancePolicy | Format-List Name,ExchangeLocation,SharePointLocation,OneDriveLocation` in Exchange Online PowerShell to confirm the policy targets EXO/SPO/ODB. 2. For 'Restrict access or encrypt content' action: Use `Get-DlpComplianceRule -Policy <PolicyName> | Select-Object Name,AccessScope,BlockAccess,BlockAccessScope` to confirm the rule enforces block access. 3. For 'Block access for specific external domains or users': Check `Get-DlpComplianceRule | Where-Object {$_.BlockAccess -eq $true} | Select-Object Name,BlockAccess,BlockAccessScope` to verify the sub-option is configured. 4. For header actions: Run `Get-DlpComplianceRule | Select-Object Name,HeaderName,HeaderValue` to confirm custom headers are set or removed. 5. For 'Redirect the message': Use `Get-DlpComplianceRule | Select-Object Name,RedirectToRecipients` to verify redirection recipients. 6. Test the policy by sending a sensitive email to an external domain and confirm the message is blocked, redirected, or headers modified as expected. 7. For SPO/ODB, upload a sensitive file and verify access is blocked for external users (note: image files are not protected).

## Rollback
1. Disable the DLP policy: Run `Set-DlpCompliancePolicy -Identity <PolicyName> -State Disabled` in Exchange Online PowerShell. 2. Remove the 'Restrict access or encrypt content' action: Use `Set-DlpComplianceRule -Identity <RuleName> -RemoveBlockAccess` to clear block access settings. 3. Remove 'Block access for specific external domains or users': Run `Set-DlpComplianceRule -Identity <RuleName> -BlockAccess $false -BlockAccessScope $null`. 4. Clear custom headers: Use `Set-DlpComplianceRule -Identity <RuleName> -RemoveHeader` to remove header modifications. 5. Remove redirection: Run `Set-DlpComplianceRule -Identity <RuleName> -RedirectToRecipients $null`. 6. Re-enable the original policy if needed: `Set-DlpCompliancePolicy -Identity <PolicyName> -State Enabled`. 7. Monitor audit logs for any residual blocking or redirection issues.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
