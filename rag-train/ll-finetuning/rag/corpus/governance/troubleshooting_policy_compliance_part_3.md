# Troubleshooting: Policy Compliance (UserError: RequestDisallowedByPolicy)

**Domain:** Governance
**Subdomain:** Policy Compliance
**Incident Type:** Troubleshooting

## Scenario / Query
A user reports that Azure Policy denies creation of a storage account even though the policy appears to be in 'audit' mode. How do I troubleshoot this behavior?

## Environment Context
- **Tenant Type:** Enterprise (Azure AD tenant with Azure Policy assignments)
- **Configuration:** A custom Azure Policy initiative assigned at the subscription scope with one policy set to 'audit' effect and another set to 'deny' effect for storage account creation.

## Symptoms
- Storage account creation fails with a generic 'disallowed by policy' error
- Azure Policy compliance dashboard shows the storage account resource as 'Non-compliant'
- The user expected only an audit warning, not a denial

## Error Codes
- `UserError: RequestDisallowedByPolicy`

## Root Causes
1. A second policy in the same initiative uses the 'deny' effect for the same resource type, overriding the audit-only policy
2. The policy assignment scope or exclusion is misconfigured, causing a deny policy to apply unexpectedly

## Remediation Steps
1. 1. In the Azure portal, navigate to Policy > Compliance and locate the non-compliant storage account resource.
2. 2. Select the resource to view the specific policy or initiative that caused the denial.
3. 3. Review the policy definition(s) assigned to the subscription scope and identify any policy with effect 'deny' that targets storage accounts.
4. 4. If the deny policy is unintended, either change its effect to 'audit' or remove it from the initiative assignment.
5. 5. After modification, wait for the next policy evaluation cycle (typically 30 minutes) or trigger an on-demand evaluation using: `Start-AzPolicyComplianceScan -ResourceGroupName <rg>`
6. 6. Retry the storage account creation.

## Validation
Create a test storage account in the same subscription and resource group. The creation should succeed if the deny policy was the cause. Verify the resource appears as 'Compliant' in the Policy compliance dashboard.

## Rollback
If the deny policy was intentionally required, re-add it to the initiative assignment and revert any effect changes. Alternatively, add an exclusion for the specific resource group or subscription if the policy should not apply there.

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/troubleshoot/general#requestdisallowedbypolicy>
