# Troubleshooting: Windows Enrollment (80070774)

**Domain:** Intune
**Subdomain:** Windows Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error 0x80070774 during Hybrid Microsoft Entra Autopilot enrollment when the device times out at the initial sign-in screen?

## Environment Context
- **Tenant Type:** Hybrid Microsoft Entra
- **Configuration:** Autopilot profile with Assign user feature enabled in Hybrid Microsoft Entra join scenario

## Symptoms
- Device times out during initial sign-in screen in Hybrid Microsoft Entra Autopilot scenario
- Error message: Something went wrong. Error Code 80070774
- Error 0x80070774: Something went wrong. Confirm you are using the correct sign-in information and that your organization uses this feature

## Error Codes
- `80070774`
- `0x80070774`

## Root Causes
1. Domain controller cannot be found or successfully reached because of connectivity issues
2. Device has entered a state that cannot join the domain
3. Microsoft Entra hybrid join is used with Assign user feature configured in Autopilot profile, which performs a Microsoft Entra join during initial sign-in screen, preventing on-premises domain join
4. Autopilot object's associated AzureAD device has been deleted

## Remediation Steps
1. In the Microsoft Intune admin center, choose > Devices > Windows > Windows devices. Select the device experiencing the issue, click the ellipsis (…) on the rightmost side, select Unassign user, and wait for the process to finish. Verify that the Hybrid Microsoft Entra Autopilot profile is assigned before reattempting OOBE.
2. If the issue persists, on the server that hosts the Offline Domain Join Intune Connector, check Event ID 30132 in the ODJ Connector Service log. Event 30132 indicates the ODJ connector does not have sufficient privileges to complete the operation.
3. Delete the Autopilot object and reimport the hash to generate a new one if the Autopilot object's associated AzureAD device has been deleted.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-windows-enrollment-errors>
