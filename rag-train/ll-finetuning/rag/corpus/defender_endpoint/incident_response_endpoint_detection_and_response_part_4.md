# Incident Response: Endpoint Detection and Response

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint Detection and Response
**Incident Type:** Incident Response

## Scenario / Query
How to contain a device from the Device inventory page in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Device inventory page

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Go to the Device inventory page and select the device to contain.
2. Select Contain device from the actions menu in the device flyout.
3. On the contain device popup, type a comment, and select Confirm.

## Validation
1. Navigate to the Device inventory page in Microsoft Defender for Endpoint. 2. Search for the contained device and select it to open the device flyout. 3. Verify that the device status shows 'Contained' or 'In Containment' and that the 'Contain device' action is no longer available (replaced by 'Release from containment' or similar). 4. Optionally, run an advanced hunting query: `DeviceInfo | where DeviceName == "<device_name>" | project DeviceName, DeviceStatus, LastSeen` to confirm the containment status.

## Rollback
1. Go to the Device inventory page and select the contained device. 2. In the device flyout, select 'Release from containment' from the actions menu. 3. On the release popup, type a comment and select Confirm. 4. Verify the device status returns to normal (e.g., 'Active') and that the device can communicate with the network again.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
