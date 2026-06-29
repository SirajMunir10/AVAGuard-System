# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to configure grant controls in a Conditional Access policy to enforce multifactor authentication, device compliance, or other access requirements?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Conditional Access policy grant controls

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Admins can choose to enforce one or more controls when granting access. These controls include: Require multifactor authentication (Microsoft Entra multifactor authentication), Require authentication strength, Require device to be marked as compliant (Microsoft Intune), Require Microsoft Entra hybrid joined device, Require approved client app, Require app protection policy, Require password change.
2. When admins choose to combine these options, they can use the following methods: Require all the selected controls (control and control), Require one of the selected controls (control or control).
3. By default, Conditional Access requires all selected controls.

## Validation
1. Sign in as a test user who is subject to the Conditional Access policy. 2. Verify that the grant controls are enforced: if 'Require multifactor authentication' is selected, confirm that the user is prompted for MFA. 3. If 'Require device to be marked as compliant' is selected, confirm that only compliant devices (as per Intune) are allowed. 4. Use the 'What If' tool in the Conditional Access UI (https://learn.microsoft.com/en-us/entra/identity/conditional-access/what-if-tool) to simulate a sign-in and verify that the policy applies with the correct grant controls. 5. Check the sign-in logs in Entra ID for the test user to confirm that the grant control requirement was satisfied (e.g., MFA completed, device compliant).

## Rollback
1. In the Microsoft Entra admin center, navigate to Protection > Conditional Access. 2. Locate the policy that was modified or created. 3. Edit the policy and change the grant controls back to the previous settings (e.g., remove the newly added control or revert to the original combination). 4. If the policy was newly created, disable or delete it. 5. Test by signing in as a test user to confirm that the previous access behavior is restored. 6. Monitor sign-in logs to ensure no unexpected access denials or grants occur.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant>
