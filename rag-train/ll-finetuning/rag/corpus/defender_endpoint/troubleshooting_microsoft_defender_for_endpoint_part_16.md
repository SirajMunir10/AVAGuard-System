# Troubleshooting: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Troubleshooting

## Scenario / Query
How to review automatically investigated evidence for a Defender for Endpoint incident?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Microsoft Defender for Endpoint incident investigation

## Symptoms
- Incident alerts contain suspicious entities that need review
- Entities are marked as infected, remediated, or suspicious

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Go through the evidence Microsoft Defender for Endpoint automatically investigates all the incidents' supported events and suspicious entities in the alerts
2. Review autoresponse and information about the important files, processes, services, and more
3. Check each analyzed entity marked as infected, remediated, or suspicious

## Validation
1. Open the Microsoft 365 Defender portal (https://security.microsoft.com).
2. Navigate to Incidents & alerts > Incidents.
3. Select the incident you want to review.
4. In the incident details pane, click the Evidence & Response tab.
5. Verify that the list of automatically investigated evidence is displayed, including entities such as files, processes, services, IP addresses, and URLs.
6. For each entity, confirm that the investigation status (e.g., Infected, Remediated, Suspicious) is shown and matches the expected outcome based on the alert details.
7. Click on any entity to view its detailed investigation card, which includes the verdict, remediation actions taken, and supporting evidence.
8. Ensure that the evidence timeline shows the sequence of automated investigation steps and any manual actions taken.

## Rollback
1. If the automatically investigated evidence is missing or incorrect, first verify that the incident is still active and not closed.
2. In the Evidence & Response tab, click the 'Run investigation' button to trigger a new automated investigation on the incident.
3. If an entity was incorrectly marked as 'Remediated' but should be 'Suspicious', manually change the entity's status by selecting it and choosing 'Mark as suspicious' from the action menu.
4. If an entity was incorrectly marked as 'Infected' and needs to be cleared, select the entity and choose 'Mark as clean' (if available) or 'Add indicator' to create a custom indicator to allow the entity.
5. For any remediation action that was automatically applied (e.g., file quarantine), you can reverse it by going to the Action center, finding the action, and selecting 'Undo'.
6. If the entire investigation needs to be reset, contact Microsoft Support to request a reset of the incident's investigation state (no self-service option exists).

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/investigate-incidents>
