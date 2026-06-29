# Troubleshooting: Windows Autopilot (80180018)

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
Why is enrollment in Microsoft Intune or a non-Microsoft MDM solution failing with an error code '80180018'?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Windows Autopilot OOBE enrollment

## Symptoms
- Something went wrong error page displayed during enrollment
- Error code 80180018 shown

## Error Codes
- `80180018`

## Root Causes
1. Incorrect or missing licenses assigned to the user
2. Too many devices enrolled for the user

## Remediation Steps
1. See Troubleshooting Windows device enrollment errors in Intune for detailed guidance

## Validation
1. Confirm the user has a valid Intune license assigned: In the Microsoft Intune admin center, go to 'Users' > select the affected user > 'Licenses' > verify an Intune or Microsoft 365 license that includes Intune is assigned. 2. Check the user's device enrollment limit: In the Microsoft Intune admin center, go to 'Devices' > 'Enroll devices' > 'Enrollment restrictions' > 'Device limit restrictions' > verify the 'Maximum number of devices a user can enroll' setting (default is 15) and confirm the user has not exceeded this limit. 3. Attempt a new enrollment on a different device with the same user credentials to see if the error persists.

## Rollback
1. If a license was incorrectly assigned or removed, reassign the correct Intune or Microsoft 365 license to the user via the Microsoft 365 admin center or Azure AD. 2. If the device enrollment limit was changed, revert the 'Maximum number of devices a user can enroll' setting to its previous value (or the default of 15) in 'Enrollment restrictions' > 'Device limit restrictions'. 3. If the user had exceeded the device limit, remove any unnecessary or duplicate device records from the Intune console under 'Devices' > 'All devices' to free up enrollment slots.

## References
- <https://learn.microsoft.com/en-us/autopilot/troubleshoot-oobe>
- <https://learn.microsoft.com/en-us/troubleshoot/windows-client/intune/troubleshoot-windows-device-enrollment-errors>
