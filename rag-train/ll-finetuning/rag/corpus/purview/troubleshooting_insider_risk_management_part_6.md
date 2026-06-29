# Troubleshooting: Insider Risk Management

**Domain:** Purview
**Subdomain:** Insider Risk Management
**Incident Type:** Troubleshooting

## Scenario / Query
How do risk analysts and investigators review user activity details for insider risk cases?

## Environment Context
- **Tenant Type:** Microsoft 365 E5/A5/G5
- **Configuration:** Insider Risk Management enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to the User activity tab in the case details.
2. Review the visual representation of potentially risky activities associated with risk alerts and cases.
3. Use the bubble chart to understand the overall scope of risk activities.

## Validation
1. Navigate to Microsoft Purview compliance portal > Insider Risk Management > Cases. 2. Open a specific case and select the 'User activity' tab. 3. Confirm that the bubble chart displays activities associated with risk alerts. 4. Verify that hovering over a bubble shows details such as activity type, date, and risk score. 5. Ensure that filtering by date range or activity type updates the chart accordingly.

## Rollback
1. If the 'User activity' tab is missing or empty, verify that the user has the 'Insider Risk Management Analyst' or 'Insider Risk Management Investigator' role. 2. Check that the case is active and contains risk alerts. 3. If the bubble chart fails to load, clear browser cache and retry. 4. If issues persist, re-enable Insider Risk Management in the tenant settings and wait 24 hours for data to repopulate.

## References
- <https://learn.microsoft.com/en-us/purview/insider-risk-management-cases>
