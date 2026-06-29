# Troubleshooting: Incident Investigation

**Domain:** Defender for Endpoint
**Subdomain:** Incident Investigation
**Incident Type:** Troubleshooting

## Scenario / Query
How to view the blast radius of an incident in Microsoft Defender XDR?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- No blast radius path found when selecting View blast radius from a node's context menu

## Error Codes
N/A

## Root Causes
1. Some nodes might not have paths associated with them
2. If no blast radius path is found, the menu item shows 'No blast radius found'

## Remediation Steps
1. Select an incident from the list in the Incidents page
2. In the graph view, select a node to open the context menu
3. Select View blast radius
4. If no blast radius path is found, the menu item shows 'No blast radius found'
5. To view the blast radius of a single node in a group, use the ungroup toggle above the grid to present all nodes
6. A new graph view loads showing the eight top-rated attack paths
7. Select View full blast radius list above the graph to see a full list of paths in the right side panel
8. From the list of reachable targets, select one to explore the path from the entry point to this target
9. Select View blast radius list to see a list of target assets
10. Select a target asset from the list to view its details and potential attack paths
11. Selecting the badges in connections shows more details about the connection
12. When paths lead to grouped targets of the same types, select the grouped icons to view discrete paths
13. A right-side panel opens showing all the targets in the group
14. Select the check box on the left and select the Expand button on top to display each target and its paths separately
15. Hide the blast radius graph and return to the original incident graph by selecting the node and choosing Hide blast radius

## Validation
1. Navigate to the Microsoft Defender XDR portal (https://security.microsoft.com).
2. Go to Incidents & alerts > Incidents.
3. Select an incident from the list.
4. In the incident graph view, select a node to open its context menu.
5. Confirm that 'View blast radius' is visible and selectable (not grayed out or showing 'No blast radius found').
6. Select 'View blast radius' and verify that a new graph loads showing the eight top-rated attack paths.
7. Select 'View full blast radius list' above the graph and confirm a list of paths appears in the right-side panel.
8. From the list of reachable targets, select one and verify the path from entry point to target is displayed.
9. Select 'View blast radius list' and confirm a list of target assets appears.
10. Select a target asset and verify its details and potential attack paths are shown.
11. If grouped targets exist, select the grouped icon, verify the right-side panel shows all targets, select the checkbox and 'Expand' button to display each target and its paths separately.
12. Select the node again and choose 'Hide blast radius' to confirm the graph returns to the original incident graph.

## Rollback
1. If the blast radius graph does not load correctly or shows unexpected results, select the node and choose 'Hide blast radius' to return to the original incident graph.
2. Refresh the incident page to reload the default graph view.
3. If the 'View blast radius' option is missing or shows 'No blast radius found', verify that the selected node is not a type that lacks associated paths (e.g., some nodes may not have blast radius paths).
4. Use the 'ungroup' toggle above the grid to present all nodes individually, then retry selecting a node and choosing 'View blast radius'.
5. If issues persist, clear browser cache and cookies, then reload the portal.
6. As a last resort, open a support ticket with Microsoft for further investigation.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-incidents>
