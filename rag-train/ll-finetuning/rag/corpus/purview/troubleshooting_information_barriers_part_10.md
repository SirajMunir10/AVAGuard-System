# Troubleshooting: Information Barriers

**Domain:** Purview
**Subdomain:** Information Barriers
**Incident Type:** Troubleshooting

## Scenario / Query
How to verify that segments are listed and each is included in an information barrier policy?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Information Barriers policies

## Symptoms
- Segments are listed and each is included in an information barrier policy

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Run the Get-InformationBarrierPolicy cmdlet to verify that information barrier policies are active
2. Run the Get-InformationBarrierPoliciesApplicationStatus cmdlet to verify that the policies are applied
3. Run the Start-InformationBarrierPoliciesApplication cmdlet to apply all active Information Barriers policies

## Validation
1. Run `Get-InformationBarrierPolicy` to confirm that each segment is included in an active policy. 2. Run `Get-InformationBarrierPoliciesApplicationStatus` to verify that the policies are applied successfully. 3. If status is not 'Complete', run `Start-InformationBarrierPoliciesApplication` and re-check status.

## Rollback
1. If a policy was incorrectly applied, run `Remove-InformationBarrierPolicy -Identity <PolicyID>` to remove the policy. 2. Run `Start-InformationBarrierPoliciesApplication` to reapply remaining policies. 3. Verify with `Get-InformationBarrierPolicy` and `Get-InformationBarrierPoliciesApplicationStatus` that only intended policies are active.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/information-barriers-troubleshooting>
