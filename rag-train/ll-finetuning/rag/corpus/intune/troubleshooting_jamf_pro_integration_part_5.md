# Troubleshooting: Jamf Pro integration

**Domain:** Intune
**Subdomain:** Jamf Pro integration
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve Jamf enrollment failure when a device was previously enrolled in Intune and shows multiple instances in the portal?

## Environment Context
- **Tenant Type:** Microsoft Intune with Jamf Pro integration
- **Configuration:** Device previously enrolled in Intune, then unenrolled from Jamf but not correctly removed from Intune

## Symptoms
- Multiple instances of the same device in the portal
- Jamf enrollment fails

## Error Codes
N/A

## Root Causes
1. Device was previously enrolled in Intune and not correctly removed from Intune after unenrollment from Jamf
2. User made several registration attempts

## Remediation Steps
1. On the Mac, start Terminal.
2. Run sudo JAMF removemdmprofile.
3. Run sudo JAMF removeFramework.
4. On the JAMF Pro server, delete the computer's inventory record.
5. Delete the device from AzureAD.

## Validation
1. On the Mac, run 'sudo profiles -P' to verify no MDM profile remains. 2. Run 'sudo jamf policy' to confirm the Jamf framework is removed (should return 'No policies found'). 3. In the Intune portal, navigate to Devices > All devices and confirm the device no longer appears. 4. In Azure AD, go to Devices > All devices and confirm the device is deleted. 5. In Jamf Pro, verify the computer's inventory record is removed.

## Rollback
1. If the MDM profile was removed accidentally, re-enroll the device in Intune by running 'sudo profiles -e' or using the Company Portal app. 2. If the Jamf framework was removed incorrectly, reinstall it by running 'sudo jamf policy' or re-enrolling the device in Jamf Pro. 3. If the device was deleted from Azure AD or Intune prematurely, re-register the device by signing in with a work or school account and following the enrollment prompts. 4. If the Jamf Pro inventory record was deleted, re-add the device by running 'sudo jamf recon' on the Mac.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-jamf>
