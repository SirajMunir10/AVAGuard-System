# Troubleshooting: Azure Policy (StatusCode=500)

**Domain:** Azure
**Subdomain:** Azure Policy
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve the error 'The resource provider 'Microsoft.PolicyInsights' is not registered in subscription' when using Azure Policy add-on?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- The add-on logs display one of the following errors: 'The resource provider 'Microsoft.PolicyInsights' is not registered in subscription '{subId}'. See https://aka.ms/policy-register-subscription for how to register subscriptions.'
- The add-on logs display: 'policyinsightsdataplane.BaseClient#CheckDataPolicyCompliance: Failure responding to request: StatusCode=500 -- Original Error: autorest/azure: Service returned an error. Status=500 Code="InternalServerError" Message="Encountered an internal server error.'

## Error Codes
- `StatusCode=500`
- `Code="InternalServerError"`

## Root Causes
1. The Microsoft.PolicyInsights resource provider isn't registered in the cluster subscription.

## Remediation Steps
1. Register the Microsoft.PolicyInsights resource provider in the cluster subscription. For instructions, see Register a resource provider.

## Validation
Run 'az provider show --namespace Microsoft.PolicyInsights --query "registrationState" -o tsv' and verify the output is 'Registered'. Also run 'az provider list --query "[?namespace=='Microsoft.PolicyInsights'].registrationState" -o tsv' to confirm.

## Rollback
If registration causes issues, run 'az provider unregister --namespace Microsoft.PolicyInsights' to revert the registration.

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/troubleshoot/general>
- <https://aka.ms/policy-register-subscription>
