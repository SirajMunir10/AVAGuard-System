# Hardening: Policy Enforcement

**Domain:** Governance
**Subdomain:** Policy Enforcement
**Incident Type:** Hardening

## Scenario / Query
A security administrator notices that several Azure subscriptions are not enforcing Azure Policy guest configuration requirements for Windows and Linux machines. How can the administrator identify and remediate non-compliant resources using built-in Azure Policy definitions to harden the environment?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Azure Policy guest configuration assignments are missing or not applied to virtual machines

## Symptoms
- Azure Policy compliance dashboard shows non-compliant resources for guest configuration policies
- Security Center recommendations indicate missing guest configuration extensions on VMs
- Audit logs show that VMs are not meeting baseline security settings

## Error Codes
N/A

## Root Causes
1. Guest configuration policy assignments were not deployed to all subscriptions or management groups
2. Required guest configuration extensions are not installed on VMs
3. Policy initiative for guest configuration was not assigned at the appropriate scope

## Remediation Steps
1. Assign the built-in policy initiative 'Deploy prerequisites to enable guest configuration policies on virtual machines' at the management group or subscription scope
2. Use the Azure portal to identify non-compliant VMs and deploy the guest configuration extension automatically via policy remediation tasks
3. Alternatively, use Azure PowerShell cmdlet Start-AzPolicyRemediation to trigger remediation for non-compliant resources
4. Verify that the guest configuration extension is installed and that the machine reports compliance within 15 minutes

## Validation
Navigate to Azure Policy > Compliance, select the assigned initiative, and confirm that all VMs show 'Compliant' status for guest configuration policies.

## Rollback
Remove the policy assignment for the guest configuration initiative at the scope, or disable the individual policy definitions within the initiative.

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/concepts/guest-configuration>
