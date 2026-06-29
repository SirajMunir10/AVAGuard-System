# Troubleshooting: BitLocker policy (0x0)

**Domain:** Intune
**Subdomain:** BitLocker policy
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot when BitLocker encryption does not initiate after Intune policy is received?

## Environment Context
- **Tenant Type:** Intune-managed Windows devices
- **Configuration:** BitLocker MDM policy refresh scheduled task

## Symptoms
- BitLocker policy appears in DeviceManagement-Enterprise-Diagnostics-Provider admin event log, MDM diagnostics, and registry
- No errors indicating policy was picked up successfully from Intune
- Nothing logged in BitLocker-API event log to show encryption was attempted

## Error Codes
- `0x0`
- `0x41303`

## Root Causes
1. BitLocker MDM policy Refresh scheduled task may not have run or encountered errors

## Remediation Steps
1. Enable the Task Scheduler operational event log manually: right-click on Start Menu > Event Viewer > Applications and Services > Microsoft > Windows > TaskScheduler > Operational
2. Enter 'task scheduler' in Windows search box, select Task Scheduler > Microsoft > Windows > BitLocker
3. Right-click on 'BitLocker MDM policy Refresh' and choose Run
4. Inspect the Last Run Result column for error codes and examine the task schedule event log for errors

## Validation
Check Last Run Result column for 0x0 (success) or other error codes; examine task schedule event log for errors

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-bitlocker-policies>
