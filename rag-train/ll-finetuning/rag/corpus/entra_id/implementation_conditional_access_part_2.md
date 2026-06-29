# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
A Conditional Access policy targeting all cloud apps with a block control is not being enforced for a user who meets all conditions. What is the most likely misconfiguration?

## Environment Context
- **Tenant Type:** Production
- **Configuration:** Conditional Access policy with 'All cloud apps' and 'Block access' control, assigned to a test user in a group. The user is in scope and meets all conditions.

## Symptoms
- User can still access Exchange Online and SharePoint Online despite the policy being enabled
- Sign-in logs show the policy was not evaluated for the user
- No other Conditional Access policies apply to the user

## Error Codes
N/A

## Root Causes
1. The policy is in 'Report-only' mode instead of 'On'
2. The policy excludes the user or group in the 'Exclude' tab
3. The policy targets 'All cloud apps' but the user's app is not considered a cloud app (e.g., legacy authentication or non-Microsoft app)

## Remediation Steps
1. Navigate to the Conditional Access policy in the Azure portal
2. Under 'Enable policy', select 'On' instead of 'Report-only'
3. Verify the 'Users and groups' assignment includes the correct user or group and does not exclude them
4. Confirm the policy targets 'All cloud apps' (or the specific app) and that the app is a supported cloud app
5. Use the 'What If' tool to simulate access for the user and validate the policy will apply

## Validation
Use the 'What If' tool in Conditional Access to simulate the user's sign-in and confirm the policy is evaluated and blocks access. Also check the Sign-in logs for the 'Conditional Access' tab to see policy status.

## Rollback
Set the policy to 'Report-only' or disable it temporarily by setting 'Enable policy' to 'Off'.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-policies>
