# Troubleshooting: iOS Enrollment (MdmAuthorityNotDefined)

**Domain:** Intune
**Subdomain:** iOS Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve the MdmAuthorityNotDefined error during iOS enrollment in Microsoft Intune?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Mobile device management authority not set

## Symptoms
- MdmAuthorityNotDefined error during iOS enrollment

## Error Codes
- `MdmAuthorityNotDefined`

## Root Causes
1. The mobile device management authority hasn't been set in Intune

## Remediation Steps
1. Review item #1 in the Step 6: Enroll mobile devices and install an app section in Get started with a 30-day trial of Microsoft Intune

## Validation
1. Open the Microsoft Intune admin center (https://intune.microsoft.com).
2. Navigate to Tenant administration > MDM authority.
3. Verify that the MDM authority is set to Microsoft Intune (not None or unset).
4. Attempt an iOS enrollment again and confirm that the MdmAuthorityNotDefined error no longer appears.

## Rollback
1. If the MDM authority was changed from a previous value (e.g., Configuration Manager), set it back to that original value via Tenant administration > MDM authority.
2. If the authority was set to Microsoft Intune for the first time and causes issues, contact Microsoft Support to revert the authority setting, as this change is irreversible without assistance.
3. Document the original MDM authority setting before any changes.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-ios-enrollment-errors>
