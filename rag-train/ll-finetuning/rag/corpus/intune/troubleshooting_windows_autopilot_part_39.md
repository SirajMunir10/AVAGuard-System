# Troubleshooting: Windows Autopilot (0x80070490)

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
TPM attestation fails on AMD platforms with ASP fTPM with error code 0x80070490

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** AMD platforms with ASP firmware TPM

## Symptoms
- TPM attestation fails

## Error Codes
- `0x80070490`

## Root Causes
1. AMD platforms with ASP firmware TPM have a known issue with TPM attestation on Windows systems

## Remediation Steps
1. Consult with device manufacturers and firmware release notes for which firmware versions contain the update that resolves this issue

## Validation
1. On an affected AMD platform with ASP fTPM, run 'Get-TpmEndorsementKeyInfo -HashAlgorithm sha256' in PowerShell as Administrator and verify it completes without error 0x80070490.
2. Check the TPM attestation status by running 'Get-AutopilotDiagnostics' (from the Windows Autopilot diagnostics module) and confirm the TPM attestation field shows 'Success'.
3. Review the System event log for Event ID 33 from source 'Microsoft-Windows-TPM-WMI' and confirm no error 0x80070490 is logged.
4. In the Microsoft Intune admin center, navigate to Devices > Enroll devices > Windows enrollment > Autopilot deployment profiles, select the profile assigned to the device, and verify the device's Autopilot status shows 'TPM attestation: Passed'.

## Rollback
1. If the firmware update causes boot issues, boot into UEFI/BIOS and restore the previous firmware version using the manufacturer's recovery procedure (e.g., using a USB recovery key or built-in backup).
2. If TPM attestation fails after the update, revert to the previous firmware version by flashing the earlier BIOS/firmware image obtained from the device manufacturer's support site.
3. After reverting firmware, run 'Clear-Tpm' in PowerShell as Administrator to reset the TPM, then re-initialize it with 'Initialize-Tpm'.
4. Re-enroll the device in Windows Autopilot by deleting its Autopilot device record from the Intune admin center (Devices > Enroll devices > Windows enrollment > Devices) and re-importing the hardware hash.

## References
- <https://learn.microsoft.com/en-us/mem/autopilot/known-issues>
