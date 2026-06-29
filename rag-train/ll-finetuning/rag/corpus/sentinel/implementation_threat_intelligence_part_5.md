# Implementation: Threat Intelligence

**Domain:** Sentinel
**Subdomain:** Threat Intelligence
**Incident Type:** Implementation

## Scenario / Query
How do I curate threat intelligence by connecting TI objects using the relationship builder in Microsoft Sentinel?

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
1. Select Add new > TI relationship.
2. Start with an existing TI object like a threat actor or attack pattern where the single object connects to one or more existing objects, like indicators.
3. Add the relationship type according to the best practices outlined in the STIX 2.1 reference relationship summary table.
4. Complete the relationship by configuring Common properties.

## Validation
1. In the Microsoft Sentinel portal, navigate to Threat Intelligence > Threat intelligence. 2. Select the TI object you created or modified (e.g., a threat actor). 3. In the details pane, verify that the 'Relationships' tab lists the connected objects (e.g., indicators) with the correct relationship type (e.g., 'uses', 'indicates'). 4. Click on the relationship to confirm the Common properties (e.g., description, confidence) are populated as configured. 5. Optionally, run the following KQL query in the Sentinel Logs workspace to confirm the relationship exists in the ThreatIntelligenceIndicator table: ThreatIntelligenceIndicator | where Relationships contains '<relationship_type>' and Relationships contains '<target_object_id>'.

## Rollback
1. In the Microsoft Sentinel portal, navigate to Threat Intelligence > Threat intelligence. 2. Select the TI object that has the relationship you want to remove. 3. In the details pane, go to the 'Relationships' tab. 4. Locate the relationship you added, click the ellipsis (three dots) next to it, and select 'Delete relationship'. 5. Confirm the deletion. 6. Verify the relationship is no longer listed in the 'Relationships' tab. 7. If the relationship was created as part of a new TI object, you can delete the entire TI object by selecting it and choosing 'Delete' from the command bar.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/work-with-threat-indicators>
