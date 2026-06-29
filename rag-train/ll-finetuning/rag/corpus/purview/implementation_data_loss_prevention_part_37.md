# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to structure a DLP policy with multiple rules and set rule execution priority?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy rule priority

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. A policy contains one or more rules.
2. Rules are executed sequentially, starting with the highest-priority rule in each policy.

## Validation
1. Connect to Exchange Online PowerShell: Connect-ExchangeOnline
2. Run: Get-DlpCompliancePolicy | Format-List Name,Priority,Mode
3. For each policy, run: Get-DlpComplianceRule -Policy "<PolicyName>" | Sort-Object Priority | Format-Table Name,Priority,Mode
4. Confirm that rules are listed in the intended order (lowest Priority number = highest priority) and that the policy Mode is 'Enable'.
5. Test the policy by sending a test email or file containing sensitive data (e.g., credit card number) to verify that the highest-priority rule triggers first and subsequent rules are evaluated as expected.

## Rollback
1. Connect to Exchange Online PowerShell: Connect-ExchangeOnline
2. To revert rule priority, run: Set-DlpComplianceRule -Identity "<RuleName>" -Priority <OriginalPriorityNumber>
3. If the entire policy must be removed, run: Remove-DlpCompliancePolicy -Identity "<PolicyName>" -Confirm:$false
4. To restore a deleted policy, re-create it using the original parameters from backup or documentation.
5. Verify rollback by running: Get-DlpCompliancePolicy | Format-List Name,Priority,Mode and Get-DlpComplianceRule -Policy "<PolicyName>" | Sort-Object Priority | Format-Table Name,Priority,Mode

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
