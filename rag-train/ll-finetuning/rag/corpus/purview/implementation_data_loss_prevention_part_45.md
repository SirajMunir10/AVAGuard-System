# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
What are the halting and non-halting actions for Exchange DLP policy rules?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Exchange DLP policy rules

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Most Exchange rules are non-halting; non-halting actions are applied after processing subsequent rules and policies.
2. When a halting action is triggered (e.g., Restrict access or encrypt the content in Microsoft 365 locations), Purview stops processing any subsequent rules.
3. If an action is neither halting nor non-halting (e.g., Forward the message for approval to sender's manager), Purview waits for the result before continuing; if manager approves, it behaves as non-halting; if manager rejects, it behaves as halting.

## Validation
1. Connect to Exchange Online PowerShell using Connect-ExchangeOnline. 2. Run Get-DlpComplianceRule | Format-List Name,Mode,RuleVersion,Action to list all DLP rules. 3. For each rule, check the Action property: if the action is 'RestrictAccess' or 'Encrypt', note that it is halting. 4. Verify that when a halting action is triggered, no subsequent rules are processed by reviewing the audit logs for DLP rule matches (Search-UnifiedAuditLog -Operations DlpRuleMatch). 5. For non-halting actions (e.g., 'NotifyUser'), confirm that subsequent rules are still evaluated by checking that multiple rule matches appear in the audit log for the same message.

## Rollback
1. If a halting action was incorrectly applied, remove or modify the rule using Remove-DlpComplianceRule -Identity <RuleName> or Set-DlpComplianceRule -Identity <RuleName> -Action <NonHaltingAction>. 2. If a non-halting action needs to become halting, update the rule with Set-DlpComplianceRule -Identity <RuleName> -Action RestrictAccess. 3. To restore default behavior, re-enable any disabled rules using Enable-DlpComplianceRule -Identity <RuleName>. 4. Verify changes by re-running Get-DlpComplianceRule and testing with a sample message.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
