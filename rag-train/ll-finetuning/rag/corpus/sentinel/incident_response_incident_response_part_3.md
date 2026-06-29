# Incident Response: Incident Response

**Domain:** Sentinel
**Subdomain:** Incident Response
**Incident Type:** Incident Response

## Scenario / Query
A security analyst in a Microsoft Sentinel environment needs to investigate a high-severity incident involving a suspicious sign-in from an unfamiliar location. The analyst wants to use the built-in investigation graph to pivot from the user entity to related alerts, bookmarks, and entities. How can the analyst open the investigation graph for the incident and what entities are automatically surfaced?

## Environment Context
- **Tenant Type:** Azure tenant with Microsoft Sentinel enabled
- **Configuration:** Sentinel workspace has at least one analytics rule generating incidents; user has Sentinel Reader or higher role.

## Symptoms
- High-severity incident appears in Sentinel with entity mapping to a user account
- Analyst needs to visually explore relationships between entities and alerts

## Error Codes
N/A

## Root Causes
1. Incident investigation requires pivoting on entities to find related activities
2. Built-in investigation graph provides a visual map of entities and connections

## Remediation Steps
1. Navigate to Microsoft Sentinel > Incidents and select the incident
2. Click 'Investigate' to open the investigation graph
3. The graph automatically displays the incident's mapped entities (e.g., user, IP address, device) and related alerts
4. Click on any entity node to expand and see additional connections, such as related bookmarks or hunting results
5. Use the graph to pivot to other entities and build a timeline of the attack

## Validation
Confirm that the investigation graph opens and shows entity nodes connected by lines representing relationships. Verify that clicking an entity reveals a menu with options to view related alerts, bookmarks, or run a hunting query.

## Rollback
Close the investigation graph pane to return to the incident details view.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/investigate-incidents>
