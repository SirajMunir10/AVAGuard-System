# Hardening: Information Barriers

**Domain:** Purview
**Subdomain:** Information Barriers
**Incident Type:** Hardening

## Scenario / Query
How to remove an Information Barriers policy from a single user by editing their profile in Microsoft Entra?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Information Barriers policies assigned to segments

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. If you must remove a policy from a single user, consider editing that user's profile in Microsoft Entra so that the user is no longer included in a segment that's affected by information barriers.
2. To remove a user from a segment that's affected by information barriers, update the user's profile information in Microsoft Entra ID.

## Validation
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) as a user with the Identity Administrator role.
2. Navigate to Identity > Users > All users.
3. Select the target user and click Edit properties.
4. Verify that the user's attributes (e.g., Department, JobTitle, or custom extension attributes) no longer match the segment definition used by the Information Barriers policy.
5. Run the following PowerShell cmdlet to confirm the user is not assigned to any segment: `Get-InformationBarrierPolicy -User <UserPrincipalName>` (if using the Exchange Online PowerShell module).
6. Confirm that the user can communicate with users outside the previously restricted segment by sending a test message.

## Rollback
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) as a user with the Identity Administrator role.
2. Navigate to Identity > Users > All users.
3. Select the target user and click Edit properties.
4. Restore the user's attributes (e.g., Department, JobTitle, or custom extension attributes) to the original values that matched the segment definition.
5. Run the following PowerShell cmdlet to verify the user is reassigned to the segment: `Get-InformationBarrierPolicy -User <UserPrincipalName>` (if using the Exchange Online PowerShell module).
6. Wait for the Information Barriers policy to apply (may take up to 30 minutes) and confirm that the user's communications are restricted as before.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/information-barriers-troubleshooting>
