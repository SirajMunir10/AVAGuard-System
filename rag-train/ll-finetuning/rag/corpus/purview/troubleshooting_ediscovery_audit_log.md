# Troubleshooting: eDiscovery Audit Log

**Domain:** Purview
**Subdomain:** eDiscovery Audit Log
**Incident Type:** Troubleshooting

## Scenario / Query
How to interpret detailed properties in eDiscovery audit log records when searching the audit log?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log search enabled

## Symptoms
- Audit log records for eDiscovery activities do not include every detailed property listed in documentation
- CSV export contains a column named AuditData with multivalue properties

## Error Codes
N/A

## Root Causes
1. Audit log record for an eDiscovery activity does not include every detailed property listed in the table

## Remediation Steps
1. Export the audit log search results to a CSV file
2. Use the Power Query feature in Excel to split the AuditData column into multiple columns so each property has its own column
3. Sort and filter on one or more of these properties

## Validation
1. Export the audit log search results to a CSV file. 2. Open the CSV in Excel and use Power Query to split the AuditData column into separate columns. 3. Verify that the detailed properties (e.g., Operation, Workload, ObjectId, etc.) appear in individual columns and match the expected values from the documentation at https://learn.microsoft.com/en-us/purview/audit-log-activities.

## Rollback
1. Delete the modified CSV file or revert to the original exported CSV. 2. If Power Query transformations were saved, remove those query steps. 3. Re-export the audit log search results to a fresh CSV file without any splitting or filtering.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
