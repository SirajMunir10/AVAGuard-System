# Troubleshooting: UEBA

**Domain:** Sentinel
**Subdomain:** UEBA
**Incident Type:** Troubleshooting

## Scenario / Query
Why is the IdentityInfo table not updating after changes to user profiles, groups, or built-in roles in Microsoft Entra ID?

## Environment Context
- **Tenant Type:** Microsoft Sentinel workspace with UEBA enabled
- **Configuration:** IdentityInfo table synchronization from Microsoft Entra ID

## Symptoms
- Changes to user attributes (display name, job title, email address) are not reflected in the IdentityInfo table.
- Group membership changes are not updated in the IdentityInfo table.
- Group renames do not appear in the IdentityInfo table.

## Error Codes
N/A

## Root Causes
1. Initial synchronization may take a few days.
2. Regular full resynchronization occurs every 14 days.
3. Incremental updates for changes occur within 15-30 minutes.

## Remediation Steps
1. Wait for the initial synchronization to complete (may take a few days).
2. Verify that changes to user profiles, groups, and built-in roles in Microsoft Entra ID are made and wait 15-30 minutes for reingestion.
3. Check that the IdentityInfo table is being queried in analytics rules, hunting queries, or workbooks.

## Validation
Query the IdentityInfo table in Log Analytics to confirm updated records.

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/ueba-enrichments>
