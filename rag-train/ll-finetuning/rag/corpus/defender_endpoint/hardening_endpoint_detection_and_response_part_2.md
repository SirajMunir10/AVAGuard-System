# Hardening: Endpoint Detection and Response

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint Detection and Response
**Incident Type:** Hardening

## Scenario / Query
How to contain a critical asset compromised and used to spread threats within an organization using Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Critical asset tag on device or IP page; automatic attack disruption

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Granularly contain the critical asset to prevent the spread of the attack while ensuring the asset remains operational for business continuity.
2. Through automatic attack disruption, Defender for Endpoint incriminates a malicious device, identifies the role of the device to apply a matching policy to automatically contain a critical asset.
3. The granular containment is done by blocking only specific ports and communication directions.
4. Identify critical assets by the critical asset tag on the device or IP page.

## Validation
1. Confirm the device is tagged as 'critical asset' by running: Get-MpComputerStatus | Select-Object -ExpandProperty DeviceTag (or check the device page in Microsoft 365 Defender).
2. Verify granular containment policy is applied: Use Microsoft 365 Defender > Devices > select device > 'Manage tags' to confirm 'critical asset' tag.
3. Check attack disruption status: In Microsoft 365 Defender, go to Incidents > select the relevant incident > 'Attack story' to confirm automatic containment actions were taken.
4. Validate blocked ports and directions: On the device, run 'netsh advfirewall show rule name=all' and look for rules with 'Block' action and specific ports/directions matching the containment policy.
5. Ensure business continuity: Test critical business applications that rely on the contained ports to confirm they still function (e.g., if port 445 is blocked, verify file shares are not needed or are redirected).

## Rollback
1. Remove the 'critical asset' tag if containment is no longer needed: In Microsoft 365 Defender > Devices > select device > 'Manage tags' > remove 'critical asset' tag.
2. Disable automatic attack disruption for the device: In Microsoft 365 Defender > Settings > Endpoints > Advanced features > 'Automatic attack disruption' > toggle off for the specific device (if supported) or adjust the policy scope.
3. Restore blocked ports and directions: Run 'netsh advfirewall firewall delete rule name="<containment rule name>"' for each rule created by the containment policy.
4. If the device was isolated, rejoin it to the network: In Microsoft 365 Defender > Devices > select device > 'Take action' > 'Release from isolation'.
5. Verify connectivity: Use Test-NetConnection -ComputerName <target> -Port <port> to confirm previously blocked ports are now open.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
