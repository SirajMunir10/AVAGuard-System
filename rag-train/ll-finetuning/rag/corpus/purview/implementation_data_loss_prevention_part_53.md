# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
What actions can be used to restrict access or encrypt content in Microsoft 365 locations?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy for Microsoft 365 locations

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use this to block users from receiving email, or accessing shared SharePoint, OneDrive, Teams files, and Power BI items
2. This action can block everyone or block only people who are outside your organization
3. For SharePoint and OneDrive locations only, you can also block access for specific external domains or user SMTPs (in public preview)

## Validation
1. Verify that the DLP policy is applied to the intended Microsoft 365 locations (Exchange, SharePoint, OneDrive, Teams, Power BI) by running: Get-DlpCompliancePolicy -Identity "PolicyName" | Format-List ExchangeLocation, SharePointLocation, OneDriveLocation, TeamsLocation, PowerBILocation. 2. Confirm the 'Block' action is enabled for the policy by running: Get-DlpComplianceRule -Policy "PolicyName" | Select-Object Name, AccessScope, BlockAccess, BlockAccessScope. 3. For SharePoint/OneDrive, test that external users (or specific domains/SMTPs if configured) are blocked from accessing protected content by attempting to open a restricted file from an external account. 4. For Exchange, send a test email containing sensitive data to an external recipient and verify it is blocked with a non-delivery report (NDR). 5. Review DLP incident reports in the Microsoft Purview compliance portal to ensure no false positives or unexpected blocks.

## Rollback
1. Remove or modify the blocking action by running: Set-DlpComplianceRule -Identity "RuleName" -BlockAccess $false -BlockAccessScope $null. 2. If the policy was applied to specific locations, remove those locations by running: Set-DlpCompliancePolicy -Identity "PolicyName" -ExchangeLocation $null -SharePointLocation $null -OneDriveLocation $null -TeamsLocation $null -PowerBILocation $null. 3. For SharePoint/OneDrive, remove any domain or SMTP block exceptions by running: Set-DlpComplianceRule -Identity "RuleName" -BlockAccessScope $null -ExceptIfRecipientDomainIs $null -ExceptIfRecipientSMTPContains $null. 4. Disable the policy entirely if needed by running: Set-DlpCompliancePolicy -Identity "PolicyName" -Enabled $false. 5. Monitor DLP alerts and reports to confirm that normal access is restored and no unintended data exposure occurs.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
