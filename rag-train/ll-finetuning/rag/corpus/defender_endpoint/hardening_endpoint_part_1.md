# Hardening: Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint
**Incident Type:** Hardening

## Scenario / Query
How to handle file blocking beyond the Stop and Quarantine action timeout or for more than 1000 devices?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** N/A

## Symptoms
- Stop and quarantine file action limited to a maximum of 1000 devices
- Stop and quarantine action has a maximum timeout period of 3 days; if device remains offline longer, action not delivered

## Error Codes
N/A

## Root Causes
1. Stop and quarantine file action is limited to a maximum of 1000 devices.
2. Stop and quarantine action has a maximum timeout period of 3 days; if targeted device remains offline longer, action not delivered.

## Remediation Steps
1. To stop a file on a larger number of devices, see Add indicator to block or allow file.
2. To ensure the file remains blocked beyond the timeout or after the action completes, create an indicator to block the file explicitly.

## Validation
1. Confirm that the file indicator is created and active: In Microsoft Defender for Endpoint, navigate to Settings > Endpoints > Indicators > File hashes. Verify the file hash is listed with action 'Block and remediate' and status 'Active'.
2. Validate the indicator applies to the intended scope: Check the indicator's scope (e.g., 'All devices' or specific device groups) matches the target devices.
3. Test the block on a sample device: On a test device, attempt to access or execute the file. Confirm the file is blocked and a notification appears.
4. Check the indicator's expiration: Ensure the indicator's expiration date is set appropriately (or 'Never' if permanent).
5. Review the action history: In the Action center, verify that the 'Stop and Quarantine' action was delivered to the original devices (if applicable) and that the indicator is now in effect.

## Rollback
1. Remove or disable the file indicator: In Microsoft Defender for Endpoint, go to Settings > Endpoints > Indicators > File hashes. Select the indicator and choose 'Remove' or set its status to 'Disabled'.
2. If the original 'Stop and Quarantine' action is still pending or failed, cancel it: In the Action center, locate the action and select 'Cancel action'.
3. For devices that already received the quarantine action, restore the file from quarantine: On each affected device, open Windows Security > Virus & threat protection > Protection history, find the quarantined item, and select 'Restore'.
4. If the file was blocked by the indicator and needs to be allowed temporarily, create a temporary allow indicator: Add a new file hash indicator with action 'Allow' and a short expiration time.
5. Monitor for any unintended blocks: Check the device's event logs or Microsoft Defender for Endpoint alerts for any unexpected file blocks after the rollback.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-file-alerts>
