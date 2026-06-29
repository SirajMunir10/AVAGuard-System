# Troubleshooting: iOS/iPadOS Enrollment (UserLicenseTypeInvalid)

**Domain:** Intune
**Subdomain:** iOS/iPadOS Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve iOS/iPadOS enrollment error: UserLicenseTypeInvalid - The device can't be enrolled because the user's account isn't yet a member of a required user group or the user doesn't have the correct license

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** Mobile device management authority

## Symptoms
- UserLicenseTypeInvalid error during iOS/iPadOS enrollment

## Error Codes
- `UserLicenseTypeInvalid`

## Root Causes
1. The user's account isn't yet a member of a required user group
2. The user doesn't have the correct license type for the mobile device management authority
3. Example: Intune has been set as the MDM authority, but the user has a System Center 2012 R2 Configuration Manager license

## Remediation Steps
N/A

## Validation
1. Verify the user has an appropriate Intune license assigned (e.g., Microsoft Intune, Enterprise Mobility + Security).
2. Confirm the user is a member of the required user group for enrollment (e.g., 'All Users' or a custom group).
3. Check the MDM authority is set to Intune in the Microsoft Intune admin center: Tenant administration > MDM authority.
4. Attempt iOS/iPadOS enrollment again and confirm no UserLicenseTypeInvalid error appears.

## Rollback
1. If the user was added to a group, remove the user from that group.
2. If the user's license was changed, reassign the previous license.
3. If the MDM authority was changed, revert to the previous MDM authority setting.
4. Re-test enrollment to confirm the original error returns.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-ios-enrollment-errors>
