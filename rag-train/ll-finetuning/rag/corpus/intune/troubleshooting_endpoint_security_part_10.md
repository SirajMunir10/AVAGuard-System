# Troubleshooting: Endpoint Security

**Domain:** Intune
**Subdomain:** Endpoint Security
**Incident Type:** Troubleshooting

## Scenario / Query
How to use manage-bde to troubleshoot BitLocker encryption status when Intune reports a device as not encrypted?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** BitLocker policy configured in Intune admin center

## Symptoms
- Microsoft Intune admin center indicates a device is not encrypted

## Error Codes
N/A

## Root Causes
1. Encryption method mismatch between Intune policy and device (e.g., policy set to XTS-AES 256-bit but device encrypted with XTS-AES 128-bit)
2. Incorrect protector configuration on the device

## Remediation Steps
1. Open Command Prompt as administrator (enter 'cmd' in Search box, right-click and select Run as administrator)
2. Run 'manage-bde -status' to check encryption status
3. Compare the encryption method from manage-bde output to the encryption method in the Intune policy to ensure they match
4. Identify the specific protectors used on the device using manage-bde output to verify policy application

## Validation
1. Open Command Prompt as administrator. 2. Run 'manage-bde -status' and confirm the device shows 'Protection On' and the encryption method matches the Intune policy (e.g., XTS-AES 256-bit). 3. In Intune admin center, navigate to Devices > All devices, select the device, and verify the BitLocker encryption status now shows 'Encrypted' or 'Fully Encrypted'.

## Rollback
1. Open Command Prompt as administrator. 2. If the encryption method was changed, run 'manage-bde -protectors -delete C: -type tpm' to remove the current protector, then 'manage-bde -protectors -add C: -tpm' to re-add the default TPM protector. 3. If the device was re-encrypted, run 'manage-bde -off C:' to decrypt the drive. 4. In Intune admin center, reapply the original BitLocker policy by editing the policy assignment to include the device again.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-bitlocker-policies>
