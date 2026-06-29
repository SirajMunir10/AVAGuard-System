# Implementation: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Implementation

## Scenario / Query
How can hybrid users complete a password change from an on-premises or hybrid joined Windows device to remediate user risk?

## Environment Context
- **Tenant Type:** Microsoft Entra ID tenant with Identity Protection and hybrid identity setup
- **Configuration:** Password hash synchronization enabled; 'Allow on-premises password change to reset user risk' setting enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Hybrid users can complete a password change from an on-premises or hybrid joined Windows device
2. Requires password hash synchronization to be enabled
3. Requires the 'Allow on-premises password change to reset user risk' setting to be enabled

## Validation
1. Confirm that password hash synchronization is enabled: run `Get-MsolDirSyncFeatures | Select-Object PasswordHashSync` in Azure AD PowerShell or check via Entra admin center > Azure AD Connect > Cloud sync > Password hash sync status.
2. Verify the 'Allow on-premises password change to reset user risk' setting is enabled: navigate to Entra admin center > Identity Protection > User risk policy > Settings > 'Allow on-premises password change to reset user risk' must be set to 'Yes'.
3. On a hybrid-joined Windows device, have the user press Ctrl+Alt+Del and select 'Change a password'. After the password is changed and synced, confirm the user's risk level in Identity Protection > Risky users shows the user's risk is remediated (risk state changes to 'Remediated' or risk level drops to 'None').

## Rollback
1. Disable the 'Allow on-premises password change to reset user risk' setting: in Entra admin center > Identity Protection > User risk policy > Settings, set 'Allow on-premises password change to reset user risk' to 'No'.
2. If password hash synchronization is causing issues, temporarily disable it: in Azure AD Connect, uncheck 'Password hash synchronization' and run a sync cycle, or disable via PowerShell with `Set-MsolDirSyncFeature -Feature PasswordHashSync -Enable $false`.
3. If the password change itself caused account lockout or sync delays, instruct the user to reset their password again via the on-premises domain controller using standard domain password reset procedures, then force a delta sync with `Start-ADSyncSyncCycle -PolicyType Delta`.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock>
