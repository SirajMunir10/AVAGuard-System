# Optimization: Device Compliance

**Domain:** Intune
**Subdomain:** Device Compliance
**Incident Type:** Optimization

## Scenario / Query
How can I optimize Intune device compliance policy evaluation by reducing unnecessary re-evaluation for devices that already meet compliance requirements?

## Environment Context
- **Tenant Type:** Enterprise (Microsoft Intune Plan 1)
- **Configuration:** Device compliance policies with multiple rules (e.g., OS version, encryption, antivirus). Default compliance evaluation schedule is every 8 hours for devices checking in.

## Symptoms
- Devices show frequent compliance status changes even when no configuration has changed
- High number of compliance policy evaluation events in Intune reporting
- Users report repeated notifications about compliance status
- Increased load on Intune service and device resources due to frequent policy evaluation

## Error Codes
N/A

## Root Causes
1. Compliance policies are configured with overly aggressive re-evaluation intervals
2. Multiple overlapping compliance policies causing redundant checks
3. Devices not properly checking in to Intune, leading to missed evaluation windows and forced re-evaluations

## Remediation Steps
1. Review and adjust compliance policy evaluation schedule: In Microsoft Intune admin center, go to Devices > Compliance policies > Policies, select a policy, and under 'Schedule', set 'Compliance status validity period' to a longer duration (e.g., 24 hours) if appropriate.
2. Consolidate overlapping compliance policies: Merge policies that target the same device groups and check similar conditions to reduce redundancy.
3. Ensure devices are regularly checking in: Verify that devices have active internet connectivity and are enrolled correctly; check the 'Check-in status' in the device's overview page.
4. Use the 'Grace period' setting for compliance policies to allow users time to remediate without immediate non-compliance flagging.

## Validation
After changes, monitor the 'Compliance status' report in Intune admin center (Reports > Device compliance) to see reduced fluctuation and fewer evaluation events. Also verify that devices remain compliant and users receive fewer notifications.

## Rollback
Revert compliance policy schedule to default (8 hours) and restore any consolidated policies to their original separate policies. Re-enable any grace periods that were removed.

## References
- Microsoft Learn: 'Monitor Intune device compliance' â€“ https://learn.microsoft.com/en-us/mem/intune/protect/compliance-policy-monitor
- Microsoft Learn: 'Compliance policy settings for Windows devices in Intune' â€“ https://learn.microsoft.com/en-us/mem/intune/protect/compliance-policy-create-windows
