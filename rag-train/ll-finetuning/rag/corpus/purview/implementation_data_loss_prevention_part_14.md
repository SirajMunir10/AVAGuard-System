# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to create and deploy data loss prevention policies by mapping common policy intent scenarios to configuration options?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Microsoft Purview DLP policy deployment

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Map common policy intent scenarios to configuration options
2. Configure those options

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Confirm the policy appears in the list with the intended configuration (e.g., locations, conditions, actions). 3. Use the DLP policy test mode (simulate) to verify the policy triggers as expected without blocking. 4. Run Get-DlpCompliancePolicy -Identity "<PolicyName>" | Format-List in Exchange Online PowerShell to confirm policy settings. 5. Check audit logs for policy match events using Search-UnifiedAuditLog -Operations "DLPRuleMatch".

## Rollback
1. In Microsoft Purview compliance portal > Data Loss Prevention > Policies, select the policy and choose 'Delete policy' or 'Disable policy'. 2. If the policy was deployed via PowerShell, run Remove-DlpCompliancePolicy -Identity "<PolicyName>" -Confirm:$false. 3. Revert any configuration changes made to existing policies by restoring from backup or reapplying previous settings. 4. If the policy was in test mode, disable it and remove any test notifications. 5. Monitor for any residual effects and re-enable previous policies if necessary.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
