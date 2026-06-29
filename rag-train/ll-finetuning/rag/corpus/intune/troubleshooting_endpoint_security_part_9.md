# Troubleshooting: Endpoint security

**Domain:** Intune
**Subdomain:** Endpoint security
**Incident Type:** Troubleshooting

## Scenario / Query
When is UEFI not required for BitLocker silent encryption?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** BitLocker policy with TPM 1.2

## Symptoms
- Device with TPM 1.2 fails to encrypt silently

## Error Codes
N/A

## Root Causes
1. TPM 1.2 does not require UEFI for silent encryption

## Remediation Steps
1. In the Search box, enter msinfo32
2. Right-click System Information in the search results, and select Run as administrator
3. Check TPM version and BIOS mode

## Validation
1. On the affected device, open System Information (msinfo32) as administrator. 2. Verify that the TPM version is listed as 1.2. 3. Confirm that the BIOS mode is 'Legacy' or 'UEFI' (both are supported for TPM 1.2 silent encryption). 4. Run 'manage-bde -status' to check that the drive encryption status is 'Fully Encrypted' or 'Encryption in Progress' without errors. 5. In the Intune console, navigate to Devices > Monitor > Device encryption status and confirm the device shows 'Encrypted'.

## Rollback
1. If silent encryption fails after remediation, revert to the previous BitLocker policy by editing the policy in Intune to remove the 'Silent encryption' requirement. 2. On the device, run 'manage-bde -off C:' to decrypt the drive if encryption was partially applied. 3. In System Information, verify that the BIOS mode is not changed; if it was switched to UEFI, restore the original BIOS mode (e.g., Legacy) via the device's firmware settings. 4. Reboot the device and confirm BitLocker is disabled by running 'manage-bde -status' showing 'Protection Off'.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-bitlocker-policies>
