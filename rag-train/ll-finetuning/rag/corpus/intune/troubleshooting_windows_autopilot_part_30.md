# Troubleshooting: Windows Autopilot (Another installation is in progress, please try again later)

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
Why is the error message 'Another installation is in progress, please try again later' occurring during the ESP of a Windows Autopilot deployment?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Windows Autopilot deployment with Enrollment Status Page (ESP) configured

## Symptoms
- Error message during ESP: 'Another installation is in progress, please try again later'

## Error Codes
- `Another installation is in progress, please try again later`

## Root Causes
1. Mixing of line-of-business (LOB) and Win32 applications in the same ESP deployment
2. Both LOB and Win32 applications use TrustedInstaller which doesn't allow simultaneous installations

## Remediation Steps
1. Consider using Windows Autopilot device preparation, which doesn't use ESP and supports mixing of LOB and Win32 apps

## Validation
1. Verify that the Autopilot deployment profile assigned to the affected device does not have ESP enabled. In the Intune portal, navigate to Devices > Windows > Windows enrollment > Enrollment Status Page, and confirm the profile is not assigned or is set to 'No' for 'Show app and profile configuration progress'. 2. Check that the device is targeted by a Windows Autopilot device preparation policy instead. Go to Devices > Windows > Windows enrollment > Windows Autopilot device preparation, and confirm the policy is assigned to the device's group. 3. On a test device, trigger a new Autopilot reset or re-deployment and observe the OOBE flow. Ensure the error 'Another installation is in progress, please try again later' does not appear during the ESP phase (if ESP is still used) or that the device preparation flow completes without this error.

## Rollback
1. Remove the Windows Autopilot device preparation policy assignment from the affected device group. In Intune, go to Devices > Windows > Windows enrollment > Windows Autopilot device preparation, select the policy, and under 'Assignments', remove the group. 2. Re-enable the Enrollment Status Page for the device group. Navigate to Devices > Windows > Windows enrollment > Enrollment Status Page, select the profile, and under 'Assignments', add the device group with 'Show app and profile configuration progress' set to 'Yes'. 3. If the device is already in a failed state, perform a fresh Autopilot reset by going to Devices > Windows > Windows devices, select the device, and choose 'Autopilot reset'. After the reset, the device will re-attempt OOBE with the original ESP configuration.

## References
- <https://learn.microsoft.com/en-us/autopilot/troubleshoot-oobe>
- <https://learn.microsoft.com/en-us/autopilot/troubleshoot-oobe#another-installation-is-in-progress-please-try-again-later>
