# Implementation: Policy Enforcement

**Domain:** Governance
**Subdomain:** Policy Enforcement
**Incident Type:** Implementation

## Scenario / Query
A Microsoft 365 tenant administrator attempts to enable the 'Require MFA for all users' conditional access policy from the Azure portal, but the policy fails to apply to all users. What is the likely cause and how should it be resolved?

## Environment Context
- **Tenant Type:** Microsoft 365 E5
- **Configuration:** Conditional Access policy targeting 'All users' with grant control 'Require multi-factor authentication'

## Symptoms
- Policy is created and enabled but does not prompt for MFA for some users
- No errors appear in the Azure portal during policy creation
- Users who already have MFA registered are not prompted again

## Error Codes
N/A

## Root Causes
1. The policy may be configured with 'Report-only' mode instead of 'On'
2. Excluded users or groups may inadvertently include the test users
3. The policy may not include 'All cloud apps' or the specific apps being accessed

## Remediation Steps
1. Verify the policy state is set to 'On' in the Conditional Access blade
2. Review the 'Exclude' tab to ensure no users or groups are excluded unintentionally
3. Confirm that 'Cloud apps or actions' includes 'All cloud apps' or the target applications
4. Use the 'What If' tool in Conditional Access to simulate a user sign-in and validate policy application

## Validation
Use the 'What If' tool for a test user to confirm the policy is evaluated and the grant control 'Require multi-factor authentication' is applied.

## Rollback
Set the policy to 'Off' or 'Report-only' to stop enforcement while troubleshooting.

## References
- <https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policies>
