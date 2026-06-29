# Troubleshooting: Pass-through Authentication (AADSTS80001)

**Domain:** Entra ID
**Subdomain:** Pass-through Authentication
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot user-facing sign-in errors for Pass-through Authentication?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Pass-through Authentication enabled

## Symptoms
- User sees error AADSTS80001 on Microsoft Entra sign-in screen
- User sees error AADSTS80002 on Microsoft Entra sign-in screen
- User sees error AADSTS80004 on Microsoft Entra sign-in screen
- User sees error AADSTS80005 on Microsoft Entra sign-in screen
- User sees error AADSTS80007 on Microsoft Entra sign-in screen

## Error Codes
- `AADSTS80001`
- `AADSTS80002`
- `AADSTS80004`
- `AADSTS80005`
- `AADSTS80007`

## Root Causes
1. AADSTS80001: Agent servers are not members of the same AD forest as the users whose passwords need to be validated or unable to connect to Active Directory
2. AADSTS80002: Active Directory is not available or not responding to requests from the agents
3. AADSTS80004: The username passed to the agent was not valid
4. AADSTS80005: Unpredictable WebException (transient error)
5. AADSTS80007: Error communicating with Active Directory

## Remediation Steps
1. For AADSTS80001: Ensure that agent servers are members of the same AD forest as the users whose passwords need to be validated and they are able to connect to Active Directory
2. For AADSTS80002: Check to ensure that Active Directory is available and is responding to requests from the agents
3. For AADSTS80004: Ensure the user is attempting to sign in with the right username
4. For AADSTS80005: Retry the request. If it continues to fail, contact Microsoft support
5. For AADSTS80007: Check the agent logs for more information and verify that Active Directory is operating as expected

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-pass-through-authentication>
