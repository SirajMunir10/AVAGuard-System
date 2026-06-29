# Troubleshooting: Microsoft Defender XDR

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender XDR
**Incident Type:** Troubleshooting

## Scenario / Query
How to filter alerts in the Microsoft Defender portal to narrow down the list of alerts?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** Default alerts queue shows new and in progress alerts from last seven days

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select Filter from the default alerts queue to see all available filters.
2. Filter alerts according to criteria: Service/detection sources, Policy/Policy rule, Product name, Alert subscription ID, Entities (the impacted assets), Automated investigation state, Data stream (workload or location), Sensitivity label.

## Validation
1. Open the Microsoft Defender portal (https://security.microsoft.com).
2. Navigate to Incidents & alerts > Alerts to view the default alerts queue.
3. Click the 'Filter' button above the alerts list.
4. Verify that the filter panel displays all available filter options: Service/detection sources, Policy/Policy rule, Product name, Alert subscription ID, Entities, Automated investigation state, Data stream, and Sensitivity label.
5. Apply one or more filters (e.g., select a specific Service/detection source and a date range).
6. Confirm that the alerts list updates to show only alerts matching the selected criteria.
7. Remove all filters and verify the queue returns to the default view (new and in progress alerts from the last seven days).

## Rollback
1. In the Microsoft Defender portal, navigate to Incidents & alerts > Alerts.
2. Click the 'Filter' button to open the filter panel.
3. Click 'Clear filters' to remove all applied filters.
4. Verify the alerts queue resets to the default view showing new and in progress alerts from the last seven days.
5. If the filter panel does not appear or the queue does not reset, refresh the browser page or sign out and sign back in to the portal.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts>
