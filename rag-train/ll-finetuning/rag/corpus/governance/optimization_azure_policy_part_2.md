# Optimization: Azure Policy

**Domain:** Governance
**Subdomain:** Azure Policy
**Incident Type:** Optimization

## Scenario / Query
An organization has deployed Azure Policy to enforce tagging on resources, but the policy is not evaluating newly created resources within the expected timeframe, causing compliance reporting delays. How can the evaluation schedule be optimized?

## Environment Context
- **Tenant Type:** Enterprise (multiple subscriptions)
- **Configuration:** Azure Policy with 'audit' or 'deny' effect on resource tags; default compliance scan interval is 24 hours

## Symptoms
- New resources do not appear in compliance results for up to 24 hours
- Compliance reports show stale data
- Manual trigger of evaluation is required to see current state

## Error Codes
N/A

## Root Causes
1. Azure Policy compliance scans run automatically every 24 hours by default
2. No on-demand evaluation trigger was configured for critical subscriptions

## Remediation Steps
1. Use Azure PowerShell or Azure CLI to trigger an on-demand compliance scan for the affected subscription: Start-AzPolicyComplianceScan -SubscriptionId '<subscription-id>' or az policy state trigger-scan --subscription '<subscription-id>'
2. For continuous optimization, consider using Azure Policy's 'Resource Provider mode' or 'Policy as Code' pipelines to trigger scans after resource creation
3. Review and adjust the policy assignment's 'Evaluation' settings if using custom initiative definitions

## Validation
Run the on-demand scan and verify that newly created resources appear in compliance results within minutes. Confirm that the compliance state matches the expected policy effect.

## Rollback
No rollback needed; on-demand scans are non-destructive. To revert to default behavior, simply stop triggering manual scans.

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/how-to/get-compliance-data>
