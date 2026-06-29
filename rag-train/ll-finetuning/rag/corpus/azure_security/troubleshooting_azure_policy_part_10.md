# Troubleshooting: Azure Policy (StatusCode=404)

**Domain:** Azure
**Subdomain:** Azure Policy
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve the Azure Policy add-on being unable to reach the service endpoint due to aad-pod-identity configuration?

## Environment Context
- **Tenant Type:** Azure Kubernetes Service (AKS) cluster with Azure Policy add-on and aad-pod-identity installed
- **Configuration:** aad-pod-identity component Node Managed Identity (NMI) pods modify nodes' iptables to intercept calls to the Azure instance metadata endpoint

## Symptoms
- The add-on is unable to reach the Azure Policy service endpoint
- Returns error: azure.BearerAuthorizer#WithAuthorization: Failed to refresh the Token for request to https://gov-prod-policy-data.trafficmanager.net/checkDataPolicyCompliance?api-version=2019-01-01-preview: StatusCode=404
- Returns error: adal: Refresh request failed. Status Code = '404'. Response body: getting assigned identities for pod kube-system/azure-policy-8c785548f-r882p in CREATED state failed after 16 attempts, retry duration [5]s, error: <nil>

## Error Codes
- `StatusCode=404`

## Root Causes
1. aad-pod-identity is installed on the cluster and the kube-system pods aren't excluded in aad-pod-identity
2. The aad-pod-identity component Node Managed Identity (NMI) pods modify the nodes' iptables to intercept calls to the Azure instance metadata endpoint, causing any request made to the metadata endpoint to be intercepted by NMI even if the pod doesn't use aad-pod-identity

## Remediation Steps
1. Exclude the system pods that have the kubernetes.azure.com/managedby: aks label in kube-system namespace in aad-pod-identity by configuring the AzurePodIdentityException CRD

## Validation
Run the following command to verify that the AzurePodIdentityException CRD is configured to exclude system pods with label 'kubernetes.azure.com/managedby: aks' in the kube-system namespace:
kubectl get AzurePodIdentityException -n kube-system -o yaml
Check that the output includes a spec.podSelector.matchLabels entry with 'kubernetes.azure.com/managedby: aks'. Then confirm the Azure Policy add-on pods are running without errors:
kubectl logs -n kube-system -l app=azure-policy --tail=50
Verify no 404 errors related to token refresh or identity assignment appear.

## Rollback
If the remediation causes issues, remove the AzurePodIdentityException CRD by running:
kubectl delete AzurePodIdentityException <exception-name> -n kube-system
Then restart the aad-pod-identity NMI pods to restore original iptables rules:
kubectl delete pods -n kube-system -l app=node-managed-identity
Wait for the NMI pods to restart and verify that the Azure Policy add-on behavior returns to the previous state.

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/troubleshoot/general>
