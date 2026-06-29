# Implementation: Device Enrollment (Event ID 76)

**Domain:** Intune
**Subdomain:** Device Enrollment
**Incident Type:** Implementation

## Scenario / Query
After configuring Windows 10/11 automatic enrollment via Group Policy, devices appear as 'Pending' in Microsoft Intune and never complete enrollment. What is the likely cause and how do I resolve it?

## Environment Context
- **Tenant Type:** Production, hybrid Azure AD joined
- **Configuration:** Group Policy configured with MDM discovery URL https://enrollment.manage.microsoft.com/enrollmentserver/discovery.svc and MDM enrollment URL https://enrollment.manage.microsoft.com/enrollmentserver/enroll.svc

## Symptoms
- Devices show 'Pending' status in Intune for more than 24 hours
- Event Viewer shows Event ID 76 or 77 in Microsoft-Windows-DeviceManagement-Enterprise-Diagnostics-Provider/Admin
- No error message displayed to the user during enrollment attempt

## Error Codes
- `Event ID 76`
- `Event ID 77`

## Root Causes
1. The Group Policy setting 'Enable automatic MDM enrollment using default Azure AD credentials' is not configured or is set to 'Not Configured'
2. The user does not have an Intune license assigned
3. The device is not Azure AD joined or hybrid Azure AD joined

## Remediation Steps
1. Ensure the Group Policy setting 'Enable automatic MDM enrollment using default Azure AD credentials' is set to 'Enabled' under Computer Configuration > Administrative Templates > Windows Components > MDM
2. Verify that the user signing in has a valid Intune license (e.g., Microsoft 365 E3, Enterprise Mobility + Security E3, or standalone Intune license)
3. Confirm the device is hybrid Azure AD joined by running 'dsregcmd /status' and checking AzureAdJoined and DomainJoined statuses
4. If the device is not hybrid joined, configure Azure AD Connect to sync the device and enable hybrid Azure AD join

## Validation
On a test device, apply the corrected Group Policy, wait for policy refresh (gpupdate /force), sign out and sign back in, then verify in Intune console that the device status changes from 'Pending' to 'Enrolled' within 15 minutes.

## Rollback
Set the 'Enable automatic MDM enrollment using default Azure AD credentials' Group Policy to 'Not Configured' or 'Disabled', then remove the device from Intune by deleting its record in the Intune console.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/windows-enroll>
- <https://learn.microsoft.com/en-us/troubleshoot/mem/intune/troubleshoot-windows-enrollment-errors>
