# Troubleshooting: Hybrid Join (0x80280036)

**Domain:** Entra ID
**Subdomain:** Hybrid Join
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve TPM_E_NOTFIPS (0x80280036/-2144862154) error during Microsoft Entra hybrid join?

## Environment Context
- **Tenant Type:** Microsoft Entra hybrid joined
- **Configuration:** TPM in FIPS mode

## Symptoms
- TPM_E_NOTFIPS (0x80280036/-2144862154) error

## Error Codes
- `0x80280036`
- `-2144862154`

## Root Causes
1. TPM in FIPS mode isn't currently supported

## Remediation Steps
1. Disable TPM on devices with this error

## Validation
1. Run 'Get-Tpm' in PowerShell as Administrator and verify that 'TpmReady' returns 'False' and 'TpmEnabled' returns 'False'.
2. Check the device's Event Viewer under 'Applications and Services Logs > Microsoft > Windows > DeviceManagement-Enterprise-Diagnostics-Provider > Admin' for no new TPM_E_NOTFIPS errors.
3. Confirm the device appears as 'Microsoft Entra hybrid joined' in the Microsoft Entra admin center under 'Identity > Devices > All devices' with a status of 'Registered' or 'Joined'.

## Rollback
1. Re-enable the TPM by running 'Enable-TpmAutoProvisioning' in PowerShell as Administrator.
2. Restart the device.
3. Verify TPM is operational by running 'Get-Tpm' and confirming 'TpmReady' returns 'True' and 'TpmEnabled' returns 'True'.
4. Re-attempt the Microsoft Entra hybrid join process using the 'dsregcmd /join' command.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
