# Implementation: Microsoft Defender XDR

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender XDR
**Incident Type:** Implementation

## Scenario / Query
How do I integrate Microsoft Defender XDR components with Microsoft Sentinel or a generic SIEM service for centralized monitoring?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Microsoft Defender XDR components, Microsoft Sentinel or generic SIEM service

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Integrate Microsoft Defender XDR components with Microsoft Sentinel using the connectors for Microsoft Defender components.
2. For generic SIEM integration, refer to the Generic SIEM integration documentation.

## Validation
1. In Microsoft Sentinel, navigate to Data connectors and verify that the Microsoft Defender XDR connector shows a status of 'Connected' and that data ingestion is active. 2. Run the following KQL query in Sentinel to confirm data is flowing: `MicrosoftDefenderXDR | take 10`. 3. For generic SIEM, confirm that the SIEM is receiving logs from the Microsoft Defender XDR API by checking the SIEM's ingestion logs for recent entries from the Microsoft 365 Defender source.

## Rollback
1. In Microsoft Sentinel, go to Data connectors, select the Microsoft Defender XDR connector, and click 'Disconnect' to remove the integration. 2. For generic SIEM, disable or delete the API integration configuration in the SIEM that connects to Microsoft Defender XDR. 3. If the integration was configured via Azure Policy or automation, remove or disable those policies to stop data flow.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/eval-overview>
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/eval-overview>
