# Troubleshooting: Android Enrollment

**Domain:** Intune
**Subdomain:** Android Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
Cannot create a work profile on an Android device during Intune enrollment

## Environment Context
- **Tenant Type:** Intune managed
- **Configuration:** Android Enterprise personally owned work profile enrollment

## Symptoms
- Unable to create a work profile on the device
- Device meets Android Enterprise and OS version requirements but still fails

## Error Codes
N/A

## Root Causes
1. Existing work profile on the device
2. OEM restrictions preventing work profile creation

## Remediation Steps
1. Go to Settings > Passwords & accounts > Work to check for an existing work profile
2. If a work profile is not expected, remove it and try enrolling again
3. Install the Test DPC app from the Google Play Store and follow setup instructions to check if the device can create a sample work profile
4. If Test DPC fails to create a work profile, contact the device manufacturer for more details on work profile support

## Validation
1. On the Android device, navigate to Settings > Passwords & accounts > Work and confirm no existing work profile is listed.
2. If a work profile was removed, attempt Intune enrollment again and verify the work profile is created successfully.
3. Install the Test DPC app from the Google Play Store, open it, and follow the setup instructions to create a sample work profile. Confirm the profile is created without errors.
4. If Test DPC succeeds, reattempt Intune enrollment and confirm the work profile is created and the device appears as compliant in the Microsoft Intune admin center under Devices > All devices.

## Rollback
1. If the work profile was removed unintentionally, restore it by re-enrolling the device with the original work account via Settings > Passwords & accounts > Work > Add account.
2. If Test DPC fails to create a work profile, restore the device to its previous state by uninstalling Test DPC and contacting the device manufacturer for work profile support.
3. If Intune enrollment still fails after removing an existing work profile, re-create the work profile manually through the device's work profile setup (if available) or factory reset the device and attempt enrollment again.
4. If OEM restrictions are suspected, revert any changes made to device settings and consult the manufacturer's documentation for work profile compatibility.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-android-enrollment>
