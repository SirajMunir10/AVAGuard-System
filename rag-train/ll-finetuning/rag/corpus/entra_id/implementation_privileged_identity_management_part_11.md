# Implementation: Privileged Identity Management

**Domain:** Entra ID
**Subdomain:** Privileged Identity Management
**Incident Type:** Implementation

## Scenario / Query
How to set up extension and renewal workflows for time-bound role assignments in Privileged Identity Management?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** PIM role assignments with expiration

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Configure time-bound owner or member assignments
2. Allow users to request extension when assignment nears expiration
3. Allow users to request renewal when assignment expires
4. Ensure Global Administrator or Privileged Role Administrator can approve or deny extension/renewal requests

## Validation
1. Sign in to the Microsoft Entra admin center as a Global Administrator or Privileged Role Administrator. 2. Navigate to Identity Governance > Privileged Identity Management > Azure AD roles > Settings. 3. Select the role for which you configured time-bound assignments. 4. Verify that under 'Assignment' the 'Expire eligible assignments after' and 'Expire active assignments after' are set to the desired duration. 5. Under 'Extension and renewal', confirm that 'Allow users to request extension when assignment nears expiration' and 'Allow users to request renewal when assignment expires' are both enabled. 6. As a test user with an eligible assignment, sign in to the PIM portal and verify that the 'Extend' option appears when the assignment is within the extension window (e.g., 14 days before expiration). 7. Submit an extension request and confirm that it appears in the 'Approve requests' pane for an administrator. 8. Approve the request and verify that the assignment end date is updated accordingly. 9. After the assignment expires, sign in as the same user and confirm that the 'Renew' option is available. 10. Submit a renewal request and verify that an administrator can approve it, reactivating the assignment.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Global Administrator or Privileged Role Administrator. 2. Navigate to Identity Governance > Privileged Identity Management > Azure AD roles > Settings. 3. Select the role for which you configured extension and renewal workflows. 4. Under 'Extension and renewal', disable both 'Allow users to request extension when assignment nears expiration' and 'Allow users to request renewal when assignment expires'. 5. If you need to remove time-bound assignments entirely, under 'Assignment' set 'Expire eligible assignments after' and 'Expire active assignments after' to 'Never'. 6. To revoke any pending extension or renewal requests, go to 'Approve requests' and deny or cancel all pending requests for the affected role. 7. If any assignments were extended or renewed during testing, manually deactivate those assignments by selecting the assignment in PIM and choosing 'Remove' or 'Deactivate' to restore the original assignment end dates. 8. Verify that users can no longer see the 'Extend' or 'Renew' options in the PIM portal.

## References
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure>
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure#extend-and-renew-assignments>
