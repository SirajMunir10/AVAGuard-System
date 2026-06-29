# Troubleshooting: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Troubleshooting

## Scenario / Query
How do I investigate a DLP alert using the standard DLP Alerts dashboard in Microsoft Purview?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Standard DLP Alerts dashboard view

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Sign in to the Microsoft Purview portal > Data loss prevention.
2. Select Alerts to view the DLP Alerts dashboard.
3. Use the Filter fields to refine the list of alerts.
4. Choose Customize columns to list the properties you want to see.
5. To sort the results in ascending or descending order, double-click the column header.
6. Double-click an alert for more information about it.
7. The Details tab opens by default and provides high-level information about the alert.
8. Select Summarize with Copilot to generate a summary of the alert.
9. Select View details to open the Overview tab.
10. The Events tab lists all of the events associated with the alert. Select any event in the list to get detailed information about the event.
11. For each event, choose the Actions drop down for a list of actions you can take on the alert, such as verifying whether or not the alert has identified a true match or a false positive.
12. The User activity summary tab requires that sharing be turned On in the insider risk management settings. Once enabled, it provides all the exfiltration activities the user has engaged in (up to the past 120 days). Users must be in scope of an insider risk management policy to see the User activity summary tab.
13. After you investigate the alert, return to the Overview tab where you can View details to triage and manage the disposition of the alert, add comments and assign ownership of the alert.
14. After you take the required action for the alert, set the Status of the alert to Resolved.

## Validation
1. Sign in to the Microsoft Purview portal and navigate to Data loss prevention > Alerts. 2. Confirm the DLP Alerts dashboard loads without errors. 3. Apply a filter (e.g., by date range or severity) and verify the list updates accordingly. 4. Customize columns to include properties like 'Alert name', 'Status', and 'Severity', and confirm the display changes. 5. Double-click a column header to sort ascending/descending and verify the sort order. 6. Double-click an alert and verify the Details tab opens with high-level information. 7. Select 'Summarize with Copilot' and confirm a summary is generated. 8. Select 'View details' and verify the Overview tab appears. 9. Click the Events tab and select an event; confirm detailed event information is displayed. 10. For an event, click the Actions drop-down and verify options like 'Verify as true match' or 'Report as false positive' are available. 11. If insider risk management is enabled, check that the 'User activity summary' tab appears for in-scope users and shows exfiltration activities. 12. On the Overview tab, verify you can add comments, assign ownership, and change the alert status to 'Resolved'.

## Rollback
1. If the DLP Alerts dashboard fails to load, clear browser cache and cookies, then retry. 2. If filters or custom columns do not apply correctly, reset the dashboard view by navigating away and back to Data loss prevention > Alerts. 3. If sorting does not work, refresh the page and attempt sorting again. 4. If an alert fails to open, try a different alert or refresh the dashboard. 5. If 'Summarize with Copilot' does not generate a summary, ensure Copilot is enabled in the tenant and retry. 6. If the Events tab does not show events, verify the alert has associated events and refresh. 7. If the Actions drop-down is missing expected options, confirm the user has appropriate permissions (e.g., DLP Compliance Management). 8. If the 'User activity summary' tab is missing, verify insider risk management settings have sharing turned On and the user is in scope of a policy. 9. If changes to alert status or comments are not saved, re-enter the information and save again. 10. If any step causes unexpected behavior, close the browser and reopen the Purview portal to restore the default dashboard state.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-learn>
