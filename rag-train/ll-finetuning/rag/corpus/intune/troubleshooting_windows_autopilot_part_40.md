# Troubleshooting: Windows Autopilot (0x81039001)

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot TPM attestation failure with error code 0x81039001 during Windows Autopilot pre-provisioning technician flow or self-deployment mode?

## Environment Context
- **Tenant Type:** Any
- **Configuration:** Windows Autopilot devices deployed using self-deploying mode or pre-provisioning mode

## Symptoms
- TPM attestation failure during the 'Securing your hardware' step
- Error code 0x81039001
- Error message: E_AUTOPILOT_CLIENT_TPM_MAX_ATTESTATION_RETRY_EXCEEDED

## Error Codes
- `0x81039001`
- `E_AUTOPILOT_CLIENT_TPM_MAX_ATTESTATION_RETRY_EXCEEDED`

## Root Causes
1. Intermittent TPM attestation failure on some devices

## Remediation Steps
1. Subsequent attempts to provision might resolve the issue

## Validation
1. On the affected device, restart the Windows Autopilot pre-provisioning technician flow or self-deployment mode from the beginning. 2. Observe the 'Securing your hardware' step and confirm that TPM attestation completes without error code 0x81039001. 3. Verify that the device proceeds to the next provisioning phase (e.g., device setup or enrollment). 4. Check the Event Viewer under Applications and Services Logs > Microsoft > Windows > Autopilot for successful attestation events (Event ID 100 or similar). 5. Confirm that the device appears as 'Assigned' or 'Provisioned' in the Microsoft Intune admin center under Devices > Windows > Windows enrollment > Autopilot devices.

## Rollback
1. If the remediation fails, reset the device to a clean state using the Windows recovery options (e.g., 'Reset this PC' or reinstall Windows). 2. Re-register the device in Windows Autopilot by obtaining the hardware hash and uploading it to the Intune admin center. 3. Retry the pre-provisioning technician flow or self-deployment mode. 4. If the issue persists, contact Microsoft Support with the TPM attestation logs (collected via 'Get-Tpm' PowerShell cmdlet and the Autopilot diagnostics tool).

## References
- <https://learn.microsoft.com/en-us/mem/autopilot/known-issues>
