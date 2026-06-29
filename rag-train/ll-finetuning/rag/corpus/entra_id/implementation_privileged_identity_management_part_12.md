# Implementation: Privileged Identity Management

**Domain:** Entra ID
**Subdomain:** Privileged Identity Management
**Incident Type:** Implementation

## Scenario / Query
How to configure approval for role elevation requests in PIM?

## Environment Context
- **Tenant Type:** Entra ID tenant with PIM licensed
- **Configuration:** PIM role settings

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. View pending approvals (requests)
2. Approve or reject requests for role elevation (single and bulk)
3. Provide justification for my approval or rejection

## Validation
1. Sign in to the Entra admin center as a user with the Privileged Role Administrator role.
2. Navigate to Identity Governance > Privileged Identity Management > Azure AD roles > Approve requests.
3. Confirm that pending requests for role elevation are visible under the 'Requests for my approval' tab.
4. Select a pending request and click 'Approve' or 'Reject'.
5. In the approval pane, verify that a justification text box is displayed and that you can enter a reason.
6. After approving or rejecting, confirm that the request status updates accordingly (e.g., 'Approved' or 'Rejected') and that the user receives a notification (if configured).
7. Optionally, test bulk approval by selecting multiple requests and clicking 'Approve' or 'Reject' to confirm the bulk action completes without error.

## Rollback
1. If an approval was made in error, sign in as a Privileged Role Administrator and navigate to Identity Governance > Privileged Identity Management > Azure AD roles > Approve requests.
2. Locate the incorrectly approved request under 'History' or 'Approved requests'.
3. To revoke the elevated role assignment, go to Identity Governance > Privileged Identity Management > Azure AD roles > Active assignments.
4. Find the user with the active role assignment that resulted from the erroneous approval.
5. Select the assignment and click 'Remove' to deactivate the role assignment immediately.
6. If a rejection was made in error, the user must resubmit a new elevation request; there is no direct undo for a rejection. Instruct the user to submit a new request.
7. To restore previous approval settings (if changes were made to the approval workflow), navigate to Identity Governance > Privileged Identity Management > Azure AD roles > Role settings, select the affected role, and revert any modified settings (e.g., require approval toggle, approver list) to their prior state.

## References
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure>
