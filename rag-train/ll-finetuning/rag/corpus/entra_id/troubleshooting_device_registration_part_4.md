# Troubleshooting: Device Registration (0xc000006d)

**Domain:** Entra ID
**Subdomain:** Device Registration
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Azure AD Primary Refresh Token (PRT) acquisition failure with error AADSTS50126?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** Device joined to Entra ID or hybrid Azure AD joined

## Symptoms
- AzureAdPrt is NO
- AcquirePrtDiagnostics is PRESENT
- Attempt Status is 0xc000006d
- HTTP status is 400
- Server Error Code is invalid_grant
- Server Error Description is AADSTS50126: Error validating credentials due to invalid username or password

## Error Codes
- `0xc000006d`
- `invalid_grant`
- `AADSTS50126`

## Root Causes
1. Invalid username or password provided during PRT acquisition

## Remediation Steps
1. Verify the user identity (e.g., john@contoso.com) and credential type (Password) from the dsregcmd /status output
2. Check the correlation ID (aaaa0000-bb11-2222-33cc-444444dddddd) in Entra ID sign-in logs for more details
3. Ensure the user enters the correct password and that the account is not locked or disabled

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-device-dsregcmd>
