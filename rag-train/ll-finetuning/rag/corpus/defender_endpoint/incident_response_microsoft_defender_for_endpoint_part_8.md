# Incident Response: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Incident Response

## Scenario / Query
How to undo contain user actions in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Global Administrator role required

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select the Contain User action in the Action Center.
2. In the side pane, select Undo.
3. Select the user from either the user inventory, Incident page side pane, or alert side pane and select Undo.

## Validation
1. Sign in to Microsoft 365 Defender portal (https://security.microsoft.com) with Global Administrator role.
2. Navigate to Action Center (https://security.microsoft.com/action-center).
3. Verify that the 'Contain user' action for the target user is no longer listed as 'Active' or 'Pending'.
4. Alternatively, go to the user inventory (https://security.microsoft.com/users), select the user, and confirm the 'Contain user' status is removed.
5. Check the Incident page or alert side pane for the same user to ensure the 'Contain user' action is not present.
6. Confirm the user can now authenticate and access resources normally.

## Rollback
1. Sign in to Microsoft 365 Defender portal (https://security.microsoft.com) with Global Administrator role.
2. Navigate to Action Center (https://security.microsoft.com/action-center).
3. If the 'Contain user' action was undone but needs to be reapplied, select the user again and choose 'Contain user' from the available actions.
4. Alternatively, go to the user inventory, Incident page side pane, or alert side pane for the target user and select 'Contain user'.
5. Confirm the action is submitted and appears as 'Pending' or 'Active' in Action Center.
6. Verify the user is contained by checking that their access is restricted as expected.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
