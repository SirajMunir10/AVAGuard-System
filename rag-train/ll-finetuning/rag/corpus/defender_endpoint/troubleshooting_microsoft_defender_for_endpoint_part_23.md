# Troubleshooting: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Troubleshooting

## Scenario / Query
What happens if a device is inactive or offline when an isolation action is submitted in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** N/A

## Symptoms
- Device is inactive or offline when isolation action is submitted.

## Error Codes
N/A

## Root Causes
1. Device is inactive or offline at the time of isolation action submission.

## Remediation Steps
1. Microsoft Defender for Endpoint retries enforcing the isolation for up to three days.
2. If the device doesn't reconnect in that time, the isolation won't be retried.
3. Administrators should reissue the isolation action after the device becomes active.

## Validation
1. Check the device's connectivity status in Microsoft Defender for Endpoint: navigate to Devices list, select the device, and verify its 'Last seen' timestamp is recent (within minutes).
2. Confirm the isolation action status: in the device page, go to 'Action center' and verify the isolation action shows 'Completed' or 'Pending' with no 'Failed' status.
3. If the device was offline, wait up to 3 days and re-check the action status; if it remains 'Pending' or 'Failed', proceed to rollback.

## Rollback
1. If the isolation action failed or the device remains offline after 3 days, reissue the isolation action once the device is active (i.e., 'Last seen' timestamp is current).
2. To remove isolation if it was applied incorrectly: navigate to the device page, select 'Action center', choose the isolation action, and click 'Release from isolation'.
3. Alternatively, use the API: POST /api/machines/{machineId}/unisolate with appropriate authorization.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
