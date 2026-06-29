# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to deploy new Conditional Access policies using Microsoft recommended templates?

## Environment Context
- **Tenant Type:** Any Entra ID tenant
- **Configuration:** Conditional Access policies

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use Conditional Access templates to deploy new policies aligned with Microsoft recommendations.
2. Select templates designed to provide maximum protection aligned with commonly used policies across various customer types and locations.

## Validation
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator, Reports Reader, or Global Reader. 2. Navigate to Protection > Conditional Access > Policies. 3. Confirm the new policy is listed with the expected name and status (On/Off). 4. Select the policy and verify that Assignments (users/groups, cloud apps, conditions) and Access controls (Grant, Session) match the template used. 5. Use the 'What If' tool (Protection > Conditional Access > What If) to simulate a user sign-in matching the policy conditions and confirm the expected grant or block result. 6. Optionally, run the following Microsoft Graph PowerShell command to list policies and verify the new one: Get-MgIdentityConditionalAccessPolicy | Where-Object {$_.DisplayName -eq '<PolicyName>'} | Format-List

## Rollback
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Locate the newly deployed policy. 4. If the policy is causing issues, set its status to 'Off' immediately to stop enforcement. 5. To fully remove the policy, select it and click 'Delete', then confirm. 6. Alternatively, use Microsoft Graph PowerShell: Remove-MgIdentityConditionalAccessPolicy -ConditionalAccessPolicyId '<PolicyId>'. 7. Verify removal by checking the policy list no longer contains the policy.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common>
