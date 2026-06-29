# Remediation: Endpoint security

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint security
**Incident Type:** Remediation

## Scenario / Query
How to release a device from automatic isolation after mitigating a risk and completing investigation in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Device isolation feature

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select the device from the Device inventory or open the device page.
2. Select Release from isolation from the action menu.

## Validation
1. Navigate to Microsoft 365 Defender portal (https://security.microsoft.com).
2. Go to Endpoints > Device inventory.
3. Locate the device that was isolated.
4. Open the device page and confirm the 'Isolation status' shows 'Not isolated'.
5. Verify the device can communicate with the network (e.g., ping a known internal resource).
6. Check the device's connectivity to Defender for Endpoint services by running 'Test-MDEConnection' on the device (if available).

## Rollback
1. If the device remains isolated or connectivity issues persist, re-isolate the device by selecting 'Isolate' from the action menu on the device page.
2. Confirm the isolation status changes to 'Isolated'.
3. Re-investigate the device for any remaining threats.
4. If the release action failed, retry the release after ensuring the device is online and accessible.
5. If the issue continues, contact Microsoft support with the device ID and timestamp of the failed release attempt.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
