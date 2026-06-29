# Implementation: Threat Hunting

**Domain:** Sentinel
**Subdomain:** Threat Hunting
**Incident Type:** Implementation

## Scenario / Query
How to conduct end-to-end proactive threat hunting in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace with hunting enabled (preview)

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Define a hypothesis from the MITRE map, recent hunting query results, content hub solutions, or generate custom hunts.
2. Go to the Hunting page Queries tab, select queries related to your hypothesis, and select New hunt.
3. Run hunt related queries and investigate results using the logs experience.
4. Bookmark results directly to your hunt to annotate findings, extract entity identifiers, and preserve relevant queries.
5. Investigate deeper using UEBA entity pages and run entity specific playbooks on bookmarked entities.
6. Use built-in actions to create new analytic rules, threat indicators, and incidents based on findings.
7. Record hunt results, track hypothesis validation, leave detailed notes in comments, and track overall impact with the metric bar.

## Validation
1. Navigate to Microsoft Sentinel > Threat Management > Hunting. 2. Confirm the new hunt appears in the list with the correct hypothesis and associated queries. 3. Run each query in the hunt and verify results are returned without errors. 4. Check that bookmarks are created and contain the expected annotations, entity identifiers, and queries. 5. Open a bookmarked entity’s UEBA page and confirm it loads correctly. 6. Verify that any new analytic rules, threat indicators, or incidents created from the hunt are present and active. 7. Review the hunt’s comments and metric bar to ensure notes and impact data are recorded.

## Rollback
1. Delete any analytic rules created from the hunt by going to Analytics > Active rules, selecting the rule, and clicking Delete. 2. Remove any threat indicators created from the hunt by going to Threat Intelligence > Indicators, selecting the indicators, and clicking Remove. 3. Close or delete any incidents created from the hunt by going to Incidents, selecting the incident, and choosing Close or Delete. 4. Delete bookmarks from the hunt by going to Hunting > Bookmarks, selecting the bookmarks, and clicking Delete. 5. Delete the hunt itself by going to Hunting > Hunts, selecting the hunt, and clicking Delete.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/hunting>
