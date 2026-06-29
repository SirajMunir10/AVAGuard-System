# Troubleshooting: Self-Service Password Reset

**Domain:** Entra ID
**Subdomain:** Self-Service Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
Why do user registrations show multiple times in the SSPR registration report?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** Self-Service Password Reset enabled

## Symptoms
- User registrations appear multiple times in the registration report

## Error Codes
N/A

## Root Causes
1. Each individual piece of data registered is logged as a separate event

## Remediation Steps
1. Download the report
2. Open the data as a pivot table in Excel to aggregate and view it with greater flexibility

## Validation
1. Download the SSPR registration report from the Entra admin center (Identity > Monitoring & health > Audit logs > Filter by activity 'Self-service password reset registration').
2. Open the downloaded CSV in Excel and create a pivot table with 'User' in Rows and 'Activity' in Columns.
3. Verify that each user now appears only once per distinct registration activity (e.g., 'Authentication methods registered'), confirming that multiple rows per user are due to separate data registrations and not duplicate entries.

## Rollback
1. If the pivot table aggregation reveals unexpected duplicates (e.g., same user, same method, same timestamp), re-download the raw audit log CSV from the Entra admin center.
2. Compare the raw data with the pivot table to ensure no data corruption occurred during export or transformation.
3. If the issue persists, restore the previous report by re-running the audit log export without pivot table modifications.
4. Contact Microsoft Support if the raw audit log shows true duplicate events that cannot be explained by the documented behavior.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr>
