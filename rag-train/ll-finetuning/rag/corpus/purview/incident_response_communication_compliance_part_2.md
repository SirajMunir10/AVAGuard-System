# Incident Response: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Incident Response

## Scenario / Query
How to review Communication Compliance policy matches and remediation actions for a user?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** N/A

## Symptoms
- Pending policy matches for a user

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. View the Communication Compliance policy matches section which displays the total number of communication Policy matches and total number of Remediation actions for the user included in this policy match
2. Select View details in this section to display a timeline of Communication Compliance activities for the user
3. Review the timeline which includes: totals for Policy matches and Remediation actions for the user, and details for each activity associated with the user for the past 30 days

## Validation
1. Navigate to Microsoft Purview compliance portal > Communication Compliance > Policies. 2. Select the relevant policy and open the policy details. 3. In the 'Policy matches' section, verify the total number of policy matches and remediation actions for the user. 4. Click 'View details' to open the user's activity timeline. 5. Confirm the timeline displays totals for policy matches and remediation actions, and includes details for each activity associated with the user for the past 30 days.

## Rollback
1. If the policy matches or remediation actions are incorrect, review the policy configuration to ensure the policy conditions, users, and reviewers are correctly set. 2. If needed, edit the policy to adjust conditions or scope. 3. For incorrect remediation actions, use the 'Resolve' option in the policy details to undo or modify the action (e.g., change a 'Resolve' status back to 'Pending'). 4. If the timeline shows incorrect data, wait for the next data refresh cycle (up to 24 hours) or contact Microsoft support for data correction.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
