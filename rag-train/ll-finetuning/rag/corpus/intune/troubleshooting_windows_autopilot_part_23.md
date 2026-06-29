# Troubleshooting: Windows Autopilot

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
Why is the Windows Autopilot profile not applied after a hardware change occurred on a device?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** Windows Autopilot profile

## Symptoms
- Windows Autopilot profile is not applied after a hardware change
- Fix pending or Attention required message displayed in Windows Autopilot devices page
- When selecting the Fix pending link, message: We've detected a hardware change on this device. We're trying to automatically register the new hardware. You don't need to do anything now; the status will be updated at the next check in with the result.

## Error Codes
N/A

## Root Causes
1. A hardware change occurs on a device
2. The device is reimaged to a Windows version before Windows 11, version 21H2 with KB5017383 or Windows 10, versions 22H2

## Remediation Steps
1. Deregister the device
2. Re-register the device

## Validation
1. In the Microsoft Intune admin center, navigate to Devices > Windows > Windows enrollment > Windows Autopilot deployment program > Devices. 2. Search for the device by its serial number or name. 3. Confirm the device is no longer listed in the Windows Autopilot devices blade (deregistration succeeded). 4. Re-register the device by importing its hardware hash using the Windows Autopilot deployment program. 5. Verify the device reappears in the Windows Autopilot devices blade with a status of 'Not assigned' or 'Assigned' (depending on profile assignment). 6. Confirm the correct Windows Autopilot profile is assigned to the device. 7. On the device, run 'Get-WindowsAutopilotInfo -Online' in an elevated PowerShell session to verify the device is recognized and the profile is applied.

## Rollback
1. If deregistration was performed but re-registration fails, re-import the device using its original hardware hash (obtained before the hardware change) via the Windows Autopilot deployment program in Intune. 2. If the device is still in a 'Fix pending' state after re-registration, wait for the next device check-in (up to 24 hours) or manually sync the device from Intune by selecting the device and clicking 'Sync'. 3. If the issue persists, contact Microsoft Support for further assistance, referencing the hardware change scenario.

## References
- <https://learn.microsoft.com/en-us/autopilot/troubleshoot-oobe>
- <https://learn.microsoft.com/en-us/autopilot/deregister-device>
- <https://learn.microsoft.com/en-us/autopilot/motherboard-replacement>
