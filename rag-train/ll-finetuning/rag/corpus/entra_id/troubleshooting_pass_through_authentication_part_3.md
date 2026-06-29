# Troubleshooting: Pass-through Authentication (1328)

**Domain:** Entra ID
**Subdomain:** Pass-through Authentication
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot user sign-in failures in Pass-through Authentication using trace logs?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Azure AD Connect Pass-through Authentication Agent

## Symptoms
- User sign-in failures with Pass-through Authentication

## Error Codes
- `1328`

## Root Causes
1. Pass-through Authentication request failed with specific error code

## Remediation Steps
1. Look for trace logs at %ProgramData%\Microsoft\Azure AD Connect Authentication Agent\Trace\
2. Open command prompt and run: Net helpmsg 1328 (replace 1328 with actual error number from logs)

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-pass-through-authentication>
