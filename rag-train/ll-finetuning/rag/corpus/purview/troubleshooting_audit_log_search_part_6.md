# Troubleshooting: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Troubleshooting

## Scenario / Query
How to search for audited activities using exact operation names in Microsoft Purview audit log search?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Purview Audit Log Search

## Symptoms
- No results returned when searching for audited activities
- Operation names entered incorrectly in search field

## Error Codes
N/A

## Root Causes
1. Operation names must be entered exactly as they are named; if entered incorrectly, no results are returned

## Remediation Steps
1. Review the audit activities article to find the exact operation name for the activities you want to search for
2. Enter one or more operation names, separated by commas, in the operation search field
3. Copy and paste the operation names directly from the article to the operation search field to ensure they're entered correctly and without typos

## Validation
1. Navigate to Microsoft Purview compliance portal > Audit > Audit log search. 2. In the 'Activities' dropdown, select 'Show operations for all activities'. 3. In the 'Operation' search field, enter the exact operation name(s) from the official list (e.g., 'MailboxLogin', 'UserLoggedIn'). 4. Set a date range that covers the expected activity period. 5. Click 'Search'. 6. Confirm that audit log entries matching the specified operation names are returned. 7. If no results appear, verify the operation name spelling and that the activity occurred within the selected date range.

## Rollback
1. If the remediation causes unexpected results (e.g., too many or irrelevant entries), clear the 'Operation' field. 2. Revert to using the 'Activities' dropdown to select a predefined activity group (e.g., 'Exchange mailbox activities'). 3. Adjust the date range or other filters as needed. 4. Click 'Search' to return to the previous search behavior. 5. If the issue persists, refer to the official documentation at https://learn.microsoft.com/en-us/purview/audit-log-search for further guidance.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-search>
