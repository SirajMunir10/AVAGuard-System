# Troubleshooting: Information Barriers

**Domain:** Purview
**Subdomain:** Information Barriers
**Incident Type:** Troubleshooting

## Scenario / Query
How to verify that segments are defined correctly for Information Barriers?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Organization segments for Information Barriers

## Symptoms
- Information Barriers policy not working as expected

## Error Codes
N/A

## Root Causes
1. Incorrect segment definition

## Remediation Steps
1. Use the Get-OrganizationSegment cmdlet to review the list of results. Example: Get-OrganizationSegment -Identity c96e0837-c232-4a8a-841e-ef45787d8fcd
2. Review the details for the segment.
3. If necessary, edit a segment and then reuse the Start-InformationBarrierPoliciesApplication cmdlet.
4. If issues persist, contact Microsoft Support.

## Validation
After running Get-OrganizationSegment, confirm that the segment details match the intended user groups.

## Rollback
Edit the segment definition to correct any misconfiguration, then reapply policies using Start-InformationBarrierPoliciesApplication.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/information-barriers-troubleshooting>
