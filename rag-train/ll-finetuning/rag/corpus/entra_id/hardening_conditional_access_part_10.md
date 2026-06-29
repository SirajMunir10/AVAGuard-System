# Hardening: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Hardening

## Scenario / Query
How to implement and validate the Block access control in a Conditional Access policy to prevent unintended side effects?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** Conditional Access policy with Block access grant control

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use Conditional Access report-only mode to test the policy before enabling it.
2. Use the What If tool in Conditional Access to evaluate the impact of the policy.
3. Apply the Block access control carefully, ensuring proper testing and validation before enabling at scale.

## Validation
1. Use the Conditional Access What If tool to simulate a user sign-in and confirm the policy with Block access grant control is triggered. 2. Enable the policy in report-only mode and monitor sign-in logs for at least 24 hours to verify that the intended users would be blocked without affecting production. 3. Review the Conditional Access insights and reporting workbook to ensure no unexpected blocks are reported.

## Rollback
1. Immediately disable the Conditional Access policy by setting its state to 'Off' in the Azure portal. 2. If the policy was applied to a pilot group, remove that group from the policy assignments. 3. Verify that affected users can sign in successfully by checking the sign-in logs for successful authentications after the policy is disabled.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant>
