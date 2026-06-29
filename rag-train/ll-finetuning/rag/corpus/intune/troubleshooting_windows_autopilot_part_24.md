# Troubleshooting: Windows Autopilot

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
Why is the join type for a device showing as 'Microsoft Entra registered' instead of 'Microsoft Entra joined'?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Windows Autopilot deployment

## Symptoms
- Device join type shows as 'Microsoft Entra registered' instead of 'Microsoft Entra joined'

## Error Codes
N/A

## Root Causes
1. Device was previously registered in Microsoft Entra ID before it was joined to Microsoft Entra ID
2. Device possibly registered in Microsoft Entra ID via something like a Workplace join
3. Microsoft Entra ID registered device was not deleted from Microsoft Entra ID before the device was joined to Microsoft Entra ID
4. Previous trust type is retained in the record

## Remediation Steps
1. Before registering an existing Microsoft Entra ID registered device as a Windows Autopilot device, delete the following existing device objects for the device: Microsoft Intune, Microsoft Entra ID, Windows Autopilot
2. After all device objects are deleted, re-register the device as a Windows Autopilot device
3. Re-enroll the device

## Validation
1. In Microsoft Entra admin center, go to Identity > Devices > All devices. Search for the device by name or serial number. Verify the 'Join Type' column shows 'Microsoft Entra joined' (not 'Registered').
2. In Microsoft Intune admin center, go to Devices > All devices. Confirm the device appears with enrollment status 'Success' and Autopilot profile assigned.
3. On the device, run 'dsregcmd /status' in an elevated command prompt. Confirm 'AzureAdJoined' is 'YES' and 'DomainJoined' is 'NO'.
4. Verify the device is no longer listed under 'Microsoft Entra registered' devices in the same Entra ID device list.

## Rollback
1. If the device still shows 'Microsoft Entra registered', delete the device object from Microsoft Entra ID (Identity > Devices > All devices > select device > Delete).
2. Delete the device from Microsoft Intune (Devices > All devices > select device > Delete).
3. If the device was previously registered as an Autopilot device, remove it from Windows Autopilot devices (Devices > Windows > Windows enrollment > Devices > select device > Delete).
4. Re-register the device as a Windows Autopilot device using the hardware hash or a CSV file.
5. Re-enroll the device by resetting it or re-running the out-of-box experience (OOBE).

## References
- <https://learn.microsoft.com/en-us/autopilot/troubleshoot-oobe>
- <https://learn.microsoft.com/en-us/autopilot/troubleshoot-oobe#deregister-a-device>
