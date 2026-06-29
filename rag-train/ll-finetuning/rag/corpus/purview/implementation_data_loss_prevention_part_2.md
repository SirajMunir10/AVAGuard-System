# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to configure alerts for DLP policies to be notified when protective actions are taken on sensitive items?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policies with alert configuration

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Configure alerts for DLP policies to be notified when an action is taken on a sensitive item
2. Use the DLP alert management dashboard in the Microsoft Purview portal to view alerts, events, and associated metadata for DLP policy violations

## Validation
1. In the Microsoft Purview portal, navigate to Data Loss Prevention > Alerts. 2. Confirm that the alert dashboard shows alerts for the DLP policy you configured. 3. For a specific alert, verify that the alert details include the policy name, rule name, action taken, and the sensitive information type detected. 4. Optionally, use the DLP alert management dashboard to filter by policy name and confirm that alerts are generated when protective actions (e.g., block, warn) are taken on sensitive items.

## Rollback
1. In the Microsoft Purview portal, go to Data Loss Prevention > Policies. 2. Select the DLP policy for which you configured alerts. 3. Edit the policy and navigate to the 'Alert' settings section. 4. Disable or remove the alert configuration (e.g., set 'Send alert to admin' to 'Off' or delete the alert rule). 5. Save the policy changes. 6. Verify that no new alerts are generated for that policy by checking the DLP alert dashboard.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-learn>
