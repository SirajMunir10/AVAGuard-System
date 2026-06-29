# Implementation: Device Enrollment

**Domain:** Intune
**Subdomain:** Device Enrollment
**Incident Type:** Implementation

## Scenario / Query
A tenant administrator is enrolling Windows 10 devices into Intune using Group Policy-based automatic enrollment, but devices appear as 'Pending' in the Microsoft Intune admin center and never complete enrollment. What is the likely cause and how should it be resolved?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Azure AD Premium P1
- **Configuration:** Group Policy configured to enable automatic MDM enrollment using the 'MDM user scope' set to 'Some' or 'All'

## Symptoms
- Devices show 'Pending' status in Intune for more than 24 hours
- No errors appear in the client-side Event Viewer under Microsoft-Windows-DeviceManagement-Enterprise-Diagnostics-Provider
- Users can sign in to the device but enrollment does not complete

## Error Codes
N/A

## Root Causes
1. The DNS CNAME record for enrollment (e.g., EnterpriseEnrollment.contoso.com) is missing or incorrectly configured
2. The Azure AD MDM terms of use have not been accepted by the tenant administrator

## Remediation Steps
1. Verify that the required DNS CNAME records are created as documented in 'Set up automatic enrollment for Windows devices' (learn.microsoft.com/en-us/mem/intune/enrollment/windows-enroll) â€“ specifically EnterpriseEnrollment.<domain>.com pointing to manage.microsoft.com and EnterpriseRegistration.<domain>.com pointing to enterpriseregistration.windows.net
2. In the Microsoft Intune admin center, go to 'Device enrollment' > 'Windows enrollment' > 'Automatic enrollment' and ensure the MDM user scope is set to 'All' or 'Some' and that the Azure AD MDM terms of use have been accepted (see 'Configure automatic MDM enrollment' in the same article)

## Validation
After correcting DNS records and accepting terms of use, force a Group Policy update (gpupdate /force) on a test device and restart. The device should appear as 'Enrolled' within 15 minutes.

## Rollback
Set the MDM user scope to 'None' in the Intune automatic enrollment blade to disable automatic enrollment. Remove any incorrect DNS CNAME records.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/windows-enroll>
