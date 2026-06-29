# Troubleshooting: Windows Autopilot

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
How can additional detailed troubleshooting information be enabled for Windows Autopilot provisioning?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Windows 11, Autopilot user-driven mode, Work or School account

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Go to the ESP profile where the Windows Autopilot diagnostics page needs to be enabled.
2. Make sure that Show app and profile configuration progress is selected to Yes.
3. Make sure that Turn on log collection and diagnostics page for end users is selected to Yes.
4. To access any diagnostic information once the diagnostic page is enabled, select the View Diagnostics button or enter the keystroke CTRL + SHIFT + D.
5. For diagnostics to be able to upload successfully from the client, make sure that the URL lgmsapeweu.blob.core.windows.net isn't blocked on the network.

## Validation
1. In the Microsoft Intune admin center, navigate to Devices > Windows > Enrollment > Enrollment Status Page. Select the ESP profile assigned to the target devices. Verify that 'Show app and profile configuration progress' is set to 'Yes' and 'Turn on log collection and diagnostics page for end users' is set to 'Yes'. 2. On a Windows 11 device undergoing Autopilot user-driven mode, during the Enrollment Status Page (ESP) phase, press CTRL + SHIFT + D to open the diagnostics page. Confirm that the diagnostics page appears and displays provisioning logs. 3. From the diagnostics page, attempt to upload logs by selecting 'View Diagnostics' and then 'Upload logs'. Verify that the upload completes without error. 4. From a network perspective, confirm that the URL lgmsapeweu.blob.core.windows.net is reachable from the client device (e.g., using Test-NetConnection or curl).

## Rollback
1. In the Microsoft Intune admin center, navigate to Devices > Windows > Enrollment > Enrollment Status Page. Select the ESP profile. Set 'Show app and profile configuration progress' to 'No' and 'Turn on log collection and diagnostics page for end users' to 'No'. 2. If the diagnostics page was enabled and caused unexpected behavior (e.g., users accessing sensitive logs), instruct users to avoid pressing CTRL + SHIFT + D during provisioning. 3. If log uploads to lgmsapeweu.blob.core.windows.net caused network issues, add a firewall rule to block that URL. 4. Reboot the device and re-initiate Autopilot to ensure the previous ESP profile (without diagnostics) is applied.

## References
- <https://learn.microsoft.com/en-us/autopilot/troubleshoot-oobe>
