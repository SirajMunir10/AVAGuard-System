# Troubleshooting: Advanced Hunting

**Domain:** Defender for Endpoint
**Subdomain:** Advanced Hunting
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot advanced hunting queries that fail due to service limits or quotas?

## Environment Context
- **Tenant Type:** Defender XDR
- **Configuration:** Advanced hunting quotas and usage parameters

## Symptoms
- Query does not complete within 10 minutes and service displays an error
- Portal displays a warning when tenant consumes over 10% of allocated CPU resources
- Queries are blocked when tenant reaches 100% CPU resource allocation
- Query results are partial due to size constraints exceeding 64 MB

## Error Codes
N/A

## Root Causes
1. Query exceeds 10-minute runtime limit
2. Tenant consumes over 10% of allocated CPU resources
3. Tenant reaches 100% of allocated CPU resources
4. Query result exceeds 64 MB size limit

## Remediation Steps
1. Apply optimization best practices to minimize disruptions
2. Be mindful of quotas and usage parameters if regularly running multiple queries
3. For queries over Microsoft Sentinel tables, ensure Log Analytics workspace limits are considered

## Validation
1. Run a test advanced hunting query that previously failed due to the 10-minute runtime limit and confirm it completes within the timeout. 2. Check the tenant's current CPU resource consumption in the Defender portal (Advanced Hunting > Quotas) and verify it is below 10%. 3. Attempt a query that previously returned partial results due to the 64 MB size limit and confirm the full result set is returned. 4. Review the advanced hunting quotas and usage parameters page to ensure no warnings or blocks are active.

## Rollback
1. If a test query still fails due to runtime limits, revert to the original query structure and apply optimization best practices (e.g., reduce time range, filter columns). 2. If CPU consumption remains above 10%, reduce the frequency or complexity of concurrent queries until consumption drops. 3. If queries are still blocked due to 100% CPU allocation, wait for the quota reset period or reduce query load. 4. If partial results persist, adjust the query to limit output columns or use aggregation to stay under 64 MB.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-overview>
