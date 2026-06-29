# Troubleshooting: Enrollment

**Domain:** Intune
**Subdomain:** Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve the 'Invalid Profile' error when an iPhone/iPad cannot download the configuration profile during enrollment?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Device type restrictions

## Symptoms
- The configuration for your iPhone/iPad couldn't be downloaded from <Company Name>: Invalid Profile

## Error Codes
N/A

## Root Causes
1. The enrollment is blocked by a device type restriction

## Remediation Steps
1. Sign in to the Microsoft Intune admin center
2. Navigate to Devices > Enroll devices > Enrollment restrictions
3. Under Device type restrictions, select All Users > Properties
4. Select Edit next to the Platform settings
5. On the Edit restriction page, select Allow for iOS/iPadOS
6. Proceed to the Review + save page, then select Save

## Validation
1. Sign in to the Microsoft Intune admin center. 2. Navigate to Devices > Enroll devices > Enrollment restrictions. 3. Under Device type restrictions, select All Users > Properties. 4. Confirm that the Platform settings for iOS/iPadOS are set to 'Allow'. 5. On an iPhone/iPad, attempt to download the configuration profile again and verify that the 'Invalid Profile' error no longer appears.

## Rollback
1. Sign in to the Microsoft Intune admin center. 2. Navigate to Devices > Enroll devices > Enrollment restrictions. 3. Under Device type restrictions, select All Users > Properties. 4. Select Edit next to the Platform settings. 5. On the Edit restriction page, change the iOS/iPadOS setting back to 'Block'. 6. Proceed to the Review + save page, then select Save.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-ios-enrollment-errors>
