# Troubleshooting: Endpoint security

**Domain:** Intune
**Subdomain:** Endpoint security
**Incident Type:** Troubleshooting

## Scenario / Query
How to use MSINFO32 to verify BitLocker prerequisites for silent encryption on a device?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** BitLocker policy configured for silent encryption

## Symptoms
- Device fails to encrypt silently via Intune BitLocker policy

## Error Codes
N/A

## Root Causes
1. BIOS mode is not UEFI when TPM 2.0 is used
2. Device does not meet prerequisites such as TPM and UEFI for silent encryption

## Remediation Steps
1. In the Search box, enter msinfo32
2. Right-click System Information in the search results, and select Run as administrator
3. Verify that BIOS mode is UEFI if the device uses TPM 2.0 and silent encryption is configured

## Validation
1. Open System Information as administrator: In the Search box, enter 'msinfo32', right-click System Information, and select 'Run as administrator'. 2. In the System Summary, locate the 'BIOS Mode' entry. Confirm it displays 'UEFI'. 3. Verify that 'Secure Boot State' is 'On' and 'TPM Manufacturer Information' shows a TPM (e.g., 'AMD fTPM' or 'Intel PTT') with specification version 2.0. 4. If all conditions are met, the device meets prerequisites for silent encryption.

## Rollback
1. If BIOS mode is not UEFI, convert the device to UEFI using the manufacturer's conversion tool (e.g., MBR2GPT.exe) and enable Secure Boot. 2. If TPM is not present or not version 2.0, enable TPM in the BIOS/UEFI firmware settings or upgrade the hardware. 3. After changes, reboot the device and re-run msinfo32 to confirm prerequisites are met. 4. If the device still fails to encrypt silently, review Intune BitLocker policy settings and ensure the policy is assigned and targeted correctly.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-bitlocker-policies>
