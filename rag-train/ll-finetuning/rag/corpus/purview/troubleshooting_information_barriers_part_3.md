# Troubleshooting: Information Barriers

**Domain:** Purview
**Subdomain:** Information Barriers
**Incident Type:** Troubleshooting

## Scenario / Query
How to verify that users are included in an Information Barriers policy?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Information Barriers policies

## Symptoms
- Users may not be subject to expected Information Barriers restrictions

## Error Codes
N/A

## Root Causes
1. Users not assigned to a segment
2. Segments not included in an Information Barriers policy
3. Policies not applied

## Remediation Steps
1. Use the Get-InformationBarrierRecipientStatus cmdlet with the Identity and Identity2 parameters to check user status. Example: Get-InformationBarrierRecipientStatus -Identity meganb -Identity2 alexw
2. If no segments are listed for the selected users: assign users to an existing segment by editing their user profiles in Microsoft Entra ID, or define a new segment using a supported attribute for information barriers, then define a new policy or edit an existing policy to include that segment, and run the Start-InformationBarrierPoliciesApplication cmdlet to apply all active policies.
3. If segments are listed but no policies are assigned: define a new information barrier policy for each applicable segment, or edit an existing policy to assign it to the applicable segment, and run the Start-InformationBarrierPoliciesApplication cmdlet.
4. If segments are listed and each is included in a policy: run Get-InformationBarrierPolicy to verify policies are active, run Get-InformationBarrierPoliciesApplicationStatus to verify policies are applied, and run Start-InformationBarrierPoliciesApplication to apply all active policies.

## Validation
Run Get-InformationBarrierRecipientStatus -Identity <value> -Identity2 <value> and review the findings. Also run Get-InformationBarrierPolicy and Get-InformationBarrierPoliciesApplicationStatus to confirm policies are active and applied.

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/information-barriers-troubleshooting>
