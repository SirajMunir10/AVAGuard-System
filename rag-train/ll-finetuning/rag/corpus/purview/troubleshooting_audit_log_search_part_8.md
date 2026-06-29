# Troubleshooting: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Troubleshooting

## Scenario / Query
How to search for text containing special characters in Purview audit log?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Keyword search in audit log

## Symptoms
- Keyword search does not return expected results for text with special characters

## Error Codes
N/A

## Root Causes
1. Special characters in the keyword search are not handled correctly

## Remediation Steps
1. Replace the special characters with an asterisk (*) in your keyword search
2. For example, to search for test_search_document, use test*search*document

## Validation
1. Perform a keyword search in the Microsoft Purview compliance portal (https://compliance.microsoft.com) using the original query with special characters (e.g., test_search_document) and confirm no results are returned.
2. Perform a keyword search using the modified query with asterisks replacing special characters (e.g., test*search*document).
3. Verify that the modified query returns the expected audit log entries.
4. Optionally, run the Search-UnifiedAuditLog cmdlet in Exchange Online PowerShell with the modified keyword to confirm results: Search-UnifiedAuditLog -FreeText 'test*search*document'.

## Rollback
1. If the modified query does not return expected results, revert to the original keyword search (e.g., test_search_document).
2. Verify that the original query returns no results, confirming the issue persists.
3. If needed, contact Microsoft Support for further assistance with special character handling in audit log searches.
4. No configuration changes were made, so no additional rollback is required.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-search>
