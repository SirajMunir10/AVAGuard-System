# Troubleshooting: Azure Policy (Error: cannot re-use a name that is still in use)

**Domain:** Azure
**Subdomain:** Azure Policy
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve a Helm Chart installation failure for Azure Policy add-on when the name already exists?

## Environment Context
- **Tenant Type:** Azure Kubernetes Service (AKS) or Kubernetes cluster with Azure Policy add-on
- **Configuration:** Helm Chart named azure-policy-addon

## Symptoms
- helm install azure-policy-addon command fails
- Error: cannot re-use a name that is still in use

## Error Codes
- `Error: cannot re-use a name that is still in use`

## Root Causes
1. The Helm Chart with the name azure-policy-addon was already installed or partially installed

## Remediation Steps
1. Follow the instructions to remove the Azure Policy for Kubernetes add-on
2. Rerun the helm install azure-policy-addon command

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/troubleshoot/general>
