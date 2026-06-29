# Troubleshooting: Information Barriers

**Domain:** Purview
**Subdomain:** Information Barriers
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot when segments are listed but no information barrier policies are assigned to those segments?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Information Barriers policies

## Symptoms
- Segments are listed but no information barrier policies are assigned to those segments

## Error Codes
N/A

## Root Causes
1. No information barrier policy defined for the applicable segments
2. Existing information barrier policy not assigned to the applicable segment

## Remediation Steps
1. Define a new information barrier policy for each applicable segment
2. Edit an existing information barrier policy to assign it to the applicable segment
3. Run the Start-InformationBarrierPoliciesApplication cmdlet to apply all active Information Barriers policies

## Validation
1. Run Get-InformationBarrierPolicy to list all policies and verify that each applicable segment has at least one policy assigned (check the AssignedSegment field).
2. Run Get-InformationBarrierPolicyApplicationStatus to confirm the last policy application completed successfully (status should be 'Completed').
3. Run Get-InformationBarrierRecipientStatus -Identity <user@domain> for a test user in each segment to verify the policy is applied (check the 'ExoPolicyId' and 'State' fields).

## Rollback
1. If a new policy was defined and causes issues, run Remove-InformationBarrierPolicy -Identity <PolicyId> to delete it.
2. If an existing policy was edited and causes issues, run Set-InformationBarrierPolicy -Identity <PolicyId> -AssignedSegment <OriginalSegment> to revert the assignment.
3. If the policy application fails, run Start-InformationBarrierPoliciesApplication -Force to reapply all policies from a clean state.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/information-barriers-troubleshooting>
