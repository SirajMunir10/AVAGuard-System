# Troubleshooting: Windows Autopilot (0x801C03F3)

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve pre-provisioning error screen with HResult error code 0x801C03F3 in Windows Autopilot?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Windows Autopilot pre-provisioning deployment

## Symptoms
- Pre-provisioning gives an error screen
- Microsoft-Windows-User Device Registration/Admin event log displays HResult error code 0x801C03F3

## Error Codes
- `0x801C03F3`

## Root Causes
1. Microsoft Entra ID cannot find a Microsoft Entra device object for the device being deployed
2. The device object was manually deleted

## Remediation Steps
1. Remove the device from Microsoft Entra ID
2. Remove the device from Intune
3. Remove the device from Windows Autopilot
4. Re-register the device with Windows Autopilot to recreate the Microsoft Entra device object
5. For more information, see Deregister a device
6. To get troubleshooting logs, run the following command: Mdmdiagnosticstool.exe -area Autopilot;TPM -cab c:\autopilot.cab

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/mem/autopilot/known-issues>
