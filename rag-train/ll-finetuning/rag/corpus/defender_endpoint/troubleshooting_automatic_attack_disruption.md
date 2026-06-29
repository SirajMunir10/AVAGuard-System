# Troubleshooting: Automatic Attack Disruption

**Domain:** Defender for Endpoint
**Subdomain:** Automatic Attack Disruption
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify when an automatic attack disruption has occurred in the Microsoft Defender environment?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** Automatic attack disruption enabled

## Symptoms
- Yellow bar at the top of the incident page highlighting automatic action taken
- Dedicated disruption tag on the incident page
- Tag titled 'Attack Disruption' next to affected incidents in the incident queue
- Current asset status shown in the incident graph (e.g., account disabled or device contained)
- Policy status column in the Activities tab showing status of actions and policies relevant to the incident
- Incident title appended with '(attack disruption)' string via API

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. In the incident queue, look for a tag titled 'Attack Disruption' next to affected incidents
2. On the incident page, check for a tag titled 'Attack Disruption' and a yellow banner at the top highlighting the automatic action taken
3. In the incident graph, review the current asset status if an action is done on an asset (e.g., account disabled or device contained)
4. In the Activities tab, use the Policy status column (Preview) to view the current status of all actions and policies relevant to the incident
5. Filter by Provider: 'Attack disruption' and Policy status: 'Active', 'Inactive', 'No status' to view disruption policy statuses
6. Via API, check for the '(attack disruption)' string appended to the end of incident titles

## Validation
Verify the presence of the 'Attack Disruption' tag in the incident queue or on the incident page, and the yellow banner at the top of the incident page.

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption>
