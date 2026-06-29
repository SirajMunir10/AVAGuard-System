# Troubleshooting: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Troubleshooting

## Scenario / Query
What to do when an error is displayed because the selected date range is greater than 180 days in audit log search?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** Maximum date range is 180 days

## Symptoms
- Error displayed if selected date range is greater than 180 days
- Error saying that the start date is earlier than the end date if using maximum date range of 180 days without selecting current time for Start date

## Error Codes
N/A

## Root Causes
1. Selected date range exceeds the maximum allowed 180 days
2. Start date is earlier than end date when using maximum date range of 180 days

## Remediation Steps
1. Select a date and time range within 180 days
2. If using the maximum date range of 180 days, select the current time for the Start date

## Validation
1. Open the Microsoft Purview compliance portal and navigate to Audit > Audit log search. 2. Set the Start date to a date exactly 180 days before today and the End date to today. 3. Click Search and confirm no error is displayed. 4. Set the Start date to the current time and the End date to 180 days from now (if allowed) or to a date within 180 days; verify no error about start date being earlier than end date appears. 5. Attempt a search with a date range of 181 days and confirm the expected error message is shown.

## Rollback
1. If the validation fails (e.g., error persists), revert to the original date range that caused the issue. 2. Clear any custom date filters and use the default date range (e.g., last 7 days). 3. If the error is due to a misconfigured time zone, reset the time zone to the tenant default in the audit log search settings. 4. If the issue is related to a browser cache or session, clear the browser cache and cookies, then restart the session. 5. Contact Microsoft support if the error continues after reverting to default settings.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-search>
