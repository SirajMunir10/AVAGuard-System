# Implementation: Authentication

**Domain:** Entra ID
**Subdomain:** Authentication
**Incident Type:** Implementation

## Scenario / Query
How to deploy Microsoft Entra multifactor authentication using a phased rollout plan with Conditional Access policies?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Conditional Access policies, authentication methods, session lifetime settings, MFA registration policies

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Meet the necessary prerequisites
2. Configure chosen authentication methods
3. Configure your Conditional Access policies
4. Configure session lifetime settings
5. Configure Microsoft Entra multifactor authentication registration policies

## Validation
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator or Security Administrator. 2. Navigate to Protection > Conditional Access > Policies and verify that the new MFA policy is listed with status 'On' and the correct assignments (users, groups, apps). 3. Navigate to Protection > Authentication methods > Policies and confirm that the selected MFA methods (e.g., Microsoft Authenticator, SMS) are enabled and configured. 4. Navigate to Protection > Authentication methods > Registration campaign and verify that the MFA registration campaign is enabled and targeted to the correct users. 5. Sign in as a test user in the pilot group and confirm that MFA registration is prompted and that MFA is required when accessing a protected app. 6. Use the 'What If' tool in Conditional Access to simulate a sign-in for a pilot user and confirm the MFA policy applies.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator or Security Administrator. 2. Navigate to Protection > Conditional Access > Policies, locate the new MFA policy, and set its status to 'Off' or delete it. 3. Navigate to Protection > Authentication methods > Registration campaign and disable the registration campaign if it was enabled. 4. If any authentication methods were changed, revert them to the previous state (e.g., disable newly enabled methods, re-enable previously disabled methods). 5. If session lifetime settings were modified, navigate to Protection > Conditional Access > Policies, edit the relevant policy, and revert session controls to the original values. 6. Monitor sign-in logs for any users who may have been affected and, if needed, reset their MFA registration via Protection > Users > (select user) > Authentication methods.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-getstarted>
