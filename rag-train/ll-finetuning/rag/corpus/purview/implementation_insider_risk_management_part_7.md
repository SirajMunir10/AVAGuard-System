# Implementation: Insider Risk Management

**Domain:** Purview
**Subdomain:** Insider Risk Management
**Incident Type:** Implementation

## Scenario / Query
How to run automated tasks using Power Automate flows for an Insider Risk Management case?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Insider Risk Management enabled, Power Automate flows configured

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select Automate on the case action toolbar.
2. Choose the Power Automate flow to run, and then select Run flow.
3. After the flow completes, select Done.

## Validation
1. Navigate to Microsoft Purview compliance portal > Insider Risk Management > Cases. 2. Open the specific case where the flow was run. 3. On the case action toolbar, select 'Automate' and verify the flow appears in the list with a status of 'Completed' or 'Succeeded'. 4. Select 'Done' to confirm the flow execution. 5. Optionally, check the Power Automate flow run history (https://make.powerautomate.com) for the specific flow to confirm successful execution and review any outputs.

## Rollback
1. If the flow caused unintended changes, open the case in Insider Risk Management and review the case activity log for any actions taken by the flow. 2. Manually reverse any changes made by the flow (e.g., if the flow escalated the case, de-escalate it; if it sent notifications, send a correction). 3. If the flow failed or caused errors, edit the Power Automate flow (https://make.powerautomate.com) to correct the logic or triggers, then re-run it from the case action toolbar by selecting 'Automate' > 'Run flow'. 4. If the flow cannot be corrected, remove the flow association from the case by selecting 'Automate' > 'Manage flows' and deleting the connection, then re-create a corrected flow.

## References
- <https://learn.microsoft.com/en-us/purview/insider-risk-management-cases>
