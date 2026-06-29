# Implementation: UEBA

**Domain:** Sentinel
**Subdomain:** UEBA
**Incident Type:** Implementation

## Scenario / Query
What changes occur to the IdentityInfo table when transitioning to the Defender portal with UEBA enabled?

## Environment Context
- **Tenant Type:** Microsoft Sentinel in Microsoft Defender portal
- **Configuration:** UEBA enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. As of May 2025, customers with UEBA enabled begin using a new release of the Advanced hunting version, referred to as the unified version or unified IdentityInfo table, which includes all UEBA fields from the Log Analytics version and some new fields.
2. Review the 'Compare to unified schema' tab to view changes that could affect queries in threat detection rules and hunts.

## Validation
1. In the Microsoft Defender portal, navigate to Hunting > Advanced hunting. 2. Run the following KQL query to confirm the unified IdentityInfo table is in use: `IdentityInfo | take 10`. 3. Compare the schema by running: `IdentityInfo | getschema`. 4. Verify that all expected UEBA fields (e.g., AccountUPN, IsAccountEnabled, GroupMembership, etc.) are present. 5. Check the 'Compare to unified schema' tab in the UEBA configuration blade to ensure no critical fields are missing for your detection rules.

## Rollback
1. If the unified IdentityInfo table causes query failures or missing data, contact Microsoft Support to request a rollback to the previous Log Analytics version of the IdentityInfo table. 2. As a temporary workaround, modify affected detection rules to use the Log Analytics table directly by specifying the workspace ID in the query (e.g., `union workspace('your-workspace-id').IdentityInfo`). 3. Update any saved hunts or analytics rules that reference the old schema to align with the new unified schema until a permanent rollback is completed.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/ueba-enrichments>
