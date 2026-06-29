# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How do I configure Paste to Browser detection in DLP?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with Paste to supported browsers action

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Paste to supported browsers detects when users paste sensitive information into a text field or web form using Microsoft Edge, Google Chrome (with Microsoft Purview extension), or Mozilla Firefox (with Microsoft Purview extension).
2. Evaluation is independent of the classification of the source file.
3. Only certain rule conditions work with Paste to Browser events: Content contains, Content is not labeled.
4. Paste to Browser supports SITs, not Sensitivity Labels.
5. Paste to Browser doesn't evaluate on text smaller than 30 characters.
6. Advanced Classification isn't supported.
7. Contextual Summary doesn't show for Paste to Browser events.
8. Paste to Browser takes 2 seconds to evaluate before allowing the paste action.
9. IF JIT is configured to block on fallback, it blocks pasting.
10. Paste to Browser only classifies the first 4 MB of text from the clipboard.

## Validation
1. Open Microsoft Edge and navigate to a site that triggers the DLP policy (e.g., a web form).
2. Attempt to paste sensitive data (e.g., a credit card number) into the form.
3. Confirm that the paste is blocked and a DLP policy tip appears.
4. Run the following PowerShell command to verify the DLP rule is applied: Get-DlpComplianceRule -Identity "YourRuleName" | Format-List Name, Mode, RuleConditions, Actions
5. Check the DLP activity explorer for a PasteToBrowser event: Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-1) -EndDate (Get-Date) -Operations "DLPRuleMatch" | Where-Object {$_.AuditData.Contains('PasteToBrowser')}

## Rollback
1. Disable the DLP rule that enforces Paste to Browser detection: Set-DlpComplianceRule -Identity "YourRuleName" -State Disabled
2. Remove the Paste to supported browsers action from the rule: Set-DlpComplianceRule -Identity "YourRuleName" -RemoveAction "PasteToBrowser"
3. If the rule was newly created, delete it: Remove-DlpComplianceRule -Identity "YourRuleName"
4. Verify the change by attempting to paste sensitive data into a browser form and confirming the paste is allowed.
5. Monitor the DLP activity explorer to ensure no further PasteToBrowser events are logged.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
