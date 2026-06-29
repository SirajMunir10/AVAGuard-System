# Optimization: Cost Management + Billing

**Domain:** Azure
**Subdomain:** Cost Management + Billing
**Incident Type:** Optimization

## Scenario / Query
A customer notices that their Azure Advisor cost recommendations are not appearing for a specific subscription. They want to know why and how to enable cost recommendations.

## Environment Context
- **Tenant Type:** Enterprise (EA or MCA)
- **Configuration:** Subscription-level Azure Advisor configuration; cost recommendations require the 'Advisor' resource provider to be registered and the user to have the 'Advisor Cost Management' role or equivalent permissions.

## Symptoms
- Azure Advisor shows no cost recommendations for a subscription
- Cost recommendations tab is empty or missing
- Other recommendation types (security, reliability, performance) appear normally

## Error Codes
N/A

## Root Causes
1. The 'Microsoft.Advisor' resource provider is not registered for the subscription
2. The user does not have sufficient permissions (e.g., missing 'Advisor Cost Management' role or 'Reader' role on the subscription)
3. Cost data is not yet available (new subscription or recent enrollment change)

## Remediation Steps
1. Register the Microsoft.Advisor resource provider: Use Azure CLI: `az provider register --namespace Microsoft.Advisor` or PowerShell: `Register-AzResourceProvider -ProviderNamespace Microsoft.Advisor`
2. Assign the 'Advisor Cost Management' role (or a role with read access to cost data) to the user at the subscription scope
3. Wait up to 48 hours for cost data to populate after subscription creation or enrollment changes

## Validation
Run `az provider show --namespace Microsoft.Advisor --query registrationState` to confirm 'Registered'. Verify user permissions via Azure Portal IAM or `az role assignment list --assignee <user> --scope /subscriptions/<sub-id>`.

## Rollback
Unregister the provider only if required: `az provider unregister --namespace Microsoft.Advisor`. Remove custom role assignments if added.

## References
- <https://learn.microsoft.com/en-us/azure/advisor/troubleshoot-cost-recommendations>
