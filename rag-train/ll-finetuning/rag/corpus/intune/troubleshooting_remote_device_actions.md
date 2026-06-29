# Troubleshooting: Remote device actions

**Domain:** Intune
**Subdomain:** Remote device actions
**Incident Type:** Troubleshooting

## Scenario / Query
I clicked the 'Disable Activation Lock' action in the portal but nothing happened on the device.

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- After clicking the Disable Activation Lock action in the Intune portal, no visible change occurs on the device.

## Error Codes
N/A

## Root Causes
1. This behavior is expected. Intune requests an updated code from Apple after starting the action, but the code must be manually entered on the device.

## Remediation Steps
1. Click the Disable Activation Lock action in the Intune portal.
2. Copy the code provided by Intune (requested from Apple).
3. Issue a Wipe action on the device.
4. When the device reaches the Activation Lock screen, manually enter the copied code in the passcode field.

## Validation
1. In the Intune portal, navigate to the device and verify that the 'Disable Activation Lock' action shows a status of 'Completed' or 'Success'. 2. Confirm that the code provided by Intune (requested from Apple) was copied and saved. 3. Issue a Wipe action on the device and wait for it to reach the Activation Lock screen. 4. On the device, manually enter the copied code in the passcode field. 5. Verify that the device proceeds past the Activation Lock screen and completes the setup process.

## Rollback
1. If the code was not copied or saved, re-click the 'Disable Activation Lock' action in the Intune portal to generate a new code. 2. If the Wipe action was issued but the device does not reach the Activation Lock screen, contact Microsoft Support for further assistance. 3. If the code entered on the device is incorrect, obtain the correct code from the Intune portal (by re-running the action if necessary) and re-enter it on the device. 4. If the issue persists, refer to the official troubleshooting documentation at https://learn.microsoft.com/en-us/mem/intune/remote-actions/troubleshoot-device-actions.

## References
- <https://learn.microsoft.com/en-us/mem/intune/remote-actions/troubleshoot-device-actions>
