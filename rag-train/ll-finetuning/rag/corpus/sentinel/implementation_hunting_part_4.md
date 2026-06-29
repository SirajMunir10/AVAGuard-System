# Implementation: Hunting

**Domain:** Sentinel
**Subdomain:** Hunting
**Incident Type:** Implementation

## Scenario / Query
How do I view hunting queries mapped to MITRE ATT&CK tactics and techniques?

## Environment Context
- **Tenant Type:** Microsoft Sentinel in Defender
- **Configuration:** Hunting > Queries tab

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the MITRE ATT&CK tactic bar at the top of the table to see how many queries are mapped to each tactic.
2. Filter or sort by MITRE ATT&CK techniques using the Technique filter.
3. Open a query and select the technique to see the MITRE ATT&CK description of the technique.

## Validation
1. In the Microsoft Sentinel (in Defender) portal, navigate to Hunting > Queries tab. 2. Observe the MITRE ATT&CK tactic bar at the top of the table; confirm that the bar displays the count of queries mapped to each tactic. 3. Apply a filter by MITRE ATT&CK technique using the Technique filter; verify that the query list updates to show only queries associated with the selected technique. 4. Open any query and select the technique link; confirm that the MITRE ATT&CK description of the technique is displayed.

## Rollback
1. Remove any applied MITRE ATT&CK technique filter by clearing the Technique filter field. 2. If the tactic bar is not visible, refresh the page or navigate away and back to Hunting > Queries tab. 3. No other rollback actions are required as viewing and filtering queries does not change any configuration or data.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/hunting>
