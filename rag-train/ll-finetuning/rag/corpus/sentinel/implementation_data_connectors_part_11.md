# Implementation: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Implementation

## Scenario / Query
How do I identify the support type for a Microsoft Sentinel data connector?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Check the data connector page in Microsoft Sentinel for the support type listed.
2. If the data connector is Microsoft-supported, refer to Microsoft Azure Support Plans for support.
3. If the data connector is partner-supported, contact the specified data connector support contact.
4. If the data connector is community-supported, file an issue in the Microsoft Sentinel GitHub community.

## Validation
1. Navigate to the Microsoft Sentinel workspace in the Azure portal. 2. Under 'Content management', select 'Data connectors'. 3. Locate the specific data connector in the list. 4. Verify that the 'Support type' column displays the expected value (e.g., 'Microsoft', 'Partner', or 'Community'). 5. Confirm that the support type matches the documentation for that connector.

## Rollback
1. If the support type is incorrect or the connector is not functioning as expected, revert to the previous data connector configuration. 2. For Microsoft-supported connectors, ensure the connector is properly installed and configured per Microsoft documentation. 3. For partner-supported connectors, contact the partner's support team for assistance. 4. For community-supported connectors, check the GitHub repository for known issues or rollback to a previous version of the connector if available.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/connect-data-sources>
