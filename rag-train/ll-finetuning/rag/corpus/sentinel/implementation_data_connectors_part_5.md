# Implementation: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Implementation

## Scenario / Query
How do I enable the Microsoft Sentinel solution for Microsoft Defender for Cloud Apps (formerly Microsoft Cloud App Security) and connect it to ingest alerts and cloud discovery logs?

## Environment Context
- **Tenant Type:** Enterprise (Azure AD tenant with Microsoft 365 E5 license)
- **Configuration:** Microsoft Sentinel workspace already created; Microsoft Defender for Cloud Apps enabled in the tenant

## Symptoms
- No Microsoft Defender for Cloud Apps alerts appear in Sentinel
- Cloud Discovery logs are not visible in the Sentinel Logs workspace
- The Microsoft Defender for Cloud Apps connector shows 'Disconnected' status

## Error Codes
N/A

## Root Causes
1. The Microsoft Sentinel solution for Microsoft Defender for Cloud Apps has not been installed from the Content Hub
2. The data connector for Microsoft Defender for Cloud Apps has not been configured or enabled
3. Required permissions (Security Administrator or Global Administrator) are missing to authorize the connection

## Remediation Steps
1. In the Azure portal, navigate to Microsoft Sentinel > Content hub. Search for 'Microsoft Defender for Cloud Apps' and install the solution.
2. After installation, go to Microsoft Sentinel > Data connectors. Select 'Microsoft Defender for Cloud Apps' and open the connector page.
3. Click 'Open connector page' and under 'Configuration', select the alert types to stream (e.g., Alerts, Cloud Discovery logs).
4. Click 'Connect' to establish the connection. Ensure the connector status changes to 'Connected'.
5. Verify that logs are flowing by querying the 'SecurityAlert' table for MCAS alerts or the 'McasShadowItReporting' table for Cloud Discovery data.

## Validation
Run the following KQL query in Sentinel Logs: SecurityAlert | where ProviderName == 'MCAS' | take 10. If results appear, the connector is working.

## Rollback
Disconnect the connector in the Data connectors page, then remove the solution from Content Hub if no longer needed.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/connect-defender-for-cloud-apps>
