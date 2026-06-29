# Implementation: Threat Intelligence

**Domain:** Sentinel
**Subdomain:** Threat Intelligence
**Incident Type:** Implementation

## Scenario / Query
How to find and view threat intelligence with queries in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure or Defender portal
- **Configuration:** ThreatIntelligenceIndicator table

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. For Microsoft Sentinel in the Defender portal, select Investigation & response > Hunting > Advanced hunting.
2. The ThreatIntelligenceIndicator table is located under the Microsoft Sentinel group.
3. For Microsoft Sentinel in the Azure portal, under General, select Logs.
4. Select the Preview data icon (the eye) next to the table name.
5. Select See in query editor to run a query that shows records from this table.

## Validation
1. In the Azure portal, navigate to Microsoft Sentinel > Logs. 2. In the query editor, run: ThreatIntelligenceIndicator | take 10. 3. Verify that records are returned. 4. In the Defender portal, go to Investigation & response > Hunting > Advanced hunting. 5. Run: ThreatIntelligenceIndicator | take 10. 6. Confirm results appear.

## Rollback
1. If the ThreatIntelligenceIndicator table is missing or empty, verify that threat intelligence connectors (e.g., TAXII, Threat Intelligence Platform) are enabled and sending data. 2. Check data ingestion by running: ThreatIntelligenceIndicator | where TimeGenerated > ago(1h). 3. If no data, re-enable the relevant connector in Microsoft Sentinel > Data connectors. 4. For query issues, reset the query editor by closing and reopening the Logs blade.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/work-with-threat-indicators>
