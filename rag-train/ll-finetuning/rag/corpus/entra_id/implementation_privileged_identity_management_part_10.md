# Implementation: Privileged Identity Management

**Domain:** Entra ID
**Subdomain:** Privileged Identity Management
**Incident Type:** Implementation

## Scenario / Query
How do delegated approvers approve or deny pending role requests in PIM?

## Environment Context
- **Tenant Type:** Microsoft Entra ID tenant with PIM enabled
- **Configuration:** Delegated approvers configured for role activation

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Delegated approvers receive email notifications when a role request is pending their approval.
2. Approvers can view, approve, or deny these pending requests in PIM.
3. After the request is approved, the member can start using the role.

## Validation
1. Sign in to the Microsoft Entra admin center as a delegated approver. 2. Navigate to Identity Governance > Privileged Identity Management > Approve requests. 3. Confirm that pending role activation requests are listed under 'Requests awaiting my approval'. 4. Select a request and choose 'Approve' or 'Deny'. 5. Verify that after approval, the request status changes to 'Approved' and the member can activate the role. 6. Check that the member receives a notification or can activate the role in PIM.

## Rollback
1. If an approval was made in error, sign in as a Privileged Role Administrator. 2. Navigate to Identity Governance > Privileged Identity Management > Audit history. 3. Locate the approval event and review details. 4. To revoke an activated role, go to PIM > Roles > Active assignments, select the user, and choose 'Remove active assignment'. 5. If a denial was incorrect, the requester can resubmit a new activation request. 6. Ensure delegated approvers are reconfigured if needed via PIM settings for the role.

## References
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure>
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure#approve-or-deny>
