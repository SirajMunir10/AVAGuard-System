# Troubleshooting: iOS Enrollment

**Domain:** Intune
**Subdomain:** iOS Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
ADE enrollment doesn't start when turning on an ADE-managed device assigned an enrollment profile

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** ADE enrollment profile created before ADE token uploaded to Intune

## Symptoms
- When you turn on an ADE-managed device that is assigned an enrollment profile, the Intune enrollment process isn't initiated

## Error Codes
N/A

## Root Causes
1. The enrollment profile is created before the ADE token is uploaded to Intune

## Remediation Steps
1. Edit the enrollment profile. You can make any change to the profile. The purpose is to update the modification time of the profile.
2. Synchronize ADE-managed devices: In the Microsoft Intune admin center, choose Devices > iOS > iOS enrollment > Enrollment program tokens > choose a token > Sync now. A sync request is sent to Apple.

## Validation
1. In the Microsoft Intune admin center, navigate to Devices > iOS > iOS enrollment > Enrollment program tokens. Select the relevant token and verify that the token status is 'Active' and the last sync timestamp is recent. 2. Go to Devices > iOS > iOS enrollment > Enrollment program tokens > choose the token > Devices. Confirm that the ADE-managed device appears in the list and its profile status is 'Assigned'. 3. On the target iOS device, perform a factory reset or erase all content and settings, then go through the setup assistant. Verify that the Remote Management screen appears and the enrollment profile is applied, leading to successful Intune enrollment.

## Rollback
1. If the remediation causes issues (e.g., devices fail to enroll or profiles are misapplied), edit the enrollment profile again to revert any changes made during remediation. 2. If the sync causes duplicate or incorrect device records, in the Intune admin center, go to Devices > iOS > iOS enrollment > Enrollment program tokens > choose the token > Devices, locate the affected device, and select 'Delete' to remove it from the token's device list. Then re-add the device using Apple Business Manager or Apple School Manager. 3. If enrollment still fails, verify the ADE token is valid and not expired by checking the token expiration date in the Intune admin center. If expired, renew the token via Apple Business Manager and upload the new token to Intune.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-ios-enrollment-errors>
