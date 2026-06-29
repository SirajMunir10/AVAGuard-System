# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to implement a Conditional Access policy that requires multifactor authentication for device registration?

## Environment Context
- **Tenant Type:** Entra ID tenant with Conditional Access licensing
- **Configuration:** Conditional Access policies

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Create a Conditional Access policy that targets the 'Register or join devices' user action
2. Configure the policy to require multifactor authentication (MFA) as a grant control

## Validation
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) as a Conditional Access administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Locate the newly created policy (e.g., 'Require MFA for device registration'). 4. Confirm the policy is set to 'Report-only' or 'On' and verify the following settings: a. Under 'Assignments' > 'Users and groups', confirm the intended users or groups are included. b. Under 'Assignments' > 'Cloud apps or actions' > 'User actions', verify 'Register or join devices' is selected. c. Under 'Access controls' > 'Grant', confirm 'Require multifactor authentication' is checked and 'Require all the selected controls' is selected. 5. Use the 'What If' tool (https://learn.microsoft.com/en-us/entra/identity/conditional-access/what-if-tool) to simulate a device registration attempt for a test user and confirm the policy applies and requires MFA. 6. As a test user, attempt to register a device (e.g., join a device to Entra ID) and verify that MFA is prompted before completion.

## Rollback
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) as a Conditional Access administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Locate the policy created for requiring MFA on device registration. 4. To disable the policy without deleting it, set the 'Enable policy' toggle to 'Off' and click 'Save'. 5. Alternatively, to delete the policy, select the policy, click 'Delete', and confirm the deletion. 6. If the policy was in 'Report-only' mode, switch it to 'Off' to stop evaluation. 7. Verify the policy is no longer active by checking the policy list and confirming its state is 'Off' or it is removed. 8. If users are unable to register devices due to the policy, temporarily disable it and instruct users to retry device registration.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policy-common>
