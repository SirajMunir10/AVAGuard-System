# Implementation: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Implementation

## Scenario / Query
How to set up risk report archiving or integration with SIEM tools in Microsoft Entra ID Protection?

## Environment Context
- **Tenant Type:** Microsoft Entra ID tenant with Identity Protection enabled
- **Configuration:** ID Protection reports can be archived for storage or integrated with SIEM tools.

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Archive ID Protection reports for storage.
2. Integrate ID Protection reports with Security Information and Event Management (SIEM) tools for further analysis.
3. Use Microsoft Defender, Microsoft Sentinel, or Microsoft Graph API integrations to aggregate data with other sources.

## Validation
1. Verify that risk report archiving is configured by navigating to the Microsoft Entra admin center > Identity Protection > Reports. Confirm that the 'Export to Azure Storage' option is enabled and the storage account is correctly linked. 2. Validate SIEM integration by checking the Microsoft Sentinel data connectors: go to Microsoft Sentinel > Data connectors > 'Microsoft Entra ID Protection' and confirm the connector status shows 'Connected'. 3. Use Microsoft Graph API to retrieve a list of risk detections: run `GET https://graph.microsoft.com/v1.0/identityProtection/riskDetections` and verify that the response returns recent risk data. 4. Confirm that risk reports are being exported by checking the Azure Storage account container for recent .csv or .json files.

## Rollback
1. Disable risk report archiving: in the Microsoft Entra admin center, navigate to Identity Protection > Reports, and disable the 'Export to Azure Storage' option. 2. Remove the SIEM integration: in Microsoft Sentinel, go to Data connectors > 'Microsoft Entra ID Protection' and select 'Disconnect'. 3. If using Microsoft Graph API integration, revoke the application permissions for Identity Risk Event API by removing the delegated or application permissions from the registered app in Microsoft Entra ID > App registrations. 4. Delete any exported risk data from the Azure Storage container if no longer needed.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk>
