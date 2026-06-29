# Implementation: Endpoint Security Policy

**Domain:** Intune
**Subdomain:** Endpoint Security Policy
**Incident Type:** Implementation

## Scenario / Query
How to configure Endpoint Detection and Response (EDR) policy in Intune with Defender for Endpoint integration?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Defender for Endpoint tenant connection with Intune

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure Defender for Endpoint tenant connection with Intune is established.
2. Use Defender-specific onboarding configurations for each platform.
3. Configure EDR policy to provide real-time attack detection and response capabilities.

## Validation
1. Confirm Defender for Endpoint tenant connection: In Microsoft Intune admin center, go to Tenant administration > Connectors and tokens > Microsoft Defender for Endpoint. Verify the status shows 'Enabled' and the connection is active.
2. Verify EDR policy assignment: In Intune, navigate to Endpoint security > Endpoint detection and response. Confirm an EDR policy exists for the target platform (e.g., Windows, macOS, Linux) with the correct onboarding configuration (e.g., Defender for Endpoint onboarding blob for Windows).
3. Check policy deployment status: Select the EDR policy, click 'Device status' and ensure devices show 'Succeeded' or 'Compliant'.
4. Validate real-time detection: On a managed device, open Microsoft 365 Defender portal (security.microsoft.com) and confirm the device appears in the device inventory with an active sensor status.

## Rollback
1. Disable or delete the EDR policy: In Intune, go to Endpoint security > Endpoint detection and response, select the policy, and choose 'Delete' to remove it, or set the policy assignment to 'Not configured' for all groups.
2. Remove Defender for Endpoint connection: In Intune, go to Tenant administration > Connectors and tokens > Microsoft Defender for Endpoint, select 'Disconnect' and confirm to sever the tenant connection.
3. Revert onboarding configurations: On affected devices, uninstall the Defender for Endpoint sensor via 'Add or Remove Programs' (Windows) or remove the onboarding package (macOS/Linux).
4. Verify rollback: Check that devices no longer appear in Microsoft 365 Defender device inventory and that Intune policy status shows 'Not applicable' or 'Error' for the removed policy.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/endpoint-security-policy>
