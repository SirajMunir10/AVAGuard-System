# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to configure the 'Require risk remediation' grant control in a Conditional Access policy?

## Environment Context
- **Tenant Type:** Entra ID tenant with Conditional Access
- **Configuration:** Conditional Access policy with grant controls

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select 'Require risk remediation' as a grant control in the Conditional Access policy.
2. The following settings are automatically applied to the policy: Require authentication strength, Sign-in frequency - Every time.

## Validation
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Locate and select the policy where 'Require risk remediation' was configured. 4. Under 'Grant', verify that 'Require risk remediation' is checked and that 'Require authentication strength' and 'Sign-in frequency - Every time' are automatically selected. 5. Use the 'What If' tool to simulate a user sign-in and confirm the policy applies as expected.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Locate and select the policy where 'Require risk remediation' was configured. 4. Under 'Grant', uncheck 'Require risk remediation'. 5. If needed, manually adjust 'Require authentication strength' and 'Sign-in frequency' to previous settings. 6. Save the policy.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant>
