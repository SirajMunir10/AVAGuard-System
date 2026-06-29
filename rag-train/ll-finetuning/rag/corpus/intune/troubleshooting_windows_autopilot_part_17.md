# Troubleshooting: Windows Autopilot

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
Where are Windows Autopilot profile settings stored on a device during OOBE, and how can I verify them?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Windows Autopilot deployment service

## Symptoms
- User receives an error during Autopilot OOBE
- Device not registering with Windows Autopilot
- Profile settings not applied

## Error Codes
N/A

## Root Causes
1. AadTenantId registry entry does not match the tenant used to register the device
2. Device not registered with Windows Autopilot (IsAutopilotDisabled = 1)
3. Network connectivity or firewall issues preventing profile download
4. Network timeouts preventing profile download
5. TenantMatched registry value is 0 (user's tenant ID does not match device's registered tenant ID)

## Remediation Steps
1. Navigate to registry key: HKLM\SOFTWARE\Microsoft\Provisioning\Diagnostics\Autopilot
2. Check AadTenantId value to ensure it matches the Microsoft Entra tenant GUID the user signed into
3. Check CloudAssignedTenantDomain value to confirm the device is registered with the correct tenant (e.g., contosomn.onmicrosoft.com)
4. Check CloudAssignedTenantId value to confirm the GUID matches the tenant domain
5. Check IsAutopilotDisabled value: if set to 1, verify device registration and network connectivity
6. Check TenantMatched value: if 0, user must start over with correct tenant

## Validation
1. Open Registry Editor as Administrator. 2. Navigate to HKLM\SOFTWARE\Microsoft\Provisioning\Diagnostics\Autopilot. 3. Verify that AadTenantId matches the Microsoft Entra tenant GUID used during sign-in. 4. Verify CloudAssignedTenantDomain matches the expected tenant domain (e.g., contosomn.onmicrosoft.com). 5. Verify CloudAssignedTenantId matches the tenant GUID. 6. Confirm IsAutopilotDisabled is 0. 7. Confirm TenantMatched is 1.

## Rollback
1. If any registry value is incorrect, correct it to the expected value. 2. If the device is not registered (IsAutopilotDisabled=1), re-register the device using Get-WindowsAutoPilotInfo or the Microsoft Intune portal. 3. If TenantMatched=0, ensure the user signs in with the correct tenant account. 4. If network issues persist, verify firewall rules allow access to https://login.live.com, https://login.microsoftonline.com, and https://autopilot.microsoft.com. 5. Restart the device and retry Autopilot OOBE.

## References
- <https://learn.microsoft.com/en-us/autopilot/troubleshoot-oobe>
