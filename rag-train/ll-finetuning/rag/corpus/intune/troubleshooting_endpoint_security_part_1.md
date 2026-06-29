# Troubleshooting: Endpoint Security

**Domain:** Intune
**Subdomain:** Endpoint Security
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot BitLocker encryption failures on Windows 10 devices managed by Intune?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** BitLocker policy configured in Intune targeting user or device groups

## Symptoms
- Device not encrypted with BitLocker as expected
- Encryption report shows no status or incomplete status for targeted devices

## Error Codes
N/A

## Root Causes
1. BitLocker policy not synced to device
2. BitLocker MDM policy Refresh scheduled task not running
3. Policy settings not replicated to FVE registry key

## Remediation Steps
1. Verify the BitLocker policy is saved to the tenant in the Intune service
2. Ensure the Windows 10 MDM client syncs with the Intune service and processes the BitLocker policy settings
3. Check that the BitLocker MDM policy Refresh scheduled task runs on the device to replicate settings to the FVE registry key
4. Use the Intune encryption report to view encryption status details for each targeted device

## Validation
Check the Intune encryption report for encryption status details of targeted devices

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-bitlocker-policies>
