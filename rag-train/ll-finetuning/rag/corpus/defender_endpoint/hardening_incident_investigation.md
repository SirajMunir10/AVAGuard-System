# Hardening: Incident Investigation

**Domain:** Defender for Endpoint
**Subdomain:** Incident Investigation
**Incident Type:** Hardening

## Scenario / Query
How can security analysts use blast radius analysis to contain an incident?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** Blast radius analysis enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use blast radius analysis to investigate an incident.
2. Instantly see the compromised component at the center of the graph and the paths to potentially compromised targets.
3. Based on the target and paths, escalate and trigger actions to disrupt, isolate, and contain the incident on nodes along the paths to the target.

## Validation
1. Open the Microsoft Defender XDR portal (https://security.microsoft.com).
2. Navigate to Incidents & alerts > Incidents.
3. Select the incident under investigation.
4. Click the 'Blast radius' tab to open the blast radius graph.
5. Verify that the compromised component is displayed at the center of the graph.
6. Confirm that paths to potentially compromised targets are visible.
7. Ensure that actions to disrupt, isolate, and contain the incident (e.g., isolate device, block file) are available on nodes along the paths.
8. Execute a containment action (e.g., isolate device) on a node and confirm the action is queued or completed successfully.

## Rollback
1. If the containment action was applied incorrectly, navigate to the action center in the Microsoft Defender XDR portal.
2. Locate the pending or completed action (e.g., device isolation).
3. For device isolation, select the action and choose 'Release from isolation' to revert the containment.
4. For file blocking, remove the block by deleting the indicator from the Indicators settings.
5. Verify the device or file is restored to its previous state by checking the device health or file access.
6. If the blast radius analysis was not helpful, continue manual investigation using the incident timeline and other investigation tools.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-incidents>
