# Troubleshooting: Audit Log Search

**Domain:** Purview
**Subdomain:** Audit Log Search
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve an error when the selected date range exceeds 180 days in Purview audit log search?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log search date range configuration

## Symptoms
- An error is displayed if the selected date range is greater than 180 days
- An error saying that the start date is earlier than the end date when using maximum date range of 180 days

## Error Codes
N/A

## Root Causes
1. Selected date range exceeds the maximum allowed 180 days
2. Start date is not set to current time when using the maximum date range of 180 days
3. Auditing was turned on within the last 180 days and the date range starts before that date

## Remediation Steps
1. Select a date and time range that does not exceed 180 days
2. If using the maximum date range of 180 days, select the current time for the Start date
3. If auditing was turned on within the last 180 days, ensure the maximum date range does not start before the date auditing was turned on

## Validation
1. Open the Microsoft Purview compliance portal (https://compliance.microsoft.com).
2. Navigate to Audit > Audit log search.
3. Set the Start date to a value within the last 180 days (e.g., today's date minus 30 days) and the End date to today.
4. Click Search and confirm no error message appears.
5. Set the Start date to the current time and the End date to 180 days from now (maximum range).
6. Click Search and confirm no error about start date being earlier than end date.
7. If auditing was enabled less than 180 days ago, set the Start date to the exact date auditing was turned on and the End date to 180 days after that date. Click Search and confirm no error.

## Rollback
1. If the validation steps fail, revert to the original date range that caused the error.
2. If the error persists, ensure the date range does not exceed 180 days by reducing the range (e.g., set Start date to 30 days ago and End date to today).
3. If the error 'start date is earlier than end date' appears when using the maximum 180-day range, set the Start date to the current time and End date to 180 days from now.
4. If auditing was turned on within the last 180 days, set the Start date to the date auditing was enabled and End date to 180 days after that date.
5. If none of the above resolves the issue, contact Microsoft Support with the error details and the date range used.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-search>
