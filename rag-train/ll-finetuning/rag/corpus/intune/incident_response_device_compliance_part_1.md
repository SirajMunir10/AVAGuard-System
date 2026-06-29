# Incident Response: Device Compliance

**Domain:** Intune
**Subdomain:** Device Compliance
**Incident Type:** Incident Response

## Scenario / Query
A user reports that their Windows 10 device is marked as non-compliant in Intune even though it appears to meet all defined compliance policies. How do you investigate and remediate this incident?

## Environment Context
- **Tenant Type:** Microsoft Intune standalone (no co-management)
- **Configuration:** Compliance policy for Windows 10 devices requiring BitLocker, Windows Defender Antivirus, and minimum OS version 22H2

## Symptoms
- Device shows 'Not compliant' in Microsoft Intune admin center
- User receives email notification about device non-compliance
- Device is compliant with all specified policy rules when checked locally

## Error Codes
N/A

## Root Causes
1. Device has not checked in with Intune recently (check-in interval exceeded)
2. Compliance policy evaluation failed due to a transient service issue
3. Device is in a grace period after a policy change

## Remediation Steps
1. 1. In the Intune admin center, go to Devices > All devices, select the device, and click Sync to force a check-in.
2. 2. After sync completes, go to Monitor > Device compliance and verify the compliance state updates.
3. 3. If still non-compliant, review the compliance policy assignment and ensure the device is in the correct group.
4. 4. Check the device's compliance policy status report for specific failure reasons.
5. 5. If the issue persists, re-evaluate the compliance policy settings and ensure they match the device's configuration.

## Validation
After performing a manual sync, the device compliance state should update to 'Compliant' within 15 minutes. Confirm in the Intune admin center under Device compliance.

## Rollback
If the sync does not resolve the issue, remove the device from the compliance policy assignment group, wait for the next check-in, then re-add it.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-compliance>
