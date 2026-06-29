# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to use the Alert Triage Agent in Microsoft Purview DLP to triage alerts?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Microsoft Purview portal with appropriate permissions for Data Loss Prevention

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Sign in to the Microsoft Purview portal > Data loss prevention with appropriate permissions, see Permissions and Roles or Permissions and Roles depending on the workload you are working with.
2. Select Alerts to view the DLP Alerts dashboard.
3. Set the Alerts page view toggle to Alert Triage Agent.
4. Choose the category (All, Needs attention, Less urgent, or Not categorized) to see the alerts that are relevant to your task.
5. Select the triaged alert to view the Agent summary, an Overview, and Events associated with the alert.
6. After you review the summary, you can select Manage alert to assign it to an analyst, change the status of the alert or add more comments.

## Validation
1. Sign in to the Microsoft Purview portal (https://purview.microsoft.com) with appropriate permissions (e.g., DLP Compliance Management, Information Protection Admin, or Security Admin).
2. Navigate to Data loss prevention > Alerts.
3. Confirm the Alerts page view toggle is set to 'Alert Triage Agent'.
4. Verify that the category filter (All, Needs attention, Less urgent, Not categorized) displays alerts as expected.
5. Select a triaged alert and confirm the Agent summary, Overview, and Events tabs are populated.
6. Click 'Manage alert' and verify that you can assign the alert to an analyst, change its status, or add comments.

## Rollback
1. If the Alert Triage Agent view is not functioning as expected, toggle the Alerts page view back to the default view (e.g., 'Standard' or 'Classic') by selecting the appropriate option.
2. If alerts are missing or incorrectly categorized, refresh the Alerts dashboard or wait up to 24 hours for alert processing to complete.
3. If permissions are insufficient, verify role assignments in Microsoft Purview compliance portal > Roles & scopes, and assign the required DLP roles (e.g., DLP Compliance Management) to the affected user.
4. If the 'Manage alert' action fails, ensure the user has the 'Manage alerts' permission; otherwise, remove and re-add the user to the appropriate role group.
5. If the issue persists, clear browser cache or use an InPrivate/Incognito session to rule out session-related problems.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-learn>
