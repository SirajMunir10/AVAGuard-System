# Optimization: Multifactor Authentication

**Domain:** Entra ID
**Subdomain:** Multifactor Authentication
**Incident Type:** Optimization

## Scenario / Query
How to migrate RADIUS-based applications to modern protocols for Microsoft Entra multifactor authentication?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Applications using RADIUS authentication

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Move client applications to modern protocols such as SAML, OpenID Connect, or OAuth on Microsoft Entra ID.
2. Federate applications with Microsoft Entra ID and enforce MFA through Conditional Access when possible.

## Validation
1. Verify that the client application is configured to use SAML, OpenID Connect, or OAuth instead of RADIUS by checking the application's authentication settings in the Microsoft Entra admin center under 'Enterprise applications' > select the application > 'Authentication' or 'Single sign-on'.
2. Confirm that the application is federated with Microsoft Entra ID by navigating to 'Enterprise applications' > select the application > 'Properties' and ensuring 'User assignment required?' is set appropriately and the application is listed as 'Enabled for users to sign-in?'.
3. Test user sign-in to the application and ensure that MFA is enforced by triggering a Conditional Access policy that requires MFA. Use the 'What If' tool in Conditional Access to simulate a user sign-in and verify the policy applies.
4. Review the Microsoft Entra sign-in logs for the application to confirm successful authentication with MFA and no RADIUS-related errors.

## Rollback
1. Revert the client application's authentication protocol from SAML/OpenID Connect/OAuth back to RADIUS by reconfiguring the application's authentication settings in the Microsoft Entra admin center or on the application server.
2. If federation was established, remove the application's federation with Microsoft Entra ID by deleting the enterprise application registration in the Microsoft Entra admin center under 'Enterprise applications' > select the application > 'Delete'.
3. Disable any Conditional Access policies that were created or modified to enforce MFA for the application by navigating to 'Security' > 'Conditional Access' > select the policy > 'Disable'.
4. Restore the original RADIUS server configuration and ensure the application can authenticate using RADIUS again. Test user sign-in to confirm the rollback is successful.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-getstarted>
