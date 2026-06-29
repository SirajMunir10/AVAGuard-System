# Incident Response: Insider Risk Management

**Domain:** Purview
**Subdomain:** Insider Risk Management
**Incident Type:** Incident Response

## Scenario / Query
How to escalate an insider risk case to a user or data investigation for deeper collaboration?

## Environment Context
- **Tenant Type:** Microsoft 365 with Purview Insider Risk Management
- **Configuration:** Insider risk management roles and permissions configured

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Determine the severity of the case
2. Review the history of risk of the user
3. Consider the risk guidelines of your organization
4. Escalate the case to a user or data investigation to collaborate with other areas of your organization and to dive deeper into risk activities

## Validation
1. Confirm that the case status is updated to 'Escalated' in the Insider Risk Management case dashboard.
2. Verify that the case is now visible in the Microsoft Purview compliance portal under 'Data investigations' or 'User investigations' as appropriate.
3. Ensure that the assigned investigator or team can access the case details and associated alerts.
4. Check that the escalation note or justification is recorded in the case history.
5. Validate that the user's risk history and case timeline are preserved after escalation.

## Rollback
1. Navigate to the escalated case in the Insider Risk Management case dashboard.
2. Select the case and choose 'Reassign' or 'Change status' to revert to the original status (e.g., 'Active' or 'Needs review').
3. If the case was moved to a different investigation area, contact the receiving team to return the case to Insider Risk Management.
4. Remove any escalation notes or comments if necessary, or add a note explaining the rollback.
5. Confirm the case is no longer visible in the data or user investigation queues and is back in the Insider Risk Management queue.

## References
- <https://learn.microsoft.com/en-us/purview/insider-risk-management-cases>
