# Troubleshooting: Hunting

**Domain:** Sentinel
**Subdomain:** Hunting
**Incident Type:** Troubleshooting

## Scenario / Query
How do I identify hunting queries that are not active in my environment due to missing data sources?

## Environment Context
- **Tenant Type:** Microsoft Sentinel in Defender
- **Configuration:** Hunting > Queries tab

## Symptoms
- Queries show N/A in the Results filter.

## Error Codes
N/A

## Root Causes
1. Required data sources are not connected.

## Remediation Steps
1. Select N/A in the Results filter to view queries that aren't at all active in your environment.
2. Hover over the info icon (i) next to the N/A to see which data sources are required to make this query active.
3. Follow recommendations on how to enable these queries.

## Validation
1. In Microsoft Sentinel, navigate to the Hunting > Queries tab. 2. In the Results filter, select 'N/A' to display queries that are not active. 3. For each query listed, hover over the info icon (i) next to 'N/A' and confirm that the required data sources are now listed as connected or available. 4. Run a sample query that previously showed 'N/A' and verify it returns results. 5. Check the 'Data connectors' page to ensure all required data sources show a connected status.

## Rollback
1. If the remediation causes issues, disconnect any newly connected data sources that were added. 2. In the Hunting > Queries tab, re-select 'N/A' in the Results filter to confirm the queries return to inactive status. 3. Verify that no unintended data ingestion or alerting changes occurred by reviewing the 'Data connectors' page and the 'Analytics' rule status. 4. If needed, restore previous data connector configurations from backup or documentation.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/hunting>
