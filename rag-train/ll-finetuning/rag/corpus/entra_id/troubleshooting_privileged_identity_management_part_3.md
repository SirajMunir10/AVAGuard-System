# Troubleshooting: Privileged Identity Management

**Domain:** Entra ID
**Subdomain:** Privileged Identity Management
**Incident Type:** Troubleshooting

## Scenario / Query
How to view the status of pending activation requests in Privileged Identity Management?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Privileged Identity Management enabled

## Symptoms
- Unable to determine the status of a role activation request

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Sign in to the Microsoft Entra admin center as at least a Privileged Role Administrator.
2. Browse to ID Governance > Privileged Identity Management > My requests.
3. When you select My requests you see a list of your Microsoft Entra role and Azure resource role requests.
4. Scroll to the right to view the Request Status column.

## Validation
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) as a user with at least the Privileged Role Administrator role.
2. Navigate to ID Governance > Privileged Identity Management > My requests.
3. In the list of requests, scroll to the right to locate the 'Request Status' column.
4. Confirm that the status for the pending activation request is displayed (e.g., 'Pending approval', 'Activated', 'Denied', etc.).
5. If the request is not visible, verify the user has submitted the request and that the correct scope (Microsoft Entra roles or Azure resource roles) is selected.

## Rollback
1. If the validation fails or the status is incorrect, sign in to the Microsoft Entra admin center as a Privileged Role Administrator.
2. Navigate to ID Governance > Privileged Identity Management > Approve requests (or 'Approve requests' under Tasks).
3. Locate the pending request by its ID or user name and review its details.
4. If the request was incorrectly approved or denied, use the 'Deny' or 'Approve' action to correct the status.
5. Alternatively, if the request is stuck, the administrator can cancel the request by selecting it and choosing 'Cancel' (if available).
6. Instruct the user to resubmit the activation request if needed.

## References
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-activate-role>
