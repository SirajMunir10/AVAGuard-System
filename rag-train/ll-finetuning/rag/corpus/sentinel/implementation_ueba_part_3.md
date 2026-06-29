# Implementation: UEBA

**Domain:** Sentinel
**Subdomain:** UEBA
**Incident Type:** Implementation

## Scenario / Query
How to configure UEBA with on-premises Active Directory using Microsoft Defender for Identity?

## Environment Context
- **Tenant Type:** Microsoft Sentinel workspace with UEBA enabled
- **Configuration:** Microsoft Active Directory (on-premises, requires Microsoft Defender for Identity)

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enable and configure UEBA for your Microsoft Sentinel workspace.
2. Select Microsoft Active Directory (on-premises, requires Microsoft Defender for Identity) as the identity provider.

## Validation
1. In the Azure portal, navigate to your Microsoft Sentinel workspace. 2. Under 'Configuration', select 'Settings' and then the 'UEBA' tab. 3. Verify that 'UEBA' is enabled and that the identity provider is set to 'Microsoft Active Directory (on-premises, requires Microsoft Defender for Identity)'. 4. Run the following KQL query in Sentinel's Logs to confirm UEBA data is being ingested: `IdentityInfo | take 10`. 5. Check that Microsoft Defender for Identity sensors are deployed and reporting to the workspace by reviewing the 'Microsoft Defender for Identity' health page.

## Rollback
1. In the Azure portal, navigate to your Microsoft Sentinel workspace. 2. Under 'Configuration', select 'Settings' and then the 'UEBA' tab. 3. Disable UEBA by toggling the setting off. 4. If needed, remove the Microsoft Defender for Identity data connector from Sentinel by going to 'Data connectors', selecting 'Microsoft Defender for Identity', and clicking 'Disconnect'. 5. Verify that UEBA data ingestion has stopped by running `IdentityInfo | take 10` and confirming no results.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/ueba-enrichments>
