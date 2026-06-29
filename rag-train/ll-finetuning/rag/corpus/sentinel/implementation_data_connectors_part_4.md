# Implementation: Data Connectors (Data connector not found)

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Implementation

## Scenario / Query
How do I resolve the 'Data connector not found' error when trying to enable the Microsoft Defender for Cloud connector in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Enterprise (Azure AD + Azure subscription with Microsoft Defender for Cloud enabled)
- **Configuration:** Microsoft Sentinel workspace in the same region as the Defender for Cloud subscription; Contributor permissions on both the Sentinel workspace and the subscription.

## Symptoms
- When attempting to connect Microsoft Defender for Cloud to Sentinel via the Data Connectors blade, the connector status shows 'Not connected' or 'Connection failed'.
- The error message 'Data connector not found' appears in the Azure portal.
- Security alerts from Defender for Cloud are not appearing in Sentinel.

## Error Codes
- `Data connector not found`

## Root Causes
1. The Microsoft Defender for Cloud connector requires the 'SecurityInsights' resource provider to be registered on the subscription where the Defender for Cloud policy is applied.
2. The connector may not have been properly onboarded because the Sentinel workspace is in a different tenant or the subscription is not linked to the same Azure AD tenant.
3. Insufficient permissions (missing 'Microsoft.SecurityInsights/onboardingStates/read' and 'write' permissions).

## Remediation Steps
1. 1. Register the Microsoft.SecurityInsights resource provider on the subscription: Run `Register-AzResourceProvider -ProviderNamespace Microsoft.SecurityInsights` in Azure PowerShell or use `az provider register --namespace Microsoft.SecurityInsights` in Azure CLI.
2. 2. Ensure the Sentinel workspace and the Defender for Cloud subscription are in the same Azure AD tenant.
3. 3. Verify that the user enabling the connector has at least Contributor permissions on both the Sentinel workspace and the subscription containing Defender for Cloud.
4. 4. In the Azure portal, navigate to Microsoft Sentinel > Data Connectors, select the Microsoft Defender for Cloud connector, and click 'Open connector page'. Then click 'Connect' to re-establish the connection.
5. 5. If the issue persists, wait 5 minutes and refresh the connector status; the registration may take a few minutes to propagate.

## Validation
After completing the remediation steps, verify that the connector status in Sentinel shows 'Connected' and that Defender for Cloud alerts appear in the Sentinel Logs under the 'SecurityAlert' table.

## Rollback
To disconnect the connector, open the Microsoft Defender for Cloud connector page in Sentinel and click 'Disconnect'. This will stop the flow of alerts but does not affect Defender for Cloud itself.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/connect-defender-for-cloud>
