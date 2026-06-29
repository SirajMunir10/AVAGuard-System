# Incident Response: Device Compliance

**Domain:** Intune
**Subdomain:** Device Compliance
**Incident Type:** Incident Response

## Scenario / Query
An Intune-managed Windows 10 device is reporting as non-compliant even though all configured compliance policies appear to be met. The device shows a compliance status of 'Not evaluated' and the last check-in was over 24 hours ago. How do you investigate and resolve this incident?

## Environment Context
- **Tenant Type:** Microsoft Intune standalone (Azure AD joined)
- **Configuration:** Windows 10 compliance policy requiring BitLocker, antivirus (Microsoft Defender), and minimum OS build. Device is Azure AD joined and enrolled via automatic enrollment.

## Symptoms
- Device compliance status shows 'Not evaluated' in Intune console
- Last check-in timestamp is more than 24 hours old
- User reports device is healthy but cannot access company resources because Conditional Access blocks non-compliant devices
- No recent errors in the device's Event Viewer under Microsoft-Windows-DeviceManagement-Enterprise-Diagnostics-Provider

## Error Codes
N/A

## Root Causes
1. Device has not successfully checked in with Intune service due to network connectivity issues or firewall blocking required endpoints
2. The Intune management extension or the enrollment certificate has expired or is corrupted
3. The device's time is out of sync with the Intune service, causing authentication failures

## Remediation Steps
1. Verify the device can reach Intune required endpoints: login.microsoftonline.com, manage.microsoft.com, and *.dm.microsoft.com. Use Test-NetConnection or Invoke-WebRequest from the device.
2. Force a manual sync from the device: Settings > Accounts > Access work or school > select the MDM enrollment > Info > Sync.
3. If manual sync fails, restart the Intune Management Extension service (IntuneManagementExtension) from Services.msc on the device.
4. On the device, run the command: 'dsregcmd /status' to verify Azure AD join status and check for any errors in the Device State section.
5. If the issue persists, re-enroll the device by removing the work or school account and re-adding it via Settings > Accounts > Access work or school > Connect.
6. As a last resort, retire and re-enroll the device from the Intune console.

## Validation
After remediation, confirm the device shows a compliance status of 'Compliant' in the Intune console and the last check-in timestamp updates to within the last few minutes. The user should regain access to company resources protected by Conditional Access.

## Rollback
If re-enrollment is performed, the device will be treated as a new enrollment. To roll back, restore the device from a backup or re-join it to Azure AD and re-enroll without retiring.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-compliance>
