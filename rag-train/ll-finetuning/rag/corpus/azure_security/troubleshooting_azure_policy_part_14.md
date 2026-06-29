# Troubleshooting: Azure Policy

**Domain:** Azure
**Subdomain:** Azure Policy
**Incident Type:** Troubleshooting

## Scenario / Query
Why does a Kubernetes resource get created during a connectivity failure despite a deny policy being assigned?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** Azure Policy with Gatekeeper on Kubernetes cluster

## Symptoms
- Kubernetes resource is created despite a deny policy being assigned
- Resource is reported as non-compliant on Azure Policy compliance

## Error Codes
N/A

## Root Causes
1. Kubernetes cluster connectivity failure
2. Gatekeeper's fail-open behavior bypasses evaluation for newly created or updated resources

## Remediation Steps
1. Monitor the admission webhook metrics provided by the kube-apiserver for the error case
2. Azure Policy retains the last known policy on the cluster and keeps the guardrails in place

## Validation
1. Verify that the Azure Policy add-on for AKS is installed and the Gatekeeper version is up to date by running: kubectl get constrainttemplates -n gatekeeper-system. 2. Check the kube-apiserver audit logs for admission webhook failures during the time of the resource creation: kubectl logs -n kube-system <apiserver-pod> --tail=100 | grep 'admission webhook'. 3. Confirm that the deny policy is still assigned and active in Azure Policy by navigating to Azure Policy > Compliance and selecting the relevant policy. 4. Validate that the non-compliant resource is now blocked by attempting to create a similar resource: kubectl apply -f test-resource.yaml (should fail). 5. Review Gatekeeper metrics for fail-open events: kubectl get --raw /metrics | grep gatekeeper_failure.

## Rollback
1. If the remediation causes issues, re-enable the fail-open behavior by setting the '--admission-control-fail-open' flag to true on the kube-apiserver (if it was changed). 2. Restore the previous Gatekeeper version by redeploying the Azure Policy add-on with the earlier version: az aks enable-addons --addons azure-policy --name <cluster-name> --resource-group <rg-name> --no-wait. 3. If the deny policy was removed, reassign it via Azure Policy: az policy assignment create --name <policy-assignment-name> --policy <policy-definition-id> --scope <scope>. 4. Recreate any resources that were incorrectly deleted during the remediation by applying their original YAML manifests: kubectl apply -f original-resource.yaml. 5. Reset the kube-apiserver admission configuration to the previous state by editing the 'ValidatingWebhookConfiguration' or 'MutatingWebhookConfiguration' for Gatekeeper: kubectl edit validatingwebhookconfiguration gatekeeper-validating-webhook-configuration.

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/troubleshoot/general>
- <https://open-policy-agent.github.io/gatekeeper/website/docs/failing-closed#considerations>
