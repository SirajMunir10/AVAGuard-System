# Optimization: Advanced Hunting

**Domain:** Defender for Endpoint
**Subdomain:** Advanced Hunting
**Incident Type:** Optimization

## Scenario / Query
How to optimize advanced hunting queries to avoid hitting service limits?

## Environment Context
- **Tenant Type:** Defender XDR
- **Configuration:** Advanced hunting quotas and usage parameters

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Apply optimization best practices to minimize disruptions
2. Be mindful of quotas and usage parameters if regularly running multiple queries

## Validation
1. Run a test advanced hunting query that previously hit service limits and confirm it completes without errors. 2. Check the current usage against quotas by running the Kusto query: 'Usage | where Timestamp > ago(1h) | summarize sum(Quantity) by DataType' in the advanced hunting console. 3. Verify that the query execution time and result size are within acceptable thresholds by reviewing the query statistics pane. 4. Confirm that no 'Too many requests' or 'Query execution timeout' errors appear in the last 24 hours via the Microsoft 365 Defender portal under 'Advanced hunting > Query history'.

## Rollback
1. If optimization changes caused query failures, revert to the previous query version using the query history in the advanced hunting console. 2. If quotas were adjusted, restore the original quota limits by contacting Microsoft support or using the appropriate PowerShell cmdlet (e.g., Set-MtpAdvancedHuntingQuota). 3. If query performance degraded, disable any newly applied filters or time range restrictions and re-run the original query. 4. Monitor the 'Advanced hunting > Usage and quotas' page to ensure no service limits are exceeded after rollback.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-overview>
