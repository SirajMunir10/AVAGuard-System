# Troubleshooting: Endpoint security

**Domain:** Intune
**Subdomain:** Endpoint security
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot BitLocker policy processing issues using the MDM agent event log in Intune?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** BitLocker policies via CSP

## Symptoms
- BitLocker settings not applying to devices
- Policy processing failures

## Error Codes
N/A

## Root Causes
1. Issues processing Intune policy or applying CSP settings

## Remediation Steps
1. Collect or review the DeviceManagement-Enterprise-Diagnostics-Provider admin event log
2. Open Event Viewer: Right-click on Start Menu > Event Viewer > Applications and Service Logs > Microsoft > Windows > DeviceManagement-Enterprise-Diagnostics-Provider > Admin
3. Alternatively, access the file system location: C:\Windows\System32\winevt\Logs\Microsoft-Windows-DeviceManagement-Enterprise-Diagnostics-Provider%4Admin.evtx
4. Filter the log: Right-click the event log and select Filter Current Log > Critical/Error/Warning
5. Search through the filtered logs for BitLocker (press F3 and enter the text)
6. Look for entries following the BitLocker CSP format, such as: ./Device/Vendor/MSFT/BitLocker/RequireDeviceEncryption or ./Vendor/MSFT/BitLocker/ConfigureRecoveryPasswordRotation
7. Enable debug logging for this event log using Event Viewer for further troubleshooting

## Validation
1. Open Event Viewer as Administrator: Right-click Start > Event Viewer > Applications and Service Logs > Microsoft > Windows > DeviceManagement-Enterprise-Diagnostics-Provider > Admin. 2. Right-click the Admin log and select 'Filter Current Log'. 3. In the filter dialog, check 'Critical', 'Error', and 'Warning', then click OK. 4. Press F3 to open Find, type 'BitLocker', and click 'Find Next'. 5. Verify that no error or warning events containing 'BitLocker' or CSP paths like './Device/Vendor/MSFT/BitLocker/' appear. 6. Alternatively, open the log file at C:\Windows\System32\winevt\Logs\Microsoft-Windows-DeviceManagement-Enterprise-Diagnostics-Provider%4Admin.evtx and repeat the filter and search. 7. Confirm that BitLocker policy settings (e.g., RequireDeviceEncryption, ConfigureRecoveryPasswordRotation) are applied successfully by checking the device's BitLocker status via 'manage-bde -status' or the BitLocker Control Panel.

## Rollback
1. If validation reveals persistent errors, enable debug logging for the DeviceManagement-Enterprise-Diagnostics-Provider Admin log: In Event Viewer, right-click the Admin log > Properties > set 'Log size' to a larger value (e.g., 20480 KB) and enable 'Overwrite events as needed'. 2. Clear the current log: Right-click the Admin log > 'Clear Log' > 'Save and Clear' (optional). 3. Trigger a policy sync on the device: Go to Settings > Accounts > Access work or school > select the Intune enrollment > Info > Sync. 4. Re-collect the log after sync and re-analyze for BitLocker-related events. 5. If the issue persists, reset the BitLocker CSP policy by removing and re-assigning the BitLocker policy from Intune: In Microsoft Intune admin center, navigate to Endpoint security > Disk encryption > select the policy > Properties > unassign the affected device group, save, then re-assign and sync. 6. As a last resort, unenroll and re-enroll the device in Intune: Go to Settings > Accounts > Access work or school > select the account > Disconnect, then re-enroll via the Company Portal app.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-bitlocker-policies>
