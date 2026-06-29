# Hardening: Data Loss Prevention (DLP)

**Domain:** Purview
**Subdomain:** Data Loss Prevention (DLP)
**Incident Type:** Hardening

## Scenario / Query
How do I harden my Microsoft Purview DLP policies by enabling endpoint DLP and restricting data exfiltration actions like copy, print, and USB transfer?

## Environment Context
- **Tenant Type:** Microsoft 365 E5/A5/G5 with Purview Data Loss Prevention (DLP) licensed
- **Configuration:** Endpoint DLP not yet configured; default DLP policies exist but lack device-level controls

## Symptoms
- Users can copy sensitive data to USB drives or print documents containing credit card numbers without restriction
- DLP policy alerts are generated but no automatic blocking occurs on endpoints
- Endpoint DLP agent is not installed or not reporting status in Purview compliance portal

## Error Codes
N/A

## Root Causes
1. Endpoint DLP has not been onboarded in the Microsoft 365 Defender console
2. No DLP policy configured with endpoint device actions (e.g., Block, Audit) for high-risk activities like copy to removable media or print
3. Device groups and policy scoping are missing or misconfigured

## Remediation Steps
1. Onboard endpoints to Endpoint DLP by deploying the Microsoft 365 Defender for Endpoint sensor and enabling DLP in the Microsoft 365 Defender portal (Settings > Endpoints > Advanced features > Microsoft Purview DLP)
2. Create or modify a DLP policy in the Microsoft Purview compliance portal (Data Loss Prevention > Policies) that includes endpoint locations and specifies actions such as 'Block' for 'Copy to clipboard', 'Print', and 'Copy to removable media'
3. Scope the policy to specific device groups or users using the 'Locations' tab and ensure the policy is enabled
4. Install the latest Microsoft 365 Apps for enterprise on endpoints to support DLP actions on Office files
5. Verify endpoint DLP agent status by running Get-MpComputerStatus in PowerShell on a test device

## Validation
In the Microsoft Purview compliance portal, navigate to Data Loss Prevention > Policies, select the hardened policy, and confirm that 'Endpoint' is listed under Locations and that the policy status is 'On'. On a test endpoint, attempt to copy a file containing a credit card number to a USB drive; the action should be blocked and an audit event generated in Activity Explorer.

## Rollback
Disable the DLP policy by setting its status to 'Off' in the Microsoft Purview compliance portal, or remove the endpoint location from the policy. To fully uninstall the Endpoint DLP agent, use the Microsoft 365 Defender console to remove the device group or uninstall the sensor.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-get-started>
- <https://learn.microsoft.com/en-us/purview/endpoint-dlp-onboard-devices>
- <https://learn.microsoft.com/en-us/purview/dlp-endpoint-policy-reference>
