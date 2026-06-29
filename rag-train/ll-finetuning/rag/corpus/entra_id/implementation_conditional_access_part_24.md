# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to require specific authentication strengths in a Conditional Access policy?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Authentication strengths defined in Microsoft Entra admin center > Entra ID > Authentication methods > Authentication strengths

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to Microsoft Entra admin center > Entra ID > Authentication methods > Authentication strengths.
2. Choose to create your own authentication strength or use the built-in versions.
3. In the Conditional Access policy, select 'Require authentication strength' and choose the desired strength.

## Validation
1. Navigate to Microsoft Entra admin center > Protection > Conditional Access > Policies. 2. Select the policy that was configured. 3. Under 'Grant', verify that 'Require authentication strength' is selected and the correct authentication strength (e.g., 'Multifactor authentication' or a custom strength) is chosen. 4. Use the 'What If' tool to simulate a user sign-in and confirm the policy is applied as expected. 5. Optionally, sign in as a test user and check the sign-in logs (Microsoft Entra admin center > Identity > Monitoring & health > Sign-in logs) to confirm the authentication strength requirement is enforced.

## Rollback
1. Navigate to Microsoft Entra admin center > Protection > Conditional Access > Policies. 2. Select the policy where the authentication strength was configured. 3. Under 'Grant', change the selection from 'Require authentication strength' to the previous grant control (e.g., 'Require multifactor authentication' or 'Block access') or remove the grant control entirely. 4. Save the policy. 5. If the policy was newly created, delete the policy entirely. 6. Use the 'What If' tool to verify the change and monitor sign-in logs to ensure the previous behavior is restored.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant>
