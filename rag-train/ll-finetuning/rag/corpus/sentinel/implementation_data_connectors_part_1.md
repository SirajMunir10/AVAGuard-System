# Implementation: Data Connectors (DataConnectorNotFound)

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Implementation

## Scenario / Query
How do I resolve a 'Data connector not found' error when trying to enable the Microsoft Defender for Cloud connector in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Microsoft Sentinel workspace in a single-tenant environment with Microsoft Defender for Cloud enabled

## Symptoms
- When attempting to enable the Microsoft Defender for Cloud connector in Microsoft Sentinel, the portal displays 'Data connector not found'.
- The connector status shows as 'Disconnected' or 'Error'.
- No security alerts from Defender for Cloud appear in Sentinel.

## Error Codes
- `DataConnectorNotFound`

## Root Causes
1. The Microsoft Defender for Cloud connector requires that the Defender for Cloud subscription is onboarded to the same tenant and that the necessary permissions (Security Reader or Security Admin) are granted to the Sentinel service principal.
2. The connector may not be listed if the subscription is not yet onboarded to Microsoft Defender for Cloud.

## Remediation Steps
1. 1. Verify that the subscription is onboarded to Microsoft Defender for Cloud by navigating to the Azure portal > Microsoft Defender for Cloud > Getting started and ensuring the subscription is listed.
2. 2. Ensure the Sentinel service principal has at least Security Reader permissions on the subscription. Use Azure RBAC to assign the 'Security Reader' role to the Microsoft Sentinel service principal (application ID: 1950a258-227b-4e31-a9cf-717495945fc2).
3. 3. In Microsoft Sentinel, go to Content hub > Microsoft Defender for Cloud and select 'Install' if not already installed.
4. 4. In Data connectors, select the Microsoft Defender for Cloud connector and click 'Open connector page'. Ensure the subscription is selected and click 'Connect'.
5. 5. If the connector still shows 'not found', wait 15 minutes and refresh the connector list.

## Validation
After remediation, the Microsoft Defender for Cloud connector should show a 'Connected' status in the Data connectors blade, and security alerts from Defender for Cloud should appear in the Sentinel Logs under the 'SecurityAlert' table.

## Rollback
Disconnect the connector by clicking 'Disconnect' on the connector page. Remove the Security Reader role assignment from the Sentinel service principal if desired.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/connect-defender-for-cloud>
