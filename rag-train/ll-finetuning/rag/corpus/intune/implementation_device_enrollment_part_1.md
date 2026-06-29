# Implementation: Device Enrollment (Event ID 76: MDM enrollment failed with error 0x80180014)

**Domain:** Intune
**Subdomain:** Device Enrollment
**Incident Type:** Implementation

## Scenario / Query
A tenant administrator configured Windows 10/11 automatic enrollment via Group Policy but devices are not enrolling into Intune. What are the common root causes and remediation steps?

## Environment Context
- **Tenant Type:** Production, hybrid Azure AD joined
- **Configuration:** Group Policy setting 'Enroll automatically into MDM' configured with MDM user scope, but no MDM discovery URL or enrollment URL set.

## Symptoms
- Devices show 'Not enrolled' in Intune console
- Event ID 76 in DeviceManagement-Enterprise-Diagnostics-Provider log
- No enrollment activity in Azure AD sign-in logs

## Error Codes
- `Event ID 76: MDM enrollment failed with error 0x80180014`

## Root Causes
1. MDM discovery URL and enrollment URL not configured in Group Policy
2. User scope set to 'Basic' instead of 'Full' or 'Auto'
3. Azure AD tenant not configured for automatic MDM enrollment

## Remediation Steps
1. Ensure the Group Policy setting 'Enroll automatically into MDM' has the MDM discovery URL set to https://enrollment.manage.microsoft.com/enrollmentserver/discovery.svc
2. Set the MDM enrollment URL to https://enrollment.manage.microsoft.com/enrollmentserver/enroll.svc
3. Set the MDM user scope to 'Full' or 'Auto'
4. Verify Azure AD tenant is configured for automatic MDM enrollment: navigate to Azure AD > Mobility (MDM and MAM) > Microsoft Intune and ensure MDM user scope is set to 'All' or 'Some'
5. Restart the device or run 'dsregcmd /leave' and rejoin Azure AD to trigger enrollment

## Validation
Run 'dsregcmd /status' on the device and confirm 'AzureAdJoined' is YES and 'MdmUrl' is set to the correct Intune enrollment URL. In Intune console, verify device appears as enrolled.

## Rollback
Revert the Group Policy setting to 'Not configured' and remove the MDM discovery/enrollment URLs. Disable automatic MDM enrollment in Azure AD if no longer needed.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/windows-enroll>
