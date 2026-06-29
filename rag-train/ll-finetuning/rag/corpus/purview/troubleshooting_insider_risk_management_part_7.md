# Troubleshooting: Insider Risk Management

**Domain:** Purview
**Subdomain:** Insider Risk Management
**Incident Type:** Troubleshooting

## Scenario / Query
How to review case activity details associated with risk alerts in the Activity explorer?

## Environment Context
- **Tenant Type:** Microsoft 365 E5/A5/G5
- **Configuration:** Insider Risk Management enabled

## Symptoms
- Risk analysts and investigators need to review case activity details associated with risk alerts
- Need to examine timeline of detected potentially risky activity

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to the Activity explorer tab in the case management interface
2. Use the timeline to review detected potentially risky activity
3. Apply filters to identify and filter all risk activities associated with alerts

## Validation
1. Navigate to the Microsoft Purview compliance portal (https://compliance.microsoft.com).
2. Go to Insider Risk Management > Cases.
3. Select the specific case you want to review.
4. Click the 'Activity explorer' tab.
5. Verify that the timeline displays detected potentially risky activities associated with the case alerts.
6. Apply filters (e.g., date range, activity type, user) to narrow down the activities and confirm that the filtered results match the expected risk alerts.
7. Confirm that each activity entry includes details such as activity type, date/time, user, and associated alert.

## Rollback
1. If the Activity explorer does not load or shows incorrect data, clear the browser cache and cookies, then reload the Microsoft Purview compliance portal.
2. Ensure the user has the necessary permissions (e.g., Insider Risk Management role) to view case activity details.
3. If filters are applied incorrectly, reset all filters by clicking 'Clear filters' or reloading the Activity explorer tab.
4. If the timeline is missing expected activities, verify that the case is correctly associated with the risk alerts and that the alerts are not in a 'Dismissed' or 'Resolved' state.
5. As a last resort, re-navigate to the case from the Cases list and re-open the Activity explorer tab.

## References
- <https://learn.microsoft.com/en-us/purview/insider-risk-management-cases>
