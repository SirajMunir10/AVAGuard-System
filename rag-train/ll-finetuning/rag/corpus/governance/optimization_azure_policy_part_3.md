# Optimization: Azure Policy

**Domain:** Governance
**Subdomain:** Azure Policy
**Incident Type:** Optimization

## Scenario / Query
How can I identify and remediate Azure Policy assignments that are not being evaluated due to an excluded scope, leading to compliance blind spots?

## Environment Context
- **Tenant Type:** Enterprise (multi-subscription)
- **Configuration:** Azure Policy assignments with exclusion (notScopes) configured at management group or subscription scope

## Symptoms
- Compliance dashboard shows lower-than-expected non-compliant resources
- Audit logs show no policy evaluation activity for certain subscriptions or resource groups
- Security baseline reports miss resources that should be covered by built-in policies

## Error Codes
N/A

## Root Causes
1. Policy assignment includes an exclusion scope (notScopes) that inadvertently removes critical resources from evaluation
2. Exclusions were added during troubleshooting without documenting the business justification

## Remediation Steps
1. 1. Use Azure Policy compliance data to list all assignments with exclusions: `Get-AzPolicyAssignment | Where-Object { $_.Properties.notScopes -ne $null }`
2. 2. Review each exclusion against the original policy intent and business requirements
3. 3. Remove unnecessary exclusions using `Set-AzPolicyAssignment -Name <assignmentName> -NotScope @()` or via Azure portal
4. 4. Re-evaluate compliance after removal and verify that expected resources are now assessed

## Validation
Run `Get-AzPolicyState -PolicyAssignmentName <assignmentName>` and confirm that previously excluded resources now appear in the compliance results.

## Rollback
Re-apply the original exclusion list using `Set-AzPolicyAssignment -Name <assignmentName> -NotScope @('<scope1>','<scope2>')`

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/concepts/assignment-structure#excluded-scopes>
