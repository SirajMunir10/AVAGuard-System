# Implementation: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Implementation

## Scenario / Query
How do I connect Microsoft Defender XDR incidents and alerts to Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace with Microsoft Defender XDR connector

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Mark the check box labeled 'Turn off all Microsoft incident creation rules for these products. Recommended', to avoid duplication of incidents. This check box doesn't appear once the Microsoft Defender XDR connector is connected.
2. Select the 'Connect incidents & alerts' button.

## Validation
1. In the Microsoft Sentinel workspace, navigate to Data connectors and select the Microsoft Defender XDR connector. 2. Confirm the connector status shows 'Connected'. 3. Verify that the 'Turn off all Microsoft incident creation rules for these products' checkbox is no longer visible (it disappears after connection). 4. Check that incidents and alerts from Microsoft Defender XDR are appearing in Microsoft Sentinel (e.g., under Incidents or Logs with the 'MicrosoftDefenderXDR' table).

## Rollback
1. In the Microsoft Sentinel workspace, go to Data connectors and select the Microsoft Defender XDR connector. 2. Click 'Disconnect' to remove the connector. 3. Re-enable any previously disabled Microsoft incident creation rules for Defender products (if needed) by navigating to Analytics > Rule templates and enabling the relevant rules. 4. Verify that incidents and alerts from Microsoft Defender XDR are no longer flowing into Sentinel.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/connect-microsoft-365-defender>
