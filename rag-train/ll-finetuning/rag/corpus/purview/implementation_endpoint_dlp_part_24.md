# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How to configure sensitive service domain groups in Microsoft Purview Endpoint DLP to control user actions like print, copy, save, upload, and paste on specific websites?

## Environment Context
- **Tenant Type:** Microsoft 365 with Purview
- **Configuration:** Endpoint DLP policy with Sensitive service domains

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Add a website to Sensitive service domains.
2. Set the policy to audit, block with override, or fully block user activity for actions: print from a website, copy data from a website, save a website as local files, upload or drag/drop a sensitive file to an excluded website, paste sensitive data to an excluded website.

## Validation
1. Verify that the sensitive service domain group includes the intended website by running: Get-DlpSensitiveServiceDomain | Where-Object {$_.Domain -eq 'https://example.com'}. 2. Confirm the Endpoint DLP policy is applied to the target devices by executing: Get-DlpCompliancePolicy -Identity 'Endpoint DLP Policy Name' | Format-List. 3. Test the policy by attempting a restricted action (e.g., copy data from the website) on a monitored device and check the DLP activity report in the Microsoft Purview compliance portal for an audit event. 4. Validate that the action is blocked or audited as configured by reviewing the policy rule details: Get-DlpComplianceRule -Policy 'Endpoint DLP Policy Name' | Where-Object {$_.Name -eq 'Sensitive Service Domain Rule'}.

## Rollback
1. Remove the website from the sensitive service domain group by running: Remove-DlpSensitiveServiceDomain -Domain 'https://example.com'. 2. If the policy rule was created specifically for this domain, disable or delete the rule: Set-DlpComplianceRule -Identity 'Sensitive Service Domain Rule' -State Disabled. 3. Revert the policy action settings to the previous state (e.g., change from 'Block' to 'Audit only') using: Set-DlpComplianceRule -Identity 'Sensitive Service Domain Rule' -AccessScope 'Audit'. 4. Confirm the rollback by repeating the validation steps to ensure the original behavior is restored.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
