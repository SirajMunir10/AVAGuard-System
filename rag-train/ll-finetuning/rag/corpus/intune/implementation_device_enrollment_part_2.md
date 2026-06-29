# Implementation: Device Enrollment (8018000b)

**Domain:** Intune
**Subdomain:** Device Enrollment
**Incident Type:** Implementation

## Scenario / Query
A tenant has enabled automatic enrollment for Windows 10/11 devices via Group Policy, but newly joined devices fail to enroll in Intune and show error 8018000b in the Event Viewer. What is the root cause and how do you resolve it?

## Environment Context
- **Tenant Type:** Hybrid Azure AD joined with on-premises AD
- **Configuration:** Group Policy configured for MDM enrollment with https://enrollment.manage.microsoft.com

## Symptoms
- Devices appear in Azure AD but not in Intune
- Event ID 76 in Event Viewer under Microsoft-Windows-DeviceManagement-Enterprise-Diagnostics-Provider/Admin
- Error code 8018000b displayed during enrollment

## Error Codes
- `8018000b`

## Root Causes
1. The user does not have an Intune license assigned
2. The device is not within the allowed enrollment scope (e.g., device type restrictions or enrollment device platform restrictions)
3. The MDM authority is not set to Intune

## Remediation Steps
1. Verify that the MDM authority is set to Intune in the Microsoft Intune admin center (Tenant administration > MDM authority)
2. Assign a valid Intune license (e.g., Microsoft 365 E3 or Enterprise Mobility + Security E3) to the user enrolling the device
3. Check enrollment restrictions: Devices > Enroll devices > Enrollment restrictions > Device platform restrictions â€“ ensure Windows is allowed
4. Ensure the user is in scope of the MDM user scope in Azure AD > Mobility (MDM and MAM) > Microsoft Intune

## Validation
After remediation, trigger a manual enrollment sync on the device by running 'dsregcmd /join' and then 'Start-Process ms-settings:workplace' to verify successful enrollment. Confirm the device appears in Intune > Devices.

## Rollback
If the issue persists, temporarily disable device platform restrictions for Windows to isolate the cause, then re-enable after testing.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-windows-enrollment-errors>
