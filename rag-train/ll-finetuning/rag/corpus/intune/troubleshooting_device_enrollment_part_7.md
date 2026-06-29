# Troubleshooting: Device Enrollment

**Domain:** Intune
**Subdomain:** Device Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to collect basic information to troubleshoot device enrollment issues in Intune?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** MDM authority, enrollment method (BYOD or Apple ADE)

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Collect the exact error message.
2. Identify where the error message appears.
3. Determine when the problem started.
4. Check if enrollment has ever worked.
5. Identify the platform (Android, iOS/iPadOS, Windows) with the problem.
6. Determine how many users are affected (all or just some).
7. Determine how many devices are affected (all or just some).
8. Identify the MDM authority.
9. Determine how enrollment is being performed (e.g., BYOD or Apple ADE with enrollment profiles).

## Validation
1. Confirm the exact error message by reviewing the device enrollment logs in the Microsoft Intune admin center (Devices > Monitor > Enrollment failures).
2. Verify the MDM authority is set correctly by navigating to Tenant administration > MDM authority and ensuring it matches the expected value (e.g., Intune).
3. Check the enrollment method: For BYOD, review the enrollment profile assigned to the user; for Apple ADE, verify the enrollment profile and Apple Business Manager token status in Devices > iOS/iPadOS > iOS enrollment > Enrollment program tokens.
4. Validate that the problem started at a specific time by comparing enrollment failure timestamps with recent configuration changes (e.g., policy updates, token expiration).
5. Confirm whether enrollment has ever worked by checking historical enrollment success logs (Devices > Monitor > Enrollment successes) for the affected user or device.
6. Identify the platform (Android, iOS/iPadOS, Windows) by filtering enrollment failures by platform in the admin center.
7. Determine the scope: Check if all users or only some are affected by reviewing user-specific enrollment logs; similarly, check if all devices or only some are affected by device-specific logs.
8. Verify the number of affected users and devices by running a report: Devices > Monitor > Enrollment failures > Export for a detailed CSV.

## Rollback
1. If the MDM authority was changed incorrectly, revert it to the previous setting by navigating to Tenant administration > MDM authority and selecting the original authority (e.g., Office 365 or Intune).
2. If an enrollment profile was modified or deleted, restore the previous profile from backup or recreate it using the original settings (e.g., for Apple ADE, re-upload the token and reassign the profile).
3. If a policy change caused the issue, revert the policy to its previous state by editing the policy in the admin center and removing the problematic setting.
4. If a user or device was incorrectly blocked, remove the block by navigating to Devices > Enroll devices > Block enrollments and clearing the blocked entry.
5. If an enrollment restriction was applied, remove or modify the restriction in Devices > Enroll devices > Enrollment restrictions to allow the affected platform or user group.
6. If a token (e.g., Apple ADE token) expired or was revoked, renew the token by following the steps in Tenant administration > Connectors and tokens > Apple Business Manager and re-uploading the new token.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-device-enrollment-in-intune>
