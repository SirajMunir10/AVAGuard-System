# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to require terms of use acknowledgment as a grant control in a Conditional Access policy?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Conditional Access policy with grant controls

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. If your organization created terms of use, other options might be visible under grant controls.
2. These options allow admins to require acknowledgment of terms of use as a condition of accessing the resources that the policy protects.

## Validation
1. Sign in as a test user who is subject to the Conditional Access policy. 2. Attempt to access the protected resource (e.g., https://portal.azure.com). 3. Verify that the user is prompted to review and accept the terms of use before access is granted. 4. After acceptance, confirm the user can access the resource. 5. In the Microsoft Entra admin center, navigate to Protection > Conditional Access > Policies, select the policy, and under Grant > Grant access, confirm that 'Require terms of use' is selected with the specific terms of use listed.

## Rollback
1. In the Microsoft Entra admin center, navigate to Protection > Conditional Access > Policies. 2. Select the policy that was modified. 3. Under Grant > Grant access, uncheck 'Require terms of use' or remove the specific terms of use from the selection. 4. Click Save to apply the change. 5. Verify that users are no longer prompted to accept the terms of use when accessing the protected resource.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant>
