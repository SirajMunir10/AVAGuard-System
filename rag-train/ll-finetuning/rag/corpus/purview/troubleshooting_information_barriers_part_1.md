# Troubleshooting: Information Barriers

**Domain:** Purview
**Subdomain:** Information Barriers
**Incident Type:** Troubleshooting

## Scenario / Query
How to verify that an Information Barriers policy is correctly applied and preventing communication between segments?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Information Barriers policies and segments

## Symptoms
- Users in Sales and Research segments may be communicating when they should not be

## Error Codes
N/A

## Root Causes
1. Incorrect policy definition or segment configuration

## Remediation Steps
1. Use the Get-InformationBarrierPolicy cmdlet together with the Identity parameter to retrieve policy details. Example: Get-InformationBarrierPolicy -Identity b42c3d0f-xyxy-4506-xyxy-bf2853b5df6f
2. Examine the results for AssignedSegment, SegmentsAllowed, and SegmentsBlocked values. For example, if AssignedSegment is Sales, SegmentsAllowed is empty, and SegmentsBlocked is Research, then the policy is working as expected.
3. If the policy seems incorrect, use the Get-OrganizationSegment cmdlet to review segment definitions. Example: Get-OrganizationSegment -Identity c96e0837-c232-4a8a-841e-ef45787d8fcd
4. If necessary, edit a segment and then reuse the Start-InformationBarrierPoliciesApplication cmdlet.
5. If issues persist, contact Microsoft Support.

## Validation
After running Get-InformationBarrierPolicy, confirm that AssignedSegment, SegmentsAllowed, and SegmentsBlocked values match the intended communication restrictions.

## Rollback
Edit the segment definition to correct any misconfiguration, then reapply policies using Start-InformationBarrierPoliciesApplication.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/information-barriers-troubleshooting>
