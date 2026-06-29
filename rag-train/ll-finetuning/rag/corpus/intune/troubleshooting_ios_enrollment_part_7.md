# Troubleshooting: iOS Enrollment

**Domain:** Intune
**Subdomain:** iOS Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve the 'User Name Not Recognized' error during iOS enrollment in Intune?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** iOS enrollment with user license requirements

## Symptoms
- User Name Not Recognized error message
- Error text: 'User Name Not Recognized. This user account isn't authorized to use Microsoft Intune. Contact your system administrator if you think you have received this message in error.'

## Error Codes
N/A

## Root Causes
1. The user who is trying to enroll the device doesn't have a valid Intune license

## Remediation Steps
1. Go to the Microsoft 365 admin center
2. Choose Users > Active Users
3. Select the affected user account
4. Choose Product licenses > Edit
5. Verify that a valid Intune license is assigned to this user
6. Re-enroll the device

## Validation
1. In the Microsoft 365 admin center, navigate to Users > Active Users and select the affected user. 2. Under the Licenses and Apps tab, confirm that an Intune license (e.g., Microsoft Intune, Enterprise Mobility + Security E3/E5) is assigned and the status is 'Active'. 3. On the iOS device, go to Settings > General > VPN & Device Management, tap the management profile, and verify the enrollment status shows 'Managed' or 'Enrolled'. 4. Attempt a fresh enrollment by opening the Company Portal app and signing in with the user's credentials; confirm no 'User Name Not Recognized' error appears.

## Rollback
1. In the Microsoft 365 admin center, navigate to Users > Active Users and select the affected user. 2. Under the Product licenses tab, uncheck the Intune license and save changes to remove the license assignment. 3. On the iOS device, go to Settings > General > VPN & Device Management, tap the management profile, and select 'Remove Management' to unenroll the device. 4. Reassign the original license configuration if needed, and document the rollback for further troubleshooting.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-ios-enrollment-errors>
