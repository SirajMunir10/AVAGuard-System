# Implementation: Authentication

**Domain:** Entra ID
**Subdomain:** Authentication
**Incident Type:** Implementation

## Scenario / Query
How to require users to register for MFA when Microsoft Entra ID Protection licenses are not available?

## Environment Context
- **Tenant Type:** Microsoft Entra ID tenant without ID Protection licenses
- **Configuration:** Conditional Access policies

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use Conditional Access policies to target frequently used applications like HR systems to require MFA at sign-in.
2. Users are prompted to register the next time that MFA is required at sign-in.

## Validation
1. Sign in as a test user who does not have MFA registered.
2. Access a targeted application (e.g., HR system) that is covered by the Conditional Access policy requiring MFA.
3. Confirm that the user is prompted to register for MFA (e.g., set up the Microsoft Authenticator app or other methods) before being granted access.
4. After registration, sign out and sign in again to the same application; verify that MFA is now required and the user can complete authentication successfully.
5. Check the Conditional Access policy in the Azure portal: navigate to 'Microsoft Entra admin center' > 'Protection' > 'Conditional Access' > 'Policies', select the policy, and verify that it is enabled and configured to require MFA for the targeted applications.

## Rollback
1. In the Microsoft Entra admin center, go to 'Protection' > 'Conditional Access' > 'Policies'.
2. Locate the policy created to require MFA registration and set its state to 'Off' or delete the policy entirely.
3. If the policy was created with a specific exclusion (e.g., excluding break-glass accounts), ensure those exclusions remain intact.
4. Notify affected users that the MFA requirement has been removed and they will no longer be prompted to register MFA for the targeted applications.
5. Optionally, verify that users can now access the previously targeted applications without MFA prompts.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-getstarted>
