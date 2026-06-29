# Troubleshooting: Identity Investigation

**Domain:** Defender for Endpoint
**Subdomain:** Identity Investigation
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate a user's risk score in Microsoft Defender XDR using the Risk score tab?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Risk score tab (Preview)

## Symptoms
- Identity risk score displayed as 0â€“100
- Risk score compared to other identities by percentile
- Account sets linked to the identity
- Microsoft Entra ID risk level for each Microsoft Entra account

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to the Risk score tab in the user investigation view
2. Review the Risk Summary section for overall risk score and percentile comparison
3. Select the Microsoft Entra ID risk level to see timeline details
4. Review Likelihood of Compromise section for alert distribution by MITRE ATT&CK kill chain stage
5. Review Impact of Compromise section based on identity criticality, classification, and PIM role assignments
6. Use the line chart to see risk score changes over a configurable time period (e.g., 30 days)
7. Select Go to timeline to view the full activity timeline
8. Use the Active alerts only toggle to focus on unresolved alerts
9. Filter by account set, status, or kill chain stage
10. Select Reset risk at the top of the tab to manually reset the identity's risk score after completing remediation

## Validation
1. Navigate to the Microsoft 365 Defender portal (https://security.microsoft.com).
2. Go to Incidents & alerts > Incidents and select the relevant incident.
3. In the incident details, select the user entity under 'Users' or 'Assets'.
4. Click the 'Risk score (Preview)' tab.
5. Verify the 'Risk Summary' section displays a risk score between 0 and 100 and a percentile comparison.
6. Confirm that the 'Likelihood of Compromise' section shows alerts distributed by MITRE ATT&CK kill chain stages.
7. Confirm that the 'Impact of Compromise' section reflects identity criticality, classification, and PIM role assignments.
8. Adjust the time period in the line chart (e.g., 30 days) and verify the risk score trend updates.
9. Select 'Go to timeline' and confirm the full activity timeline loads.
10. Toggle 'Active alerts only' and verify only unresolved alerts are shown.
11. Apply filters by account set, status, or kill chain stage and confirm the list updates accordingly.
12. If remediation was performed, select 'Reset risk' and confirm the risk score resets to 0 or a baseline value.

## Rollback
1. If the risk score was manually reset using 'Reset risk', note that this action cannot be undone automatically. To restore the previous risk score, you must wait for Microsoft Entra ID Protection to recalculate the risk based on new signals or manually adjust risk policies.
2. If filters or time period changes were applied, simply clear all filters and reset the time period to the default (e.g., 30 days) to return to the default view.
3. If the 'Active alerts only' toggle was enabled, disable it to show all alerts again.
4. No other rollback steps are required as the Risk score tab is read-only except for the 'Reset risk' action. For any unintended changes to risk policies, refer to Microsoft Entra ID Protection documentation to reconfigure risk policies.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-users>
