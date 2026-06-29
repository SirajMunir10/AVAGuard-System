# Optimization: Threat Intelligence

**Domain:** Sentinel
**Subdomain:** Threat Intelligence
**Incident Type:** Optimization

## Scenario / Query
How do I optimize threat intelligence ingestion from my sources using ingestion rules in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace with threat intelligence enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the management interface to search, filter and sort, then add tags to your threat intelligence.
2. Optimize TI from your sources with ingestion rules.
3. Curate existing TI with the relationship builder.

## Validation
1. In the Microsoft Sentinel workspace, navigate to Threat Intelligence > Threat intelligence (Preview).
2. Use the search, filter, and sort options to confirm that the expected threat indicators are visible and correctly tagged.
3. Check the ingestion rules by going to Threat Intelligence > Ingestion rules. Verify that the rules are enabled and applied to the correct sources.
4. Review the relationship builder by selecting an indicator and clicking 'Relationships' to ensure relationships are properly curated.
5. Run the following KQL query to confirm indicators are being ingested: ThreatIntelligenceIndicator | where TimeGenerated > ago(1h) | summarize count() by SourceSystem

## Rollback
1. To revert tagging changes, use the Threat intelligence (Preview) blade to remove tags from indicators that were added during remediation.
2. Disable or delete any ingestion rules created or modified by navigating to Threat Intelligence > Ingestion rules, selecting the rule, and choosing 'Disable' or 'Delete'.
3. If the relationship builder was used, remove any relationships added by editing the indicator and deleting the relationship entries.
4. If indicators were incorrectly filtered or sorted, reset the view to default by refreshing the page or clearing filters.
5. Monitor ingestion health by checking the ThreatIntelligenceIndicator table for any drop in data volume using the same KQL query from validation.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/work-with-threat-indicators>
