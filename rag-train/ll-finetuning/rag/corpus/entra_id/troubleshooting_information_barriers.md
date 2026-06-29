# Troubleshooting: Information Barriers

**Domain:** Entra ID
**Subdomain:** Information Barriers
**Incident Type:** Troubleshooting

## Scenario / Query
How to remove a user from a segment affected by information barriers?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Information Barriers policies active

## Symptoms
- User is incorrectly assigned to a segment that is affected by information barriers

## Error Codes
N/A

## Root Causes
1. User's profile information in Microsoft Entra ID needs to be updated

## Remediation Steps
1. Update the user's profile information in Microsoft Entra ID
2. Wait about 30 minutes for the FwdSync operation to finish
3. Or, run the Start-InformationBarrierPoliciesApplication cmdlet to apply all active Information Barriers policies

## Validation
1. Verify the user's profile attributes (e.g., department, custom attributes) in Microsoft Entra ID have been updated correctly using the Microsoft Entra admin center or Get-MgUser cmdlet.
2. Run Get-InformationBarrierPolicy to list active policies and confirm the user is no longer in the affected segment.
3. Run Get-InformationBarrierRecipientStatus -Identity <user@domain.com> to check the user's current segment assignment and policy application status.
4. If the policy was manually applied, run Start-InformationBarrierPoliciesApplication and then re-run Get-InformationBarrierRecipientStatus to confirm the user is removed from the incorrect segment.

## Rollback
1. Revert the user's profile attributes in Microsoft Entra ID to their previous values using the Microsoft Entra admin center or Update-MgUser cmdlet.
2. If the policy was manually applied, run Start-InformationBarrierPoliciesApplication to reapply the original policies.
3. Run Get-InformationBarrierRecipientStatus -Identity <user@domain.com> to confirm the user is reassigned to the original segment.
4. If the rollback causes further issues, contact Microsoft Support with the tenant ID and user details.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/information-barriers-troubleshooting>
