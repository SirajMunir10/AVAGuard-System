# Implementation: Advanced Hunting

**Domain:** Defender for Endpoint
**Subdomain:** Advanced Hunting
**Incident Type:** Implementation

## Scenario / Query
How do I enable and start using advanced hunting in Microsoft Defender XDR?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** Advanced hunting requires Microsoft Defender XDR to be turned on. For Microsoft Sentinel integration, connect Microsoft Sentinel to the Defender portal.

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Turn on Microsoft Defender XDR to use advanced hunting.
2. To use advanced hunting with Microsoft Sentinel, connect Microsoft Sentinel to the Defender portal.

## Validation
1. Confirm that Microsoft Defender XDR is turned on by navigating to the Microsoft Defender portal (https://security.microsoft.com) and verifying that the 'Advanced hunting' option appears in the left navigation pane under 'Investigation & response'.
2. Run a sample advanced hunting query in the portal to ensure data is being returned, e.g., `DeviceInfo | take 10`.
3. If Microsoft Sentinel integration is configured, verify the connection by going to the Microsoft Defender portal > Settings > Microsoft Sentinel, and confirm the status shows 'Connected'.

## Rollback
1. If advanced hunting is not working as expected, ensure Microsoft Defender XDR is still enabled by checking the same navigation pane. If it was recently turned off, re-enable it via the Microsoft 365 Defender portal settings.
2. If the Microsoft Sentinel connection is causing issues, disconnect it by navigating to the Microsoft Defender portal > Settings > Microsoft Sentinel and selecting 'Disconnect'.
3. If queries fail, verify that the necessary data connectors (e.g., Microsoft Defender for Endpoint) are properly configured and streaming data to the workspace.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-overview>
