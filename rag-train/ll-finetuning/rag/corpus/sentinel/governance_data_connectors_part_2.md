# Governance: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Governance

## Scenario / Query
A security auditor notices that Microsoft Sentinel is ingesting logs from a subset of Azure subscriptions but not others, despite all subscriptions being under the same management group. The auditor wants to verify that Sentinel's data collection is governed by Azure Policy and that all subscriptions in the scope are compliant with the deployed policy initiative.

## Environment Context
- **Tenant Type:** Enterprise (Azure AD tenant with multiple subscriptions under a single management group)
- **Configuration:** Microsoft Sentinel workspace is deployed in a central subscription; Azure Policy initiative 'Enable Azure Sentinel for all subscriptions in a management group' is assigned at the management group scope.

## Symptoms
- Some subscriptions under the management group do not appear in the Sentinel workspace's data sources list.
- Azure Policy compliance dashboard shows non-compliant resources for the Sentinel deployment initiative.
- Security events and other logs from non-compliant subscriptions are missing from Sentinel.

## Error Codes
N/A

## Root Causes
1. The Azure Policy initiative assigned at the management group scope has not been remediated for non-compliant subscriptions.
2. The 'Deploy if not exists' effect in the policy requires a remediation task to be run after assignment to enable Sentinel on existing subscriptions.

## Remediation Steps
1. Navigate to Azure Policy in the Azure portal, select the initiative assignment for Sentinel deployment, and review the compliance status.
2. For each non-compliant subscription, create a remediation task to deploy the Sentinel data connector resources as defined in the policy.
3. Alternatively, use the Azure PowerShell cmdlet `Start-AzPolicyRemediation` to trigger remediation at scale for the initiative assignment.
4. After remediation, verify that the subscriptions appear in the Sentinel workspace under 'Data connectors' and that logs are flowing.

## Validation
Check the Azure Policy compliance dashboard for the initiative; all subscriptions should show as 'Compliant'. In Sentinel, navigate to 'Data connectors' and confirm that the expected subscriptions are listed with healthy data ingestion.

## Rollback
Remove the policy assignment from the management group scope, or delete the remediation tasks and manually disable data collection from the affected subscriptions in Sentinel.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/enable-sentinel-at-scale>
