# Hardening: Data Loss Prevention (DLP) Policy Configuration

**Domain:** Purview
**Subdomain:** Data Loss Prevention (DLP) Policy Configuration
**Incident Type:** Hardening

## Scenario / Query
How to avoid performance issues when configuring DLP policy file extension conditions?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy rules with file extension condition

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Avoid including the following file extensions in policy rules: .dll, .exe, .mui, .ost, .pf, .pst.
2. These extensions might significantly increase CPU load.

## Validation
1. Confirm that the DLP policy rule no longer includes any of the prohibited file extensions (.dll, .exe, .mui, .ost, .pf, .pst) by running: Get-DlpComplianceRule | Where-Object {$_.FileExtension -match '\.(dll|exe|mui|ost|pf|pst)$'} | Format-List Name, FileExtension. 2. Verify that the policy rule still applies to the intended file types by checking the remaining file extensions in the rule: Get-DlpComplianceRule -Identity "<PolicyRuleName>" | Select-Object -ExpandProperty FileExtension. 3. Monitor CPU load on the DLP processing servers for at least 24 hours post-change using Performance Monitor counters (e.g., \Processor(_Total)\% Processor Time) to ensure no abnormal spikes occur.

## Rollback
1. Restore the original DLP policy rule that included the prohibited file extensions by running: Set-DlpComplianceRule -Identity "<PolicyRuleName>" -FileExtension @(".dll", ".exe", ".mui", ".ost", ".pf", ".pst") -Force. 2. If the rule was removed, recreate it using the original parameters: New-DlpComplianceRule -Name "<OriginalRuleName>" -Policy "<PolicyName>" -FileExtension @(".dll", ".exe", ".mui", ".ost", ".pf", ".pst") -Action ... (include other original actions). 3. Confirm the rollback by running: Get-DlpComplianceRule | Where-Object {$_.FileExtension -match '\.(dll|exe|mui|ost|pf|pst)$'} | Format-List Name, FileExtension.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
