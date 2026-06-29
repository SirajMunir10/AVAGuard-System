# Troubleshooting: Incident Investigation

**Domain:** Defender for Endpoint
**Subdomain:** Incident Investigation
**Incident Type:** Troubleshooting

## Scenario / Query
How do I filter and focus the incident graph in Microsoft Defender XDR to simplify complex incidents with many alerts and entities?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Very large incidents with many alerts and entities
- Complex incident graph that is difficult to navigate

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select Add filter above the incident graph.
2. Choose any of the following available filter criteria, and then select Add: Severity (Display high-, medium-, or low-severity alerts), Status (Display new, in progress, or resolved alerts), Service sources (Display alerts from specific services, such as Microsoft Defender for Endpoint, Microsoft Defender for Identity, Microsoft Defender for Office 365, and others).
3. For each added filter criteria, choose the items you want to filter, and then select Apply.
4. If all entities are filtered out, an empty state message appears. Adjust your filters to see relevant entities.
5. To hide specific entity types: Select Entity types above the incident graph.
6. Uncheck the entity types you want to hide, such as file or user. The graph redraws itself without these entities.

## Validation
1. Open the incident graph for a complex incident in Microsoft Defender XDR. 2. Confirm that the 'Add filter' option is visible above the graph. 3. Add a filter for Severity = High and apply it. Verify that only high-severity alerts are displayed in the graph. 4. Add a filter for Status = New and apply it. Verify that only new alerts are shown. 5. Add a filter for Service sources = Microsoft Defender for Endpoint and apply it. Verify that only alerts from that service appear. 6. Remove all filters and confirm the graph returns to its original state. 7. Click 'Entity types' above the graph, uncheck 'File', and apply. Verify that file entities are hidden from the graph. 8. Re-check 'File' and confirm it reappears.

## Rollback
1. To remove a filter: Click the 'X' next to the filter criteria in the filter bar above the graph. 2. To remove all filters: Clear each filter individually or refresh the incident page to reset the graph to its default view. 3. To restore hidden entity types: Click 'Entity types' above the graph, re-check any unchecked entity types (e.g., file, user), and apply. The graph will redraw with all entity types visible.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-incidents>
