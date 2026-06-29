# Troubleshooting: Azure Policy (The subscription '{subId}' has been disabled for azure data-plane policy. Please contact support.)

**Domain:** Azure
**Subdomain:** Azure Policy
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve the error 'The subscription '{subId}' has been disabled for azure data-plane policy' when the add-on can reach the Azure Policy service endpoint?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** feature flag Microsoft.PolicyInsights/DataPlaneBlocked

## Symptoms
- The add-on can reach the Azure Policy service endpoint
- Error displayed: The subscription '{subId}' has been disabled for azure data-plane policy. Please contact support.

## Error Codes
- `The subscription '{subId}' has been disabled for azure data-plane policy. Please contact support.`

## Root Causes
1. The subscription was determined to be problematic
2. The feature flag Microsoft.PolicyInsights/DataPlaneBlocked was added to block the subscription

## Remediation Steps
1. Contact the feature team to investigate and resolve this issue

## Validation
1. Verify that the subscription is no longer blocked by checking the feature flag: run 'az feature show --namespace Microsoft.PolicyInsights --name DataPlaneBlocked --subscription <subId>' and confirm the output shows 'RegistrationState': 'Registered' or the flag is absent. 2. Confirm the add-on can successfully query Azure Policy data-plane endpoints by executing a test request, e.g., 'az policy event list --subscription <subId> --top 1' and verifying no error is returned. 3. Check the Azure Policy service health for the subscription using 'az rest --method get --uri https://management.azure.com/subscriptions/<subId>/providers/Microsoft.PolicyInsights/eventGridFilters?api-version=2019-10-01' and ensure a 200 response.

## Rollback
1. If the issue persists or reoccurs, re-block the subscription by re-enabling the feature flag: run 'az feature register --namespace Microsoft.PolicyInsights --name DataPlaneBlocked --subscription <subId>' and wait for the registration to complete. 2. Contact the Azure Policy feature team again to investigate the root cause and request re-blocking if needed. 3. As a temporary workaround, disable the add-on or restrict its network access to the Azure Policy service endpoint until the feature team resolves the underlying issue.

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/troubleshoot/general>
