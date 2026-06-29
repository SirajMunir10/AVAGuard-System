# Troubleshooting: Endpoint Security

**Domain:** Intune
**Subdomain:** Endpoint Security
**Incident Type:** Troubleshooting

## Scenario / Query
How to verify BitLocker policy settings by comparing registry keys with policy configuration in Intune?

## Environment Context
- **Tenant Type:** Intune-managed Windows devices
- **Configuration:** BitLocker policies deployed via Intune

## Symptoms
- BitLocker encryption not applying as expected
- Policy settings in UI do not match device behavior

## Error Codes
N/A

## Root Causes
1. Misconfiguration or mismatch between policy provider registry key and main BitLocker registry key

## Remediation Steps
1. Navigate to registry key location: Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\FVE
2. Compare the settings in the FVE registry key with the policy settings in the Intune UI, MDM log, MDM diagnostics, and the policy registry key
3. Use the BitLocker CSP documentation to decode all setting names in the registry
4. Verify specific values: EncryptionMethodWithXtsOs, EncryptionMethodWithXtsFdv, EncryptionMethodWithXtsRdv (possible values: 3 = AES-CBC 128, 4 = AES-CBC 256, 6 = XTS-AES 128, 7 = XTS-AES 256)
5. Check UseTPM, UseTPMKey, UseTPMKeyPIN, UseTPMPIN are set to 2 (allow)
6. Confirm OSActiveDirectoryBackup has a value of 1 (enabled)
7. Confirm OSHideRecoveryPage is equal to 0 (not enabled)

## Validation
Ensure settings in FVE registry key match policy settings in Intune UI and MDM logs

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-bitlocker-policies>
