# Remediation: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Remediation

## Scenario / Query
How do I unresolve a message in Communication Compliance?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Communication Compliance solution

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Sign in to the Microsoft Purview portal with credentials for an admin account in your Microsoft 365 organization.
2. Go to the Communication Compliance solution.
3. Select Policies in the left navigation, then select a policy that contains the resolved message to view the policy matches.
4. Select the Resolved tab.
5. On the Resolved tab, select one or more messages.
6. On the command bar, select Unresolve.
7. On the Unresolve item pane, add any comments, then select Save.
8. Select the Pending tab to verify that the selected items are displayed.

## Validation
1. Sign in to the Microsoft Purview portal with admin credentials. 2. Navigate to Communication Compliance > Policies. 3. Select the policy that contained the resolved message. 4. Click the 'Resolved' tab and confirm the message is no longer listed. 5. Click the 'Pending' tab and verify the message appears there. 6. Optionally, open the message to confirm its status is now 'Pending'.

## Rollback
1. Sign in to the Microsoft Purview portal with admin credentials. 2. Navigate to Communication Compliance > Policies. 3. Select the same policy. 4. On the 'Pending' tab, select the message(s) that were unresolved. 5. On the command bar, select 'Resolve'. 6. In the Resolve item pane, add comments if needed, then select 'Save'. 7. Verify the message moves back to the 'Resolved' tab.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
