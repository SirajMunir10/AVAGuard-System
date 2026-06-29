# Troubleshooting: Password Reset (SSPR_0029)

**Domain:** Entra ID
**Subdomain:** Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve SSPR_0029 error indicating on-premises configuration for password reset is not properly set up?

## Environment Context
- **Tenant Type:** Entra ID with on-premises Active Directory
- **Configuration:** Password writeback configuration

## Symptoms
- Error SSPR_0029: Your organization hasn't properly set up the on-premises configuration for password reset

## Error Codes
- `SSPR_0029`

## Root Causes
1. The MSOL_XXXXXXX management account is not included as an allowed user in the policy

## Remediation Steps
1. Edit the policy to include the MSOL_XXXXXXX management account as an allowed user

## Validation
1. Verify that the MSOL_XXXXXXX management account is listed as an allowed user in the password writeback policy: Open the Azure AD Connect Synchronization Rules Editor, navigate to the 'Outbound – AAD to AD – Password Writeback' rule, and confirm the 'Allowed Users' attribute includes the MSOL_XXXXXXX account. 2. Trigger a test password reset for a user synced from on-premises and confirm no SSPR_0029 error appears. 3. Check the Event Viewer on the Azure AD Connect server for successful password writeback events (Event ID 31000).

## Rollback
1. Remove the MSOL_XXXXXXX management account from the 'Allowed Users' list in the password writeback policy using the Azure AD Connect Synchronization Rules Editor. 2. Re-run the Azure AD Connect synchronization wizard to apply the change. 3. Verify that the SSPR_0029 error reoccurs by attempting a password reset for a synced user.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
