# Incident Response: Device Compliance

**Domain:** Intune
**Subdomain:** Device Compliance
**Incident Type:** Incident Response

## Scenario / Query
A user reports that their Windows 10 device is marked as non-compliant in Intune and they cannot access corporate email. The device shows a compliance status of 'Not evaluated' and the last check-in was over 24 hours ago. How do I investigate and resolve this?

## Environment Context
- **Tenant Type:** Enterprise (Microsoft 365 E5)
- **Configuration:** Conditional Access policy requires Intune compliance for Exchange Online access; device is Azure AD joined and enrolled in Intune via MDM.

## Symptoms
- Device shows 'Not evaluated' compliance status in Microsoft Intune admin center
- Last check-in timestamp is more than 24 hours old
- User cannot access corporate email on the device
- No recent errors in the device's Event Viewer under Microsoft-Windows-DeviceManagement-Enterprise-Diagnostics-Provider

## Error Codes
N/A

## Root Causes
1. Device has not checked in with Intune due to network connectivity issues or the Intune service endpoint being unreachable
2. The Intune management extension or the MDM client is not running or is blocked by security software
3. Device is in a power-saving state that prevents scheduled check-ins

## Remediation Steps
1. Verify the device can reach the Intune service endpoints: login.microsoftonline.com, manage.microsoft.com, and *.dm.microsoft.com
2. On the device, open Settings > Accounts > Access work or school, select the work account, and click 'Info' then 'Sync' to force a manual check-in
3. If sync fails, restart the Intune Management Extension service (IntuneManagementExtension) from Services.msc
4. If the issue persists, re-enroll the device by removing the work or school account and re-adding it via Settings > Accounts > Access work or school > Connect
5. Ensure no third-party firewall or antivirus is blocking the Intune service URLs

## Validation
After remediation, the device should show a compliance status of 'Compliant' in the Intune admin center within 15 minutes, and the user should regain access to corporate email.

## Rollback
If re-enrollment is performed, the device will need to be reconfigured with any custom device restrictions or profiles that were previously applied. Document existing policies before re-enrollment.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-compliance>
