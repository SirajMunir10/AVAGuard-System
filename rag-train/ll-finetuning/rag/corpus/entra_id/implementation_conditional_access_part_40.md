# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to configure a Conditional Access policy for Exchange ActiveSync clients?

## Environment Context
- **Tenant Type:** Entra ID tenant with Exchange Online
- **Configuration:** Conditional Access policy assigned to Exchange ActiveSync clients

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Assign policy to users or groups (selecting 'All users', 'All guest and external users', or 'Directory roles' causes all users to be subject of the policy).
2. Ensure Exchange Online is the only cloud application assigned to the policy.
3. Narrow the scope of this policy to specific platforms using the 'Device platforms' condition.
4. If the access control assigned to the policy uses 'Require approved client app', the user is directed to install and use the Outlook mobile client.
5. If 'Multifactor authentication', 'Terms of use', or custom controls are required, affected users are blocked because basic authentication does not support these controls.

## Validation
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Locate the policy configured for Exchange ActiveSync clients. 4. Confirm the policy is set to 'On' and assigned to the intended users or groups (e.g., 'All users'). 5. Verify that 'Exchange Online' is the only cloud app selected under 'Cloud apps or actions'. 6. Under 'Conditions' > 'Device platforms', confirm the policy is scoped to the desired platforms (e.g., 'Android', 'iOS'). 7. Under 'Grant', verify the access controls (e.g., 'Require approved client app') are correctly configured. 8. Use the 'What If' tool to simulate a user accessing Exchange Online via Exchange ActiveSync and confirm the policy applies as expected.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Locate the policy configured for Exchange ActiveSync clients. 4. Set the policy state to 'Off' to disable it immediately. 5. If the policy was created incorrectly, delete the policy by selecting 'Delete' from the policy's context menu. 6. Alternatively, modify the policy assignments: remove any incorrect user/group assignments, change the cloud app selection, or adjust the grant controls to a less restrictive setting (e.g., 'Require approved client app' instead of 'Require multifactor authentication'). 7. Verify that users can access Exchange Online via Exchange ActiveSync without being blocked.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-conditions>
