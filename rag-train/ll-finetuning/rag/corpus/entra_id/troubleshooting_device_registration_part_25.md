# Troubleshooting: Device Registration (0x801c03f2)

**Domain:** Entra ID
**Subdomain:** Device Registration
**Incident Type:** Troubleshooting

## Scenario / Query
How to find the phase and error code when a Microsoft Entra hybrid join fails on Windows 10 version 1803 or later?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Windows 10 version 1803 or later, domain-joined device unable to Microsoft Entra hybrid join

## Symptoms
- Device is domain-joined but unable to Microsoft Entra hybrid join
- Previous Registration subsection appears in Diagnostic Data section of join status output

## Error Codes
- `0x801c03f2`
- `DirectoryError`

## Root Causes
1. The device object by the given id (e92325d0-xxxx-xxxx-xxxx-94ae875d5245) isn't found.

## Remediation Steps
N/A

## Validation
1. Run 'dsregcmd /status' on the affected Windows 10 device (version 1803 or later).
2. In the output, locate the 'Device Registration State' section and verify that 'AzureAdJoined' is set to 'YES'.
3. Check the 'Diagnostic Data' section; confirm that the 'Previous Registration' subsection no longer appears.
4. Ensure no error codes such as 0x801c03f2 or 'DirectoryError' are present in the output.
5. Confirm that the device object ID (e.g., e92325d0-xxxx-xxxx-xxxx-94ae875d5245) is now found in Microsoft Entra ID by running 'Get-MgDevice -Filter "deviceId eq 'e92325d0-xxxx-xxxx-xxxx-94ae875d5245'"' in Microsoft Graph PowerShell.

## Rollback
1. If the remediation fails or causes issues, re-run 'dsregcmd /leave' on the device to remove the device from Microsoft Entra ID.
2. Delete the device object from Microsoft Entra ID using 'Remove-MgDevice -DeviceId "e92325d0-xxxx-xxxx-xxxx-94ae875d5245"' in Microsoft Graph PowerShell.
3. Rejoin the device to the on-premises Active Directory domain if it was removed.
4. Restart the device and verify the original state by running 'dsregcmd /status' to confirm the device is domain-joined but not Microsoft Entra hybrid joined, with the 'Previous Registration' subsection present and error codes 0x801c03f2 or 'DirectoryError'.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
