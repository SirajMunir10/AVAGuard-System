# Troubleshooting: Azure Policy (!: event not found)

**Domain:** Azure
**Subdomain:** Azure Policy
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve a Helm Chart installation failure for Azure Policy add-on due to a password containing a comma?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** Azure Policy add-on installed via Helm Chart

## Symptoms
- helm install azure-policy-addon command fails
- Error: !: event not found
- Error: failed parsing --set data: key "<key>" has no value (cannot end with ,)

## Error Codes
- `!: event not found`
- `failed parsing --set data: key "<key>" has no value (cannot end with ,)`

## Root Causes
1. The generated password includes a comma ( , ), which the Helm Chart is splitting on.

## Remediation Steps
1. When you run helm install azure-policy-addon, escape the comma ( , ) in the password value with a backslash ( \ ).

## Validation
Run the following command to verify that the Azure Policy add-on Helm release is installed successfully: helm list -n <namespace> --filter 'azure-policy-addon'. Confirm the STATUS column shows 'deployed'. Then run: kubectl get pods -n <namespace> -l app.kubernetes.io/name=azure-policy-addon --no-headers | wc -l to ensure at least one pod is running. Finally, check the add-on logs for any remaining parsing errors: kubectl logs -n <namespace> deployment/azure-policy-addon --tail=50 | grep -i 'error\|fail'.

## Rollback
If the remediation fails or causes issues, uninstall the failed release: helm uninstall azure-policy-addon -n <namespace>. Then reinstall using a password that does not contain a comma, or properly escape the comma by enclosing the entire --set value in single quotes and escaping the comma with a backslash, e.g., --set azurePolicyConnectString='<password_with_escaped_comma>'. Alternatively, generate a new password without commas and rerun: helm install azure-policy-addon --set azurePolicyConnectString=<new_password>.

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/troubleshoot/general>
