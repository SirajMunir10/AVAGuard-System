# Troubleshooting: Endpoint security

**Domain:** Intune
**Subdomain:** Endpoint security
**Incident Type:** Troubleshooting

## Scenario / Query
How to determine if a device satisfies BitLocker prerequisites using MSINFO32?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** BitLocker policy settings

## Symptoms
- Device cannot be encrypted using an Intune BitLocker policy

## Error Codes
N/A

## Root Causes
1. Device does not meet prerequisites such as TPM and UEFI for silent encryption
2. TPM 1.2 devices do not require UEFI for silent encryption

## Remediation Steps
1. In the Search box, enter msinfo32
2. Right-click System Information in the search results, and select Run as administrator
3. Check the file system location: C:\Windows\System32\Msinfo32.exe
4. Verify prerequisites based on BitLocker policy settings and required outcome

## Validation
1. Open System Information as administrator: In the Search box, enter 'msinfo32', right-click System Information, and select 'Run as administrator'. 2. Confirm the executable path is 'C:\Windows\System32\Msinfo32.exe'. 3. Under 'System Summary', verify the following prerequisites: a. 'BIOS Mode' shows 'UEFI' (required for silent encryption with TPM 2.0; TPM 1.2 does not require UEFI). b. 'Secure Boot State' shows 'On' (if applicable per policy). c. 'TPM Manufacturer ID' and 'TPM Manufacturer Version' indicate a supported TPM (e.g., TPM 2.0 or TPM 1.2). d. 'OS Name' shows a supported Windows edition (e.g., Windows 10/11 Pro, Enterprise, or Education). 4. Cross-reference with Intune BitLocker policy settings to ensure all prerequisites are met.

## Rollback
1. If the device does not meet prerequisites, do not apply the BitLocker policy. 2. For TPM 2.0 devices without UEFI: Enable UEFI boot mode in firmware settings (disable CSM/Legacy boot). 3. For missing TPM: Enable TPM in firmware settings or install a compatible TPM module. 4. For Secure Boot disabled: Enable Secure Boot in firmware settings. 5. After changes, reboot the device and re-run msinfo32 to confirm prerequisites are met. 6. If prerequisites cannot be met, configure Intune BitLocker policy to use non-silent encryption (e.g., require user PIN or startup key).

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-bitlocker-policies>
