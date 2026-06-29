# Troubleshooting: Windows Autopilot

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
Why are blocking apps specified in a user-targeted Enrollment Status Profile ignored during device ESP?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** User-targeted Enrollment Status Profile

## Symptoms
- Blocking apps specified in a user-targeted Enrollment Status Profile are ignored during device ESP

## Error Codes
N/A

## Root Causes
1. The services responsible for determining the list of apps that should be blocking during device ESP aren't able to determine the correct ESP profile containing the list of apps because they don't know the user identity

## Remediation Steps
1. Enable the default ESP profile (which targets all users and devices) and place the blocking app list there
2. Target the ESP profile to device groups

## Validation
1. Verify that a default Enrollment Status Profile (targeting 'All users' and 'All devices') exists and is enabled in the Microsoft Intune admin center under Devices > Enrollment > Windows enrollment > Enrollment Status Page. 2. Confirm that the blocking app list is configured in that default profile (not in a user-targeted profile). 3. On a test device, perform a fresh Windows Autopilot deployment and observe the ESP. Ensure that the specified blocking apps now appear and block progress until installed. 4. Check the ESP logs on the device (C:\ProgramData\Microsoft\Windows\Autopilot\ETW\* or via the Event Viewer under Applications and Services Logs > Microsoft > Windows > Autopilot) for any errors related to app blocking.

## Rollback
1. In the Microsoft Intune admin center, navigate to Devices > Enrollment > Windows enrollment > Enrollment Status Page. 2. Remove the blocking app list from the default ESP profile (or disable the default profile if it was not previously enabled). 3. Re-enable the original user-targeted ESP profile (if it was disabled) and restore its blocking app list. 4. If the issue persists, consider targeting the ESP profile to a device group instead of a user group, as documented in the known issues article.

## References
- <https://learn.microsoft.com/en-us/mem/autopilot/known-issues>
