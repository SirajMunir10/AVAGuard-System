# Incident Response: Device Compliance

**Domain:** Intune
**Subdomain:** Device Compliance
**Incident Type:** Incident Response

## Scenario / Query
A user reports that their Windows device is marked as non-compliant in Intune and they cannot access corporate resources. How do I investigate and resolve this incident?

## Environment Context
- **Tenant Type:** Microsoft Intune standalone (no co-management)
- **Configuration:** Device compliance policy requiring BitLocker encryption and Windows Defender Antivirus real-time protection enabled

## Symptoms
- Device shows 'Non-compliant' status in Microsoft Intune admin center
- User receives 'Your device does not meet your organization's compliance requirements' notification
- Conditional Access blocks access to Exchange Online and SharePoint Online

## Error Codes
N/A

## Root Causes
1. BitLocker Drive Encryption is not enabled on the device
2. Windows Defender Antivirus real-time protection is disabled or tampered with
3. Device has not checked in with Intune recently (check-in interval exceeded)

## Remediation Steps
1. Sign in to the Microsoft Intune admin center (https://intune.microsoft.com) and navigate to Devices > All devices > select the affected device > Device compliance to view the specific non-compliance reasons.
2. If BitLocker is missing: Enable BitLocker via Settings > System > About > BitLocker Drive Encryption, or run 'manage-bde -on C:' from an elevated command prompt.
3. If Defender real-time protection is off: Open Windows Security > Virus & threat protection > Manage settings and turn Real-time protection On.
4. Force a device sync: On the device, go to Settings > Accounts > Access work or school > select the MDM enrollment > Info > Sync, or run 'dsregcmd /sync' from an elevated command prompt.
5. After remediation, verify compliance status in Intune admin center under Devices > Monitor > Device compliance. The status should update within 15 minutes or after the next check-in.

## Validation
Confirm the device status changes to 'Compliant' in Intune admin center and the user can access corporate resources (e.g., Outlook Web App, SharePoint).

## Rollback
If a compliance policy setting was incorrectly enforced, modify the policy in Intune admin center (Devices > Compliance policies > Policies > select policy > Properties > Settings) to remove the requirement, then save and assign.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/compliance-policy-monitor>
- <https://learn.microsoft.com/en-us/mem/intune/protect/create-compliance-policy>
