# Troubleshooting: Hybrid Identity

**Domain:** Entra ID
**Subdomain:** Hybrid Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve token or account authorization errors when enabling Pass-Through Authentication in Entra ID?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Pass-Through Authentication feature enabling

## Symptoms
- Enabling the feature failed due to token or account authorization errors

## Error Codes
N/A

## Root Causes
1. Using a non-cloud-only Hybrid Identity Administrator account
2. Multi-factor authentication (MFA) enabled on the Hybrid Identity Administrator account

## Remediation Steps
1. Ensure that you use a cloud-only Hybrid Identity Administrator account when enabling the feature.
2. If the account has MFA enabled, turn off MFA temporarily (only to complete the operation) as a workaround.

## Validation
1. Sign in to the Entra admin center using a cloud-only Hybrid Identity Administrator account (e.g., admin@contoso.onmicrosoft.com).
2. Navigate to Identity > Hybrid management > Azure AD Connect > Pass-through authentication.
3. Verify that the status shows 'Enabled' and no errors are displayed.
4. Run the following PowerShell command as a global administrator to confirm the feature state:
   Get-MsolCompanyInformation | Select-Object -ExpandProperty AuthenticationMethods
   Confirm that 'PassThroughAuthentication' appears in the list.
5. If MFA was temporarily disabled, re-enable MFA for the account and confirm that authentication still works.

## Rollback
1. If enabling Pass-Through Authentication fails again, disable the feature:
   - In the Entra admin center, go to Identity > Hybrid management > Azure AD Connect > Pass-through authentication and click 'Disable'.
2. If MFA was turned off as a workaround and the operation still fails, re-enable MFA for the Hybrid Identity Administrator account immediately.
3. Verify that the account used is cloud-only (not synchronized from on-premises). If it is not, create a new cloud-only Hybrid Identity Administrator account (e.g., admin@contoso.onmicrosoft.com) and retry the enablement.
4. If the issue persists, review the Pass-Through Authentication troubleshooting guide at https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-pass-through-authentication and check for other prerequisites such as Azure AD Connect health status.

## References
- <https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-pass-through-authentication>
