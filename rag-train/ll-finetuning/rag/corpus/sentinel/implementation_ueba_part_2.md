# Implementation: UEBA

**Domain:** Sentinel
**Subdomain:** UEBA
**Incident Type:** Implementation

## Scenario / Query
How to enable and configure UEBA for Microsoft Sentinel workspace to synchronize user data to the IdentityInfo table?

## Environment Context
- **Tenant Type:** Microsoft Sentinel workspace
- **Configuration:** UEBA enabled and configured with Microsoft Entra ID (cloud-based) or Microsoft Active Directory (on-premises, requires Microsoft Defender for Identity)

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Enable and configure UEBA for your Microsoft Sentinel workspace.
2. Select Microsoft Entra ID (cloud-based) or Microsoft Active Directory (on-premises, requires Microsoft Defender for Identity) as identity providers when configuring UEBA.

## Validation
1. In the Azure portal, navigate to your Microsoft Sentinel workspace. 2. Under 'Configuration', select 'Entity behavior analytics' (UEBA). 3. Verify that 'UEBA' is set to 'On'. 4. Under 'Identity providers', confirm that the desired provider (Microsoft Entra ID or Active Directory) is selected and shows a 'Connected' status. 5. Run the following KQL query in the Sentinel Logs workspace to confirm data is populating the IdentityInfo table: `IdentityInfo | take 10`. 6. Check that the query returns rows with recent timestamps, indicating synchronization is active.

## Rollback
1. In the Azure portal, navigate to your Microsoft Sentinel workspace. 2. Under 'Configuration', select 'Entity behavior analytics' (UEBA). 3. Set 'UEBA' to 'Off'. 4. If you need to remove a connected identity provider, under 'Identity providers', click the provider and select 'Disconnect'. 5. To fully revert, ensure no UEBA-related data is being ingested by disabling any associated data connectors (e.g., Microsoft Entra ID or Microsoft Defender for Identity) if they were enabled solely for UEBA. 6. Monitor the IdentityInfo table to confirm no new records appear.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/ueba-enrichments>
