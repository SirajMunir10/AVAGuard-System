# Implementation: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Implementation

## Scenario / Query
How to search for Windows 365 Customer Lockbox activities in the Microsoft 365 audit log?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select Windows365CustomerLockbox under Record types.
2. Use the date range boxes and the Users list to narrow the search results.

## Validation
1. Go to Microsoft Purview compliance portal > Audit solutions > Audit. 2. Under Record type, select Windows365CustomerLockbox. 3. Set the date range to cover the period of interest. 4. Optionally, specify users in the Users list. 5. Click Search. 6. Confirm that audit records for Windows 365 Customer Lockbox activities appear in the results.

## Rollback
1. In the Audit search page, change the Record type back to the previous selection (e.g., Exchange, SharePoint, or All). 2. Clear any date range or user filters if they were modified. 3. Click Search to revert to the original audit log view. 4. If the search was part of a script or automated process, restore the original Record type parameter and filter values.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
