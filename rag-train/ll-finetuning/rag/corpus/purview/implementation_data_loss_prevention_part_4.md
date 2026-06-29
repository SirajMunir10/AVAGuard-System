# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How do I create a shareable link to a DLP alert event in Microsoft Purview?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP Alerts console access required

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. In the Purview Portal, navigate to Data Loss Prevention, and then select Alerts.
2. Select an alert, and then select View details.
3. On the Alert details screen, select the Events tab just below the alert title to view the events contained in this alert.
4. Select the event you want to share, and then click the Actions button at the bottom of the screen to see the Actions menu.
5. Select Copy event link, and then select Copy to copy the shareable link to the event.
6. Paste the link from your clipboard to share the link via chat, email, or other means.

## Validation
1. Confirm the user has access to the DLP Alerts console in Microsoft Purview. 2. Navigate to Data Loss Prevention > Alerts, select an alert, and click View details. 3. On the Alert details screen, select the Events tab. 4. Select an event, click Actions, and verify that 'Copy event link' appears in the menu. 5. Click 'Copy event link' and then 'Copy' to copy the link. 6. Paste the link into a browser or chat to confirm it opens the specific event details page.

## Rollback
1. If the link does not work or was shared in error, ask recipients to disregard or delete the link. 2. To prevent further sharing, the DLP alert event can be closed or resolved in the Purview portal (select the alert, then 'Resolve' or 'Dismiss'). 3. If the issue is that the 'Copy event link' option is missing, verify that the user has the required permissions (e.g., DLP Alerts Admin role) and that the alert is not in a state that prevents sharing. 4. If the link was copied incorrectly, repeat the steps to generate a new link.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-learn>
