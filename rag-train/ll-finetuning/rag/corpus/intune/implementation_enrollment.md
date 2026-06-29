# Implementation: Enrollment

**Domain:** Intune
**Subdomain:** Enrollment
**Incident Type:** Implementation

## Scenario / Query
A tenant is configured with a Windows enrollment restriction that blocks Windows MDM enrollment for all users, but the administrator needs to allow enrollment only for users in a specific security group. How should the enrollment restriction be configured?

## Environment Context
- **Tenant Type:** Production
- **Configuration:** Default Windows enrollment restriction is set to Block for all users

## Symptoms
- Windows devices cannot enroll in Intune MDM
- Users report enrollment failure with no specific error message

## Error Codes
N/A

## Root Causes
1. The default enrollment restriction is set to Block for Windows platform, and no platform-specific exception has been configured for the allowed group

## Remediation Steps
1. 1. Sign in to the Microsoft Intune admin center (https://intune.microsoft.com)
2. 2. Navigate to Devices > Enroll devices > Enrollment device platform restrictions
3. 3. Select the default Windows restriction (or create a new one) and set 'Block' for Windows
4. 4. Under 'Exceptions', add the security group that should be allowed to enroll
5. 5. Save the configuration

## Validation
Attempt to enroll a Windows device with a user in the allowed group; the device should enroll successfully. Attempt with a user not in the group; enrollment should be blocked.

## Rollback
Remove the security group from the 'Exceptions' list, or set the default restriction to 'Allow' for Windows.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/create-device-platform-restrictions>
