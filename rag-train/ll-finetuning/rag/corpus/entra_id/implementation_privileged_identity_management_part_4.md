# Implementation: Privileged Identity Management

**Domain:** Entra ID
**Subdomain:** Privileged Identity Management
**Incident Type:** Implementation

## Scenario / Query
How do eligible members activate their Azure AD roles in Privileged Identity Management?

## Environment Context
- **Tenant Type:** Entra ID tenant with PIM licensed
- **Configuration:** User must be eligible for a role in PIM

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Sign in to the Microsoft Entra admin center as an eligible member.
2. Browse to Identity governance > Privileged Identity Management > My roles.
3. Select Azure AD roles to see a list of your eligible Azure AD roles.
4. Under Action, select Activate.
5. Enter the reason for activation in the Reason box.
6. Select Activate.

## Validation
1. Sign in to the Microsoft Entra admin center as the eligible member. 2. Navigate to Identity governance > Privileged Identity Management > My roles > Azure AD roles. 3. Confirm that the role now shows as 'Active' (not 'Eligible') in the list. 4. Verify the activation duration and reason are recorded in the PIM audit history: browse to Privileged Identity Management > Audit history > Azure AD role activations and locate the corresponding activation event.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Privileged Role Administrator. 2. Navigate to Identity governance > Privileged Identity Management > Azure AD roles > Active assignments. 3. Locate the user's active assignment for the role. 4. Select the assignment and choose 'Remove' to deactivate the role immediately. 5. Alternatively, if the activation was self-service, the eligible member can wait for the activation duration to expire, or a Privileged Role Administrator can manually deactivate the role as described.

## References
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-activate-role>
