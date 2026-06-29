# Troubleshooting: Azure Policy

**Domain:** Azure
**Subdomain:** Azure Policy
**Incident Type:** Troubleshooting

## Scenario / Query
I'm seeing a large number of updates on constraint.gatekeeper.sh CRDs and other Gatekeeper resources

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** AKS cluster with Azure Policy add-on and standalone Gatekeeper installed

## Symptoms
- Large number of updates on constraint.gatekeeper.sh CRDs
- Large number of updates on other Gatekeeper resources

## Error Codes
N/A

## Root Causes
1. Standalone instance of Gatekeeper installed alongside the addon's Gatekeeper instance

## Remediation Steps
1. Check for the existence of multiple Gatekeeper installations
2. Remove all Gatekeeper components not managed by AKS

## Validation
1. Run 'kubectl get pods -n gatekeeper-system' to verify only the Azure Policy add-on's Gatekeeper pods are running. 2. Run 'kubectl get validatingwebhookconfigurations' and confirm only the webhook named 'gatekeeper-validating-webhook-configuration' exists. 3. Run 'kubectl get constraint.gatekeeper.sh --all-namespaces' and verify no unexpected constraints are present. 4. Check the Azure Policy add-on status via 'kubectl get pods -n kube-system | grep azure-policy' to ensure it is healthy.

## Rollback
1. If the removal of standalone Gatekeeper causes issues, reinstall it using the original installation method (e.g., Helm: 'helm install gatekeeper/gatekeeper --name-template=gatekeeper --namespace gatekeeper-system --create-namespace'). 2. If the Azure Policy add-on becomes unhealthy, restart its pods: 'kubectl delete pods -n kube-system -l app=azure-policy'. 3. If constraints are missing, reapply them from backup or source manifests.

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/troubleshoot/general>
