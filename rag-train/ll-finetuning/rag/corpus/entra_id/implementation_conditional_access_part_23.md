# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to configure grant controls for agent users in a Conditional Access policy?

## Environment Context
- **Tenant Type:** Entra ID tenant with Windows 365 for Agents
- **Configuration:** Conditional Access policy targeting agent identities

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. When a policy targets agents acting as users, the available grant behavior differs from user and group scenarios: Block access, Grant access with Require device to be marked as compliant.
2. Use Require device to be marked as compliant when agent user sessions run on managed endpoints that provide device compliance signals.
3. Agent identities don't support grant controls and only support Block access.
4. For targeting and condition guidance, see Target agent identities in Conditional Access policies.

## Validation
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Locate and select the policy that targets agent identities. 4. Under 'Grant', confirm that only 'Block access' is selected (or 'Grant access' with 'Require device to be marked as compliant' if the policy targets agents acting as users on managed endpoints). 5. Verify that no other grant controls (e.g., Require multifactor authentication, Require password change) are selected, as they are not supported for agent identities. 6. Use the 'What If' tool to test the policy against an agent user account and confirm the expected grant behavior is applied.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Locate and select the policy that was modified. 4. Under 'Grant', revert to the previous grant control settings (e.g., remove 'Require device to be marked as compliant' and select 'Block access' if that was the original setting). 5. If the policy was newly created, disable or delete the policy. 6. Use the 'What If' tool to verify that the policy no longer applies unintended grant controls. 7. Monitor sign-in logs for any access issues caused by the change and adjust as needed.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant>
