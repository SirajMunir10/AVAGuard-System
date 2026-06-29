# Implementation: Device Enrollment

**Domain:** Intune
**Subdomain:** Device Enrollment
**Incident Type:** Implementation

## Scenario / Query
An organization is deploying Windows Autopilot with Intune. After uploading the device hardware hashes, the devices appear in Intune but are not automatically enrolling. What configuration steps are missing?

## Environment Context
- **Tenant Type:** Production
- **Configuration:** Windows Autopilot deployment profile assigned to a dynamic device group containing the uploaded devices; Enrollment Status Page (ESP) configured

## Symptoms
- Devices are listed in Intune under Devices > Windows enrollment > Devices
- Devices do not start the Autopilot provisioning process during OOBE
- No Autopilot profile appears as assigned when checking device details

## Error Codes
N/A

## Root Causes
1. The Windows Autopilot deployment profile is not assigned to the correct Azure AD group containing the devices
2. The user performing the enrollment does not have an Intune license assigned
3. The enrollment restrictions block Windows Autopilot enrollment

## Remediation Steps
1. Verify that the Autopilot deployment profile is assigned to an Azure AD group that includes the uploaded devices. In the Microsoft Intune admin center, go to Devices > Windows > Windows enrollment > Deployment profiles, select the profile, and check the 'Assignments' tab.
2. Ensure the enrolling user has an appropriate Intune license (e.g., Microsoft Intune, Microsoft 365 E3/E5).
3. Check enrollment restrictions: Devices > Windows > Windows enrollment > Enrollment restrictions. Ensure the default restriction does not block Windows Autopilot enrollment.
4. If using a user-driven Autopilot scenario, confirm that the user is a member of the Azure AD group assigned to the profile.

## Validation
After applying the above steps, perform a fresh OOBE on a test device. The device should display the organization-specific Autopilot branding and automatically enroll into Intune.

## Rollback
Remove the Autopilot deployment profile assignment from the Azure AD group. The devices will then fall back to standard OOBE without Autopilot.

## References
- <https://learn.microsoft.com/en-us/mem/autopilot/existing-devices>
- <https://learn.microsoft.com/en-us/mem/autopilot/enrollment-autopilot>
