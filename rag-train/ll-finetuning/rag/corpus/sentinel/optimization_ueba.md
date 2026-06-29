# Optimization: UEBA

**Domain:** Sentinel
**Subdomain:** UEBA
**Incident Type:** Optimization

## Scenario / Query
How to reduce false positives in analytics rules by using the IdentityInfo table?

## Environment Context
- **Tenant Type:** Microsoft Sentinel workspace with UEBA enabled
- **Configuration:** IdentityInfo table populated with user data from Microsoft Entra ID or Active Directory

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Query the IdentityInfo table in analytics rules, hunting queries, and workbooks.
2. Enhance analytics to fit your use cases using the IdentityInfo table data.

## Validation
1. In the Microsoft Sentinel workspace, navigate to Logs and run: IdentityInfo | take 10. Confirm that the table returns rows with user data (e.g., AccountName, AccountUPN, GroupMembership).
2. Open an existing analytics rule that uses the IdentityInfo table (e.g., a rule referencing IdentityInfo in its query). Click 'Test with current data' and verify that the rule runs without errors and returns expected results.
3. In a hunting query or workbook that references IdentityInfo, execute the query and confirm that the output includes enriched user details (e.g., JobTitle, Department, Manager).
4. Check the UEBA settings in Sentinel: ensure 'IdentityInfo table populated' status shows 'Active' and the last sync time is recent.

## Rollback
1. If the IdentityInfo table is not populated or returns empty results, verify the UEBA configuration: in Sentinel, go to Entity Behavior > UEBA settings and confirm that 'Enable UEBA' is turned on and the data sources (Microsoft Entra ID or Active Directory) are correctly connected.
2. If an analytics rule using IdentityInfo fails, edit the rule and remove or comment out the reference to IdentityInfo in the query. Save the rule and re-enable it.
3. For hunting queries or workbooks that fail due to IdentityInfo, replace the IdentityInfo reference with a static list of user data or remove the enrichment logic until the table is repopulated.
4. If the IdentityInfo table is stale, trigger a manual sync: in UEBA settings, click 'Sync now' to force a refresh from Microsoft Entra ID or Active Directory.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/ueba-enrichments>
