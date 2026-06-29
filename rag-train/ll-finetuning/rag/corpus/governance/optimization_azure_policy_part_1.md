# Optimization: Azure Policy

**Domain:** Governance
**Subdomain:** Azure Policy
**Incident Type:** Optimization

## Scenario / Query
How can I identify and remediate Azure Policy assignments that are not being evaluated due to scope mismatch or exclusion, to ensure full compliance coverage?

## Environment Context
- **Tenant Type:** Enterprise (multiple management groups)
- **Configuration:** Azure Policy assignments at management group or subscription scope with exclusions or non-matching resource selectors

## Symptoms
- Compliance dashboard shows lower-than-expected coverage for a policy initiative
- Some resources are not being evaluated by a policy that should apply to them
- Policy evaluation logs show 'ScopeNotApplicable' or 'Excluded' entries

## Error Codes
N/A

## Root Causes
1. Policy assignment scope does not include all intended subscriptions or resource groups
2. Exclusions defined in the policy assignment remove certain resources from evaluation
3. Resource selectors in the policy definition do not match the target resources

## Remediation Steps
1. Review the policy assignment scope in the Azure portal or via PowerShell (Get-AzPolicyAssignment) and adjust it to cover all intended resources
2. Remove unnecessary exclusions from the policy assignment using Set-AzPolicyAssignment -NotScope
3. Update resource selectors in the policy definition to match the intended resource types or locations

## Validation
Run Get-AzPolicyState -PolicyAssignmentName <assignment> and verify that all expected resources are evaluated and compliant.

## Rollback
Reapply the previous scope, exclusions, or resource selectors using the same PowerShell cmdlets or Azure portal.

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources>
- <https://learn.microsoft.com/en-us/azure/governance/policy/concepts/assignment-structure>
