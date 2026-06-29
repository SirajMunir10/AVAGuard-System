# Optimization: Device Compliance

**Domain:** Intune
**Subdomain:** Device Compliance
**Incident Type:** Optimization

## Scenario / Query
How can I optimize Intune device compliance policy evaluation by reducing unnecessary re-evaluation for devices that have not changed state?

## Environment Context
- **Tenant Type:** Production
- **Configuration:** Device compliance policies with frequent re-evaluation cycles

## Symptoms
- High number of compliance policy evaluation requests per device per day
- Increased load on Intune service and potential throttling
- Unnecessary network traffic and device resource usage

## Error Codes
N/A

## Root Causes
1. Compliance policies are configured with a short evaluation schedule (e.g., every 1 hour) even for devices that rarely change compliance state
2. No use of grace periods or check-in intervals to reduce frequency

## Remediation Steps
1. Review and adjust the compliance policy evaluation schedule to a longer interval (e.g., every 8 hours or daily) for devices that are stable
2. Implement a grace period for non-compliant devices to allow time for remediation before re-evaluation
3. Use the 'Device compliance policy evaluation schedule' setting in Intune to set a minimum interval of 8 hours or more as recommended by Microsoft

## Validation
Monitor the number of compliance policy evaluation requests per device in Intune reporting. Verify that the new schedule reduces the frequency without delaying compliance detection beyond acceptable thresholds.

## Rollback
Revert the evaluation schedule to the previous shorter interval if compliance detection delays become unacceptable.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/create-compliance-policy>
