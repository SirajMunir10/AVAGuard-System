# Troubleshooting: Windows Autopilot

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
What is the Windows Autopilot process flow for troubleshooting device deployments?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Windows Autopilot profile, MDM enrollment configured in Microsoft Entra ID

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Establish a network connection (wireless or wired).
2. Download the Windows Autopilot profile from the Windows Autopilot deployment service.
3. Perform user authentication (user-driven deployment) or skip (self-deploying).
4. Join device to Microsoft Entra ID using user credentials (user-driven) or without (self-deploying).
5. Enroll device in MDM service (e.g., Microsoft Intune) as part of Microsoft Entra join.
6. Apply settings via enrollment status page if configured, or after user sign-in.

## Validation
1. Verify the device successfully downloads the Windows Autopilot profile by checking the event log at 'Applications and Services Logs/Microsoft/Windows/DeviceManagement-Enterprise-Diagnostics-Provider/Admin' for Event ID 100 (profile downloaded).
2. Confirm user authentication completed by reviewing the 'Microsoft-Windows-User Device Registration/Admin' log for successful registration events.
3. Validate Microsoft Entra ID join by running 'dsregcmd /status' on the device and confirming 'AzureAdJoined' is 'YES'.
4. Check MDM enrollment by running 'dsregcmd /status' and verifying 'MdmUrl' is set to the Intune enrollment URL.
5. Ensure the Enrollment Status Page (ESP) completed successfully by reviewing the 'Microsoft-Windows-DeviceManagement-Enterprise-Diagnostics-Provider/Admin' log for Event ID 200 (ESP success).

## Rollback
1. If the Autopilot profile fails to download, verify network connectivity and ensure the device is registered in the Autopilot service; re-register the device if needed.
2. If user authentication fails, reset the user's password in Microsoft Entra ID and retry the OOBE.
3. If Microsoft Entra ID join fails, remove the device from Microsoft Entra ID via the Azure portal and restart the OOBE.
4. If MDM enrollment fails, verify the MDM discovery URL is correctly configured in Microsoft Entra ID (Device settings) and that the user has an Intune license.
5. If the ESP fails, review the ESP profile configuration in Intune and ensure no conflicting policies; temporarily disable ESP and retry.

## References
- <https://learn.microsoft.com/en-us/autopilot/troubleshoot-oobe>
