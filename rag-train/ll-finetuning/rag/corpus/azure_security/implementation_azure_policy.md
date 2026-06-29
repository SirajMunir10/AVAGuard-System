# Implementation: Azure Policy

**Domain:** Azure
**Subdomain:** Azure Policy
**Incident Type:** Implementation

## Scenario / Query
How to configure an AzurePodIdentityException for Azure Policy in AKS?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** Azure Kubernetes Service (AKS) with Azure Policy and Azure Active Directory pod identity

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. apiVersion: "aadpodidentity.k8s.io/v1"
2. kind: AzurePodIdentityException
3. metadata:
4. name: mic-exception
5. namespace: default
6. spec:
7. podLabels:
8. app: mic
9. component: mic
10. ---
11. apiVersion: "aadpodidentity.k8s.io/v1"
12. kind: AzurePodIdentityException
13. metadata:
14. name: aks-addon-exception
15. namespace: kube-system
16. spec:
17. podLabels:
18. kubernetes.azure.com/managedby: aks

## Validation
Run the following kubectl commands to confirm the AzurePodIdentityException resources are created and correctly configured:
1. kubectl get AzurePodIdentityException -n default -o yaml
   Verify that the 'mic-exception' resource exists with spec.podLabels.app=mic and spec.podLabels.component=mic.
2. kubectl get AzurePodIdentityException -n kube-system -o yaml
   Verify that the 'aks-addon-exception' resource exists with spec.podLabels.'kubernetes.azure.com/managedby'=aks.
3. Check that Azure Policy assignments for pod identity are not blocking pods in the 'default' namespace with labels 'app: mic' and 'component: mic', and pods in 'kube-system' with label 'kubernetes.azure.com/managedby: aks'.

## Rollback
If the AzurePodIdentityException resources cause issues, delete them using:
1. kubectl delete AzurePodIdentityException mic-exception -n default
2. kubectl delete AzurePodIdentityException aks-addon-exception -n kube-system
After deletion, verify that the resources are removed with:
   kubectl get AzurePodIdentityException -n default
   kubectl get AzurePodIdentityException -n kube-system
If the exceptions were part of a broader policy remediation, reapply the original Azure Policy assignment or restore from backup.

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/troubleshoot/general>
