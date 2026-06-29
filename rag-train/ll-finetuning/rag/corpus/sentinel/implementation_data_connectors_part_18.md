# Implementation: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Implementation

## Scenario / Query
How do I configure the Microsoft 365 Defender data connector in Microsoft Sentinel to collect events from Defender for Endpoint, Defender for Office 365, Defender for Identity, and Defender for Cloud Apps?

## Environment Context
- **Tenant Type:** Azure/Entra ID
- **Configuration:** Microsoft Sentinel workspace with Microsoft 365 Defender connector enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Mark the check boxes of the tables with the event types you wish to collect: Defender for Endpoint, Defender for Office 365, Defender for Identity, Defender for Cloud Apps, Defender alerts.
2. Select Apply Changes.

## Validation
1. In the Microsoft Sentinel workspace, navigate to Data connectors and select Microsoft 365 Defender. 2. Verify that the connector status shows 'Connected'. 3. Check that the checkboxes for the following tables are marked: 'AdvancedHuntingDeviceAlertEvents', 'AdvancedHuntingDeviceInfo', 'AdvancedHuntingDeviceNetworkEvents', 'AdvancedHuntingDeviceProcessEvents', 'AdvancedHuntingDeviceRegistryEvents', 'AdvancedHuntingDeviceFileEvents', 'AdvancedHuntingDeviceLogonEvents', 'AdvancedHuntingDeviceImageLoadEvents', 'AdvancedHuntingDeviceEvents', 'AdvancedHuntingDeviceTvmSoftwareInventoryVulnerabilities', 'AdvancedHuntingDeviceTvmSoftwareVulnerabilities', 'AdvancedHuntingDeviceTvmSecureConfigurationAssessment', 'AdvancedHuntingDeviceTvmSecureConfigurationAssessmentKB', 'AdvancedHuntingEmailEvents', 'AdvancedHuntingEmailAttachmentInfo', 'AdvancedHuntingEmailUrlInfo', 'AdvancedHuntingEmailPostDeliveryEvents', 'AdvancedHuntingIdentityLogonEvents', 'AdvancedHuntingIdentityQueryEvents', 'AdvancedHuntingIdentityDirectoryEvents', 'AdvancedHuntingIdentityInfo', 'AdvancedHuntingCloudAppEvents', 'AdvancedHuntingAlertInfo', 'AdvancedHuntingAlertEvidence', 'SecurityAlert' (for Defender alerts). 4. Run the following KQL query in Log Analytics to confirm data ingestion: 'Microsoft365Defender | take 10'. 5. Verify that the query returns results within the expected time range.

## Rollback
1. In the Microsoft Sentinel workspace, navigate to Data connectors and select Microsoft 365 Defender. 2. Uncheck all the checkboxes for the tables that were previously selected (Defender for Endpoint, Defender for Office 365, Defender for Identity, Defender for Cloud Apps, Defender alerts). 3. Select 'Apply Changes'. 4. Confirm that the connector status changes to 'Disconnected' or that the data collection stops. 5. If the connector was previously configured with a different set of tables, re-select only those original tables and apply changes. 6. Run the KQL query 'Microsoft365Defender | take 10' to verify that data ingestion has stopped or reverted to the previous state.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/connect-microsoft-365-defender>
