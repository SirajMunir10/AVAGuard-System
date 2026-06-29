# Troubleshooting: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate identity risks in Microsoft Entra ID Protection when access to the risk reports page requires authorization?

## Environment Context
- **Tenant Type:** Microsoft Entra ID tenant with Identity Protection enabled
- **Configuration:** Access to Identity Protection risk reports requires appropriate permissions (e.g., Security Reader, Security Operator, or Security Administrator role).

## Symptoms
- Access to the Identity Protection risk reports page is denied with message: 'Access to this page requires authorization. You can try signing in or changing directories.'

## Error Codes
N/A

## Root Causes
1. Insufficient permissions to view Identity Protection risk reports.

## Remediation Steps
1. Sign in with an account that has the required role (e.g., Security Reader, Security Operator, or Security Administrator).
2. If already signed in, try changing directories to the correct tenant.

## Validation
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) with an account that has at least the Security Reader role assigned. 2. Navigate to Protection > Identity Protection > Risky users. 3. Confirm the page loads without an authorization error and displays the list of risky users. 4. Navigate to Protection > Identity Protection > Risky sign-ins and verify the page loads successfully. 5. Optionally, run the Microsoft Graph API query: GET https://graph.microsoft.com/v1.0/identityProtection/riskyUsers and verify a 200 OK response with user data.

## Rollback
1. If the validation fails, sign out of the current account and sign in with an account that has the required role (Security Reader, Security Operator, or Security Administrator). 2. If the error persists, ensure you are in the correct tenant directory by checking the directory switcher in the top-right corner of the Microsoft Entra admin center and selecting the correct tenant. 3. If the issue remains, verify role assignments in Microsoft Entra ID > Roles & admins and assign the appropriate role to your account if missing.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk>
