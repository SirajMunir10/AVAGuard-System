# Troubleshooting: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to detect when an admin removes themselves from a user's OneDrive site collection administrators list?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log search enabled

## Symptoms
- Admin removed from site collection administrators for a user's OneDrive account

## Error Codes
N/A

## Root Causes
1. Admin edited the user profile in the SharePoint admin center

## Remediation Steps
1. Search for all activities in the audit log
2. Look for the activity 'Removed user or group from SharePoint group' with the operation 'RemovedFromGroup'

## Validation
1. Go to Microsoft Purview compliance portal > Audit > Search. 2. Set 'Activities' to 'Removed user or group from SharePoint group' and 'Start date' to the time of the incident. 3. Run the search and verify that an entry with Operation 'RemovedFromGroup' appears, showing the admin as the user who performed the removal and the affected OneDrive site collection. 4. Confirm the 'Item' field contains the OneDrive URL and the 'Target' field shows the admin's user principal name.

## Rollback
1. In SharePoint admin center, go to Active sites > select the affected user's OneDrive site. 2. Click 'Permissions' > 'Site collection administrators'. 3. Add the admin's user principal name back to the list. 4. Verify the admin can access the site by navigating to the OneDrive URL. 5. Optionally, run the audit log search again to confirm a 'Added user or group to SharePoint group' activity appears.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
