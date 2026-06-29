# Troubleshooting: Pass-through Authentication (SIGN-IN ERROR CODE)

**Domain:** Entra ID
**Subdomain:** Pass-through Authentication
**Incident Type:** Troubleshooting

## Scenario / Query
How to diagnose sign-in failures for Pass-through Authentication using the Microsoft Entra admin center sign-in activity report?

## Environment Context
- **Tenant Type:** Microsoft Entra ID P1 or P2 license required
- **Configuration:** Pass-through Authentication enabled

## Symptoms
- User sign-in failures

## Error Codes
- `SIGN-IN ERROR CODE`

## Root Causes
1. User's Active Directory password has expired
2. No Authentication Agent available
3. Authentication Agent's password validation request timed out
4. Invalid response received by Authentication Agent
5. Incorrect User Principal Name (UPN) used in sign-in request
6. Authentication Agent: Error occurred (transient error)
7. Authentication Agent unable to connect to Active Directory
8. Authentication Agent unable to decrypt password
9. Authentication Agent unable to retrieve decryption key
10. Validation request responded after maximum elapsed time exceeded

## Remediation Steps
1. Reset the user's password in your on-premises Active Directory
2. Install and register an Authentication Agent
3. Check if your Active Directory is reachable from the Authentication Agent
4. If the problem is consistently reproducible across multiple users, check your Active Directory configuration
5. Ask the user to sign in with the correct username
6. Transient error: Try again later
7. Check if your Active Directory is reachable from the Authentication Agent
8. If the problem is consistently reproducible, install and register a new Authentication Agent and uninstall the current one
9. If the problem is consistently reproducible, install and register a new Authentication Agent and uninstall the current one
10. Open a support ticket with the error code, correlation ID, and timestamp to get more details on this error

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-pass-through-authentication>
