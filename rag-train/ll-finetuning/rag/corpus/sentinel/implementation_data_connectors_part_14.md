# Implementation: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Implementation

## Scenario / Query
How do I connect on-premises Active Directory user identities into Microsoft Sentinel through Microsoft Defender for Identity?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace with Microsoft Defender for Identity

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. In Microsoft Sentinel, select Data connectors.
2. Select Microsoft Defender XDR from the gallery and Open connector page.
3. In the Configuration section, select Connect entities to enable the integration of on-premises Active Directory user identities into Microsoft Sentinel through Microsoft Defender for Identity.

## Validation
1. In Microsoft Sentinel, navigate to Data connectors and select Microsoft Defender XDR. 2. On the connector page, verify that the status shows 'Connected' and that the 'Connect entities' toggle is enabled. 3. Run the following KQL query in Sentinel Logs: `MicrosoftDefenderForIdentity | where TimeGenerated > ago(1h) | take 10`. Confirm that results include on-premises AD user identity data. 4. Check Microsoft Defender for Identity health page to ensure sensor is reporting and syncing identities.

## Rollback
1. In Microsoft Sentinel, go to Data connectors and select Microsoft Defender XDR. 2. On the connector page, disable the 'Connect entities' toggle to stop the integration. 3. If needed, remove the Microsoft Defender XDR data connector entirely by selecting 'Disconnect' on the connector page. 4. Verify in Microsoft Defender for Identity that no Sentinel-related identity sync is active.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/connect-microsoft-365-defender>
