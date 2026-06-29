# Troubleshooting: Windows Autopilot

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
Windows Autopilot self-deploying mode fails with an error code indicating a timeout. What are the common causes and how to resolve?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Windows Autopilot self-deploying mode

## Symptoms
- Windows Autopilot self-deploying mode fails with an error code
- Timeout error

## Error Codes
N/A

## Root Causes
1. Device isn't TPM 2.0 capable (e.g., virtual machine)
2. TPM attestation failed
3. Multiple MDM configurations in Microsoft Entra ID causing failure to join Microsoft Entra ID with a device token

## Remediation Steps
1. Ensure the device is TPM 2.0 capable
2. Verify TPM attestation succeeds
3. Ensure only one MDM configuration exists in Microsoft Entra ID

## Validation
1. Confirm the device has a TPM 2.0 chip: Run 'Get-Tpm' in PowerShell and verify 'TpmReady' is True and 'SpecVersion' is 2.0. 2. Verify TPM attestation: On the device, run 'Get-WindowsAutoPilotInfo -Online' and check for successful attestation logs in Event Viewer under 'Applications and Services Logs/Microsoft/Windows/DeviceManagement-Enterprise-Diagnostics-Provider/Admin'. 3. Check MDM configuration count in Microsoft Entra ID: Navigate to 'Microsoft Entra admin center > Mobility (MDM and MAM) > Microsoft Intune' and ensure only one MDM configuration is present.

## Rollback
1. If TPM attestation fails, disable and re-enable TPM in BIOS, then run 'Initialize-Tpm' in PowerShell. 2. If multiple MDM configurations exist, remove the duplicate by deleting the extra configuration in 'Microsoft Entra admin center > Mobility (MDM and MAM) > Microsoft Intune', keeping only the one linked to Intune. 3. If the device is not TPM 2.0 capable, replace the device with a TPM 2.0-capable one or use a different Autopilot deployment profile (e.g., user-driven mode) as a workaround.

## References
- <https://learn.microsoft.com/en-us/mem/autopilot/known-issues>
