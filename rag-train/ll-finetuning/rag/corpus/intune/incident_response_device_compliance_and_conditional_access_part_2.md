# Incident Response: Device Compliance and Conditional Access

**Domain:** Intune
**Subdomain:** Device Compliance and Conditional Access
**Incident Type:** Incident Response

## Scenario / Query
A user reports that their Windows 10 device is marked as non-compliant in Intune and they cannot access corporate email. The device shows a compliance status of 'Not evaluated' and the last check-in was over 24 hours ago. How do I investigate and resolve this incident?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Intune and Conditional Access
- **Configuration:** Device compliance policy for Windows 10 requiring BitLocker, antivirus, and minimum OS version; Conditional Access policy blocking access for non-compliant devices

## Symptoms
- Device compliance status shows 'Not evaluated' in Microsoft Intune admin center
- Last check-in timestamp is older than 24 hours
- User cannot access corporate email or other cloud resources protected by Conditional Access
- Device appears as 'Not compliant' in Conditional Access reports

## Error Codes
N/A

## Root Causes
1. Device has not checked in with Intune service within the required interval (default 8 hours, configurable up to 30 days)
2. Device may be offline, powered off, or has a network connectivity issue preventing communication with Intune
3. Device enrollment certificate may have expired or been revoked
4. Intune management extension or Microsoft Intune Company Portal app may be corrupted or outdated

## Remediation Steps
1. 1. Verify device connectivity: Ensure the device has internet access and can reach *.manage.microsoft.com and *.dm.microsoft.com
2. 2. Force a manual sync: On the device, go to Settings > Accounts > Access work or school > select the work account > click Info > then Sync
3. 3. Restart the Intune service: On the device, open Services.msc, locate 'Microsoft Intune Management Extension', restart it, then force a sync again
4. 4. Re-enroll the device if necessary: If the above steps fail, remove the device from Intune (admin center > Devices > select device > Delete) and re-enroll by signing into the Company Portal app
5. 5. Verify compliance policy assignment: In Intune admin center, go to Devices > Compliance policies > select the policy > Assignments and confirm the user/device group is included

## Validation
After remediation, check the device compliance status in Intune admin center under Devices > All devices > select device > Device compliance. It should show 'Compliant' within 15 minutes. Also verify the user can access corporate email again.

## Rollback
If re-enrollment was performed, the original device record is deleted and cannot be restored. The user must re-enroll via Company Portal. If only a manual sync was performed, no rollback is needed.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-compliance>
- <https://learn.microsoft.com/en-us/mem/intune/remote-actions/device-sync>
