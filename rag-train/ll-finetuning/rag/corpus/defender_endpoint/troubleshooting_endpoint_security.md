# Troubleshooting: Endpoint security

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint security
**Incident Type:** Troubleshooting

## Scenario / Query
What to check if isolation is removed unexpectedly from a device in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Time-limited undo window for isolation

## Symptoms
- Isolation is removed unexpectedly

## Error Codes
N/A

## Root Causes
1. A time-limited undo window may apply in your environment

## Remediation Steps
1. Check whether a time-limited undo window applies in your environment.
2. Review the action history for the release event.

## Validation
1. In Microsoft Defender for Endpoint, navigate to the device page for the affected machine. 2. Under 'Action center', review the 'Action history' for any 'Release from isolation' events. 3. Confirm the timestamp of the release event and check if it falls within the time-limited undo window (typically 1 hour). 4. Verify the user or process that initiated the release. 5. Check the device's current isolation status in the device inventory.

## Rollback
1. If the isolation was removed unexpectedly and the device is still within the time-limited undo window, re-initiate isolation from the device page by selecting 'Isolate device'. 2. If the undo window has expired, submit a new isolation request via the 'Actions' menu on the device page. 3. After re-isolation, verify the device status shows 'Isolated' in the device inventory. 4. Review the action history again to confirm the new isolation action was recorded.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
