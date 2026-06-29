# Troubleshooting: Azure Policy (failed to fetch token, service not reachable)

**Domain:** Azure
**Subdomain:** Azure Policy
**Incident Type:** Troubleshooting

## Scenario / Query
The Azure Policy add-on for AKS is unable to reach the Azure Policy service endpoint due to egress restrictions.

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** AKS cluster with egress locked down

## Symptoms
- The add-on can't reach the Azure Policy service endpoint
- Returns error: failed to fetch token, service not reachable
- Returns error: Error getting file 'Get https://raw.githubusercontent.com/Azure/azure-policy/master/built-in-references/Kubernetes/container-allowed-images/template.yaml: dial tcp 151.101.228.133.443: connect: connection refused

## Error Codes
- `failed to fetch token, service not reachable`
- `Error getting file 'Get https://raw.githubusercontent.com/Azure/azure-policy/master/built-in-references/Kubernetes/container-allowed-images/template.yaml: dial tcp 151.101.228.133.443: connect: connection refused`

## Root Causes
1. Cluster egress is locked down

## Remediation Steps
1. Ensure that the domains and ports mentioned in the following article are open: Required outbound network rules and fully qualified domain names (FQDNs) for AKS clusters

## Validation
1. Verify that the AKS cluster's egress firewall or network security group rules allow outbound HTTPS (port 443) to the required FQDNs for Azure Policy: `*.policy.core.windows.net`, `*.blob.core.windows.net`, `raw.githubusercontent.com`, and `dc.services.visualstudio.com`. Use `az aks show --resource-group <rg> --name <cluster> --query 'networkProfile.outboundType'` to confirm outbound type. 2. Deploy a test pod with `curl` and run `kubectl exec <pod> -- curl -v https://gov-prod.policy.core.windows.net` and `kubectl exec <pod> -- curl -v https://raw.githubusercontent.com/Azure/azure-policy/master/built-in-references/Kubernetes/container-allowed-images/template.yaml` to confirm connectivity. 3. Check the Azure Policy add-on logs using `kubectl logs -n kube-system -l app=azure-policy` for the absence of 'failed to fetch token' or 'connection refused' errors. 4. Run `az policy state list --resource <aks-cluster-id>` to confirm policy evaluations are succeeding.

## Rollback
1. Revert any changes made to egress firewall rules or network security groups to their previous state. 2. If a custom route table or Azure Firewall was modified, restore the previous rule set from backup or configuration management. 3. Restart the Azure Policy add-on pods to clear any cached state: `kubectl delete pods -n kube-system -l app=azure-policy`. 4. Confirm the original error reappears by checking add-on logs: `kubectl logs -n kube-system -l app=azure-policy | grep -E 'failed to fetch token|connection refused'`. 5. If the cluster was recreated, redeploy the original AKS cluster configuration without the egress changes.

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/troubleshoot/general>
