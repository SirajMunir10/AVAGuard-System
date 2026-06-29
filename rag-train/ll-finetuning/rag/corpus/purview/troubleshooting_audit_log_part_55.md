# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to search for Viva Engage activities in the Microsoft 365 audit log?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit (Premium) licensing required for some activities

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select Show results for all activities in the Activities list.
2. Use the date range boxes and the Users list to narrow the search results.

## Validation
1. Navigate to Microsoft Purview compliance portal > Audit > Search. 2. In the Activities list, select 'Show results for all activities'. 3. Set the date range to cover the period of interest. 4. Optionally, specify a user in the Users list. 5. Click Search. 6. Verify that the search results include Viva Engage activities (e.g., 'Viva Engage activity' entries under the 'Viva Engage' group). 7. Confirm that the results display the expected activity details (date, user, activity, item).

## Rollback
1. If the search returns no Viva Engage activities, verify that Audit (Premium) licensing is assigned to the relevant users. 2. Ensure the date range is correct and not too narrow. 3. Clear the Users filter to search all users. 4. If still no results, check that Viva Engage is enabled in the tenant and that audit logging is turned on. 5. As a last resort, contact Microsoft Support for further investigation.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
