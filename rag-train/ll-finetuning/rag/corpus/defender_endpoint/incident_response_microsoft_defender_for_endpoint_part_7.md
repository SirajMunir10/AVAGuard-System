# Incident Response: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Incident Response

## Scenario / Query
What happens when a contained device changes its IP address?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Contained device with IP change

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. If a contained device changes its IP address, all Microsoft Defenders for Endpoint onboarded devices recognize this and start blocking communications with the new IP address.
2. The original IP address is no longer blocked (It might take up to 5 minutes to see these changes).

## Validation
1. Verify that the new IP address of the contained device is listed in the blocked IP addresses for the tenant: Run the advanced hunting query `DeviceNetworkEvents | where ActionType == 'Blocked' and RemoteIP == '<new_IP>' | summarize by RemoteIP, Timestamp`. 2. Confirm that the original IP address is no longer blocked: Run `DeviceNetworkEvents | where ActionType == 'Blocked' and RemoteIP == '<original_IP>' | summarize by RemoteIP, Timestamp` and ensure no recent results. 3. Wait up to 5 minutes after the IP change, then check the device containment status in the Microsoft Defender portal: Navigate to Devices, select the device, and confirm the containment status is still active and the new IP is reflected in the device details.

## Rollback
1. If the new IP is not being blocked after 5 minutes, manually add the new IP to the block list: In Microsoft Defender, go to Settings > Endpoints > Rules > IP address block list and add the new IP. 2. If the original IP is still being blocked incorrectly, remove it from the block list: In the same IP address block list, delete the original IP entry. 3. If containment is lost, re-initiate containment on the device: In the Microsoft Defender portal, select the device and choose 'Contain device' from the actions menu.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
