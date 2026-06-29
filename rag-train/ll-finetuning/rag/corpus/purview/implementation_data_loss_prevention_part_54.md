# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How do I configure Block with override for DLP rules on devices?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP rules with action 'Audit or restrict activities on devices'

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Configure the rule action to Block with override.
2. When applied to a file, any attempt to perform a restricted action is blocked.
3. A notification is displayed with the option to override the restriction.
4. If the user chooses to override, the action is permitted for a period of 1 minute, during which the user can retry the action without restriction.

## Validation
1. Confirm the DLP policy is assigned to the correct scope (e.g., Devices) and includes the action 'Block with override' by running: Get-DlpCompliancePolicy -Identity "<PolicyName>" | Format-List. 2. Verify the rule action is set to 'Block with override' by executing: Get-DlpComplianceRule -Policy "<PolicyName>" | Select-Object Name, Actions. 3. On a test device, attempt a restricted action (e.g., copy sensitive data to USB) and confirm the action is blocked and a notification appears with an override option. 4. Choose the override and verify the action is permitted for 1 minute, after which the restriction re-applies.

## Rollback
1. Remove the 'Block with override' action from the rule by setting it to 'Audit only' or 'Block' without override: Set-DlpComplianceRule -Identity "<RuleName>" -Policy "<PolicyName>" -BlockAccess $false -OverrideOption None. 2. If the entire policy is problematic, disable it: Set-DlpCompliancePolicy -Identity "<PolicyName>" -Enabled $false. 3. Confirm the change by running: Get-DlpComplianceRule -Policy "<PolicyName>" | Select-Object Name, Actions. 4. Test on a device to ensure the restricted action is no longer blocked or overridable as per the original configuration.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
