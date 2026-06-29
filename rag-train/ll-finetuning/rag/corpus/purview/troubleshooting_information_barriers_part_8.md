# Troubleshooting: Information Barriers

**Domain:** Purview
**Subdomain:** Information Barriers
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot when no segments are listed for selected users in Information Barriers?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Information Barriers policies

## Symptoms
- No segments are listed for the selected users

## Error Codes
N/A

## Root Causes
1. Users are not assigned to any segment
2. No segment defined using a supported attribute for information barriers

## Remediation Steps
1. Assign users to an existing segment by editing their user profiles in Microsoft Entra ID
2. Define a segment by using a supported attribute for information barriers, then either define a new policy or edit an existing policy to include that segment
3. Run the Start-InformationBarrierPoliciesApplication cmdlet to apply all active Information Barriers policies

## Validation
1. Verify that the user is assigned to a segment by running: Get-InformationBarrierRecipientStatus -Identity <userUPN> | Format-List. 2. Confirm the segment definition uses a supported attribute (e.g., Department, MemberOf) by running: Get-InformationBarrierSegment -Identity <segmentName> | Format-List. 3. After assigning or redefining, run: Start-InformationBarrierPoliciesApplication. 4. Check that the user now appears in the segment by re-running Get-InformationBarrierRecipientStatus -Identity <userUPN> and confirming the 'Segment' field is populated.

## Rollback
1. If assignment to a segment was incorrect, remove the user from that segment by clearing the attribute used for segmentation (e.g., set Department to a value not in any segment) in Microsoft Entra ID. 2. If a segment was incorrectly defined, remove or edit the segment using: Remove-InformationBarrierSegment -Identity <segmentName> or Set-InformationBarrierSegment -Identity <segmentName> -<Attribute> <correctValue>. 3. Re-run Start-InformationBarrierPoliciesApplication to apply the rollback changes. 4. Verify the user no longer appears in the unwanted segment by running Get-InformationBarrierRecipientStatus -Identity <userUPN>.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/information-barriers-troubleshooting>
