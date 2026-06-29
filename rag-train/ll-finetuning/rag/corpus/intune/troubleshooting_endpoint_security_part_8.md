# Troubleshooting: Endpoint security

**Domain:** Intune
**Subdomain:** Endpoint security
**Incident Type:** Troubleshooting

## Scenario / Query
What are the prerequisites for silent encryption with TPM 2.0 and how to verify them?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** BitLocker policy configured for silent encryption with TPM 2.0

## Symptoms
- Device encryption fails silently

## Error Codes
N/A

## Root Causes
1. BIOS mode is not UEFI
2. TPM 2.0 requires UEFI for silent encryption

## Remediation Steps
1. In the Search box, enter msinfo32
2. Right-click System Information in the search results, and select Run as administrator
3. Verify that BIOS mode is UEFI

## Validation
1. On a test device, open System Information (msinfo32) as administrator. 2. Confirm that 'BIOS Mode' displays 'UEFI'. 3. Run 'manage-bde -status' and verify that the drive shows 'Protection On' and 'Encryption Method' matches the configured BitLocker policy. 4. Check the Device Encryption status in Intune console: Devices > All devices > select device > Hardware > confirm TPM 2.0 is present and BIOS mode is UEFI.

## Rollback
1. If silent encryption fails due to BIOS mode not being UEFI, convert the device to UEFI using the MBR2GPT tool: run 'mbr2gpt /convert /allowfullOS' from an elevated command prompt. 2. After conversion, reboot and verify BIOS mode is UEFI via msinfo32. 3. If issues persist, disable the BitLocker policy in Intune: Endpoint security > Disk encryption > select policy > Properties > toggle 'Enable' to 'No' > Review + save. 4. Re-enable the policy after verifying prerequisites.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-bitlocker-policies>
