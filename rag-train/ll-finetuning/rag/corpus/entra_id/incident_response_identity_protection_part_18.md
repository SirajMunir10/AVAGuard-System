# Incident Response: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Incident Response

## Scenario / Query
How to confirm a user is compromised in Entra ID Identity Protection and what actions to take?

## Environment Context
- **Tenant Type:** Entra ID tenant with Identity Protection enabled
- **Configuration:** Risk-based policies may or may not be triggered; continuous access evaluation may be enabled

## Symptoms
- Sign-in or user is identified as at risk in Risky sign-ins or Risky users reports

## Error Codes
N/A

## Root Causes
1. User account or sign-in activity is confirmed as compromised after investigation

## Remediation Steps
1. Select the event or user in the Risky sign-ins or Risky users reports and choose Confirm compromised
2. Request a password change
3. Block the user if you suspect the attacker can reset the password or do multifactor authentication for the user
4. Revoke refresh tokens
5. Disable any devices that are considered compromised
6. If using continuous access evaluation, revoke all access tokens

## Validation
1. Navigate to the Entra admin center > Protection > Identity Protection > Risky users. Verify the user's risk level is now 'Confirmed compromised' and the 'Risk state' is 'Confirmed compromised'. 2. Check the user's sign-in logs to confirm no recent successful sign-ins after the remediation. 3. Verify the user's password change was enforced by checking the 'Last password change' timestamp in the user's profile. 4. Confirm the user is blocked from sign-in by reviewing the 'Sign-in blocked' status in the user's properties. 5. Use Microsoft Graph PowerShell: `Get-MgUser -UserId 'user@domain.com' | Select-Object DisplayName, UserPrincipalName, AccountEnabled` to ensure AccountEnabled is $false if blocked. 6. Validate refresh token revocation by running: `Revoke-MgUserSignInSession -UserId 'user@domain.com'` and confirming no errors. 7. Check continuous access evaluation (CAE) token revocation by reviewing sign-in logs for 'Token issued' events with 'Token type' = 'Access Token' and verifying they are revoked.

## Rollback
1. If the user was incorrectly confirmed as compromised, navigate to Identity Protection > Risky users, select the user, and choose 'Dismiss user risk' to revert the risk state. 2. If the user was blocked, re-enable the account: In Entra admin center > Users > select user > uncheck 'Block sign in' or use PowerShell: `Update-MgUser -UserId 'user@domain.com' -AccountEnabled $true`. 3. If a password change was forced and the user cannot authenticate, an admin can reset the password: In Entra admin center > Users > select user > Reset password. 4. To restore revoked refresh tokens, the user must sign in again; no direct rollback exists. 5. For revoked access tokens via CAE, the user must re-authenticate; no direct rollback. 6. If a device was disabled, re-enable it in Entra admin center > Devices > select device > Enable.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock>
