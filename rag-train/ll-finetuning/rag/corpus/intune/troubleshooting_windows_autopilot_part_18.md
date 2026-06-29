# Troubleshooting: Windows Autopilot

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
How can I determine if a device is registered with Windows Autopilot using registry values?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Windows Autopilot deployment service

## Symptoms
- Device not receiving Autopilot profile
- Blank CloudAssignedTenantDomain or CloudAssignedTenantId values

## Error Codes
N/A

## Root Causes
1. Device not registered with Windows Autopilot
2. IsAutopilotDisabled set to 1

## Remediation Steps
1. Check registry key: HKLM\SOFTWARE\Microsoft\Provisioning\Diagnostics\Autopilot
2. Verify CloudAssignedTenantDomain is not blank; if blank, device is not registered
3. Verify CloudAssignedTenantId is not blank; if blank, device is not registered
4. Check IsAutopilotDisabled: if 1, device is not registered or profile could not be downloaded

## Validation
Open Registry Editor and navigate to HKLM\SOFTWARE\Microsoft\Provisioning\Diagnostics\Autopilot. Confirm that CloudAssignedTenantDomain and CloudAssignedTenantId are not blank (i.e., contain the expected tenant domain and tenant ID). Also confirm that IsAutopilotDisabled is either absent or set to 0. If these conditions are met, the device is registered with Windows Autopilot.

## Rollback
If the remediation fails or causes issues, re-register the device with Windows Autopilot using the official Microsoft method (e.g., via Microsoft Intune or the Autopilot deployment service). Alternatively, if the registry was manually modified, restore the original values from a backup or reimage the device to factory settings.

## References
- <https://learn.microsoft.com/en-us/autopilot/troubleshoot-oobe>
