# Troubleshooting: Privileged Identity Management

**Domain:** Entra ID
**Subdomain:** Privileged Identity Management
**Incident Type:** Troubleshooting

## Scenario / Query
How to cancel a pending role activation request in PIM when approval is required?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** PIM role activation requires approval

## Symptoms
- User has a pending role activation request that they no longer need

## Error Codes
N/A

## Root Causes
1. User submitted a role activation request but no longer requires the role

## Remediation Steps
1. Sign in to the Microsoft Entra admin center as at least a Privileged Role Administrator.
2. Browse to ID Governance > Privileged Identity Management > My requests.
3. For the role that you want to cancel, select the Cancel link.
4. When you select Cancel, the request is canceled.
5. To activate the role again, you have to submit a new request for activation.

## Validation
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) as a user with at least the Privileged Role Administrator role.
2. Navigate to ID Governance > Privileged Identity Management > My requests.
3. Verify that the previously pending role activation request no longer appears in the list of active requests.
4. Optionally, check the audit log: Browse to Privileged Identity Management > Audit history and filter by 'Cancel activation request' activity for the user to confirm the cancellation event.

## Rollback
1. If the cancellation was performed in error, the user must submit a new activation request: Sign in to the Microsoft Entra admin center, go to ID Governance > Privileged Identity Management > My roles, select the role, and follow the activation steps to request approval again.
2. If the cancellation fails or the request remains pending, escalate to a Privileged Role Administrator to review the request in Privileged Identity Management > Approve requests and manually deny or cancel the request from there.

## References
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-activate-role>
