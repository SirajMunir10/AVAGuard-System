# Implementation: Endpoint Data Loss Prevention (DLP)

**Domain:** Purview
**Subdomain:** Endpoint Data Loss Prevention (DLP)
**Incident Type:** Implementation

## Scenario / Query
How to configure DLP policy to detect copying protected files to a network share?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP settings, network share coverage and exclusions

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the 'Copy to a network share' condition in DLP policy to detect when protected files are copied or moved from an onboarded device to any network share.
2. For more information, see Endpoint activities you can monitor and take action on and Network share coverage and exclusions.

## Validation
1. Confirm the DLP policy is enabled and assigned to the correct scope: `Get-DlpCompliancePolicy -Identity "PolicyName" | Format-List Name, Enabled, ExchangeLocation, SharePointLocation, OneDriveLocation, EndpointLocation, TeamsLocation`
2. Verify the policy includes the 'Copy to a network share' condition: `Get-DlpComplianceRule -Policy "PolicyName" | Where-Object {$_.Conditions -like "*CopyToNetworkShare*"} | Format-Table Name, Conditions`
3. Test the policy by copying a protected file from an onboarded device to a network share and confirm an audit event is generated: `Search-UnifiedAuditLog -StartDate (Get-Date).AddHours(-1) -EndDate (Get-Date) -Operations "FileCopiedToNetworkShare" -ResultSize 10`
4. Review DLP alerts in the Microsoft Purview compliance portal: Navigate to Data Loss Prevention > Alerts and filter by policy name.

## Rollback
1. Disable the DLP policy to stop enforcement: `Set-DlpCompliancePolicy -Identity "PolicyName" -Enabled $false`
2. Remove the 'Copy to a network share' condition from the rule: `$rule = Get-DlpComplianceRule -Policy "PolicyName" -Identity "RuleName"`
   `$rule.Conditions = $rule.Conditions | Where-Object {$_.Type -ne "CopyToNetworkShare"}`
   `Set-DlpComplianceRule -Identity "RuleName" -Policy "PolicyName" -Conditions $rule.Conditions`
3. If the policy is no longer needed, delete it: `Remove-DlpCompliancePolicy -Identity "PolicyName"`
4. Verify removal: `Get-DlpCompliancePolicy -Identity "PolicyName"` should return no results.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
