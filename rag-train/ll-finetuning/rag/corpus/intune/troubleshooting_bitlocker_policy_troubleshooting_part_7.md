# Troubleshooting: BitLocker policy troubleshooting

**Domain:** Intune
**Subdomain:** BitLocker policy troubleshooting
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot BitLocker policy settings in Intune by examining registry locations?

## Environment Context
- **Tenant Type:** Intune-managed Windows devices
- **Configuration:** BitLocker policies deployed via Intune MDM

## Symptoms
- BitLocker policy settings not applying as expected
- Need to verify which BitLocker policies the client has picked up

## Error Codes
N/A

## Root Causes
1. Policy settings may not be correctly received by the MDM agent (OMADM client)

## Remediation Steps
1. Open Registry Editor by right-clicking Start > Run and entering regedit
2. Navigate to Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\current\device\BitLocker to view the policy settings picked up by Intune
3. Identify the GUID in the PolicyManager registry key
4. Navigate to Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\Providers\<GUID>\default\Device\BitLocker to troubleshoot BitLocker policy settings
5. Examine specific registry keys such as EncryptionMethodByDriveType and SystemDrivesRecoveryOptions to verify policy values

## Validation
1. Open Registry Editor (regedit) as administrator. 2. Navigate to HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\current\device\BitLocker. 3. Verify that the expected policy keys (e.g., EncryptionMethodByDriveType, SystemDrivesRecoveryOptions) exist and their values match the Intune policy configuration. 4. Note the GUID under PolicyManager\current\device\BitLocker. 5. Navigate to HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\Providers\<GUID>\default\Device\BitLocker. 6. Confirm that the same policy keys are present with the same values, indicating the policy was received and processed by the MDM agent.

## Rollback
1. If policy values are incorrect or cause issues, open Registry Editor as administrator. 2. Navigate to HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\current\device\BitLocker. 3. Delete or modify the problematic registry keys (e.g., EncryptionMethodByDriveType) to their previous or default values. 4. Navigate to HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\Providers\<GUID>\default\Device\BitLocker and apply the same changes. 5. Restart the device or run 'gpupdate /force' to reapply policies. 6. If needed, trigger a sync from Intune by going to Settings > Accounts > Access work or school > select the MDM enrollment > Info > Sync.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-bitlocker-policies>
