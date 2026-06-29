# Implementation: UEBA

**Domain:** Sentinel
**Subdomain:** UEBA
**Incident Type:** Implementation

## Scenario / Query
How to access and use UEBA enrichments in Microsoft Sentinel for security incident investigations?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel with UEBA enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to entity pages in Microsoft Sentinel to view enrichments.
2. Query the BehaviorAnalytics table in Log Analytics to access UEBA output information.
3. Use the UsersInsights, DevicesInsights, and ActivityInsights dynamic fields from the BehaviorAnalytics table for entity information.
4. Review the IdentityInfo table for identity information synchronized from Microsoft Entra ID and on-premises Active Directory via Microsoft Defender for Identity.

## Validation
1. In Microsoft Sentinel, open an entity (user, device, or IP) page and confirm that the 'UEBA Enrichments' section displays insights such as 'User Insights', 'Device Insights', or 'Activity Insights'.
2. Run the following KQL query in Log Analytics to verify that the BehaviorAnalytics table returns data with the dynamic fields UsersInsights, DevicesInsights, and ActivityInsights:
   BehaviorAnalytics
   | take 10
   | project UsersInsights, DevicesInsights, ActivityInsights
3. Run the following KQL query to confirm the IdentityInfo table contains identity data:
   IdentityInfo
   | take 10

## Rollback
1. If UEBA enrichments are not needed, disable UEBA in Microsoft Sentinel by navigating to 'Settings' > 'Settings' > 'Entity behavior' and toggling the UEBA feature off.
2. If the BehaviorAnalytics table is not required, stop data collection by removing the relevant data connectors (e.g., Microsoft Entra ID, Microsoft Defender for Identity) that feed into UEBA.
3. If the IdentityInfo table is not needed, disable the synchronization of identity data by turning off the 'IdentityInfo' table in the Microsoft Sentinel settings or by removing the associated data connectors.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/ueba-enrichments>
