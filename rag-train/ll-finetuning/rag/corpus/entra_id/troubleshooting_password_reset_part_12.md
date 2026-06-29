# Troubleshooting: Password Reset

**Domain:** Entra ID
**Subdomain:** Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
How to fix password writeback service failing to restart after Microsoft Entra Connect restart?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Microsoft Entra Connect with password writeback enabled

## Symptoms
- After working for some time, federated, pass-through authentication, or password-hash-synchronized users can't reset their passwords
- Password writeback service fails to restart when Microsoft Entra Connect has restarted

## Error Codes
N/A

## Root Causes
1. Password writeback service fails to restart in some rare cases

## Remediation Steps
1. Check if password writeback is enabled on-premises using the Microsoft Entra Connect wizard or PowerShell
2. If the feature appears to be enabled, try enabling or disabling the feature again
3. If the above step doesn't work, try a complete uninstall and reinstall of Microsoft Entra Connect

## Validation
1. Sign in to the Microsoft Entra Connect server as an administrator. 2. Open the Microsoft Entra Connect wizard and select 'View current configuration' to confirm that password writeback is enabled. 3. Alternatively, run PowerShell as administrator and execute: `Get-ADSyncAADPasswordWritebackConfiguration | fl Enabled`. Verify the output shows 'Enabled : True'. 4. On a test user account that is synchronized from on-premises, initiate a password reset from the Microsoft Entra portal (https://passwordreset.microsoftonline.com). 5. Confirm that the password reset completes successfully and the user can sign in with the new password. 6. Check the Windows Event Viewer on the Microsoft Entra Connect server under 'Applications and Services Logs > Microsoft > AzureADConnect > ADSync' for any error events related to password writeback.

## Rollback
1. If the remediation steps cause issues (e.g., password writeback stops working), first re-enable password writeback using the Microsoft Entra Connect wizard: select 'Customize synchronization options', then under 'Optional features', check 'Password writeback' and complete the wizard. 2. If the feature was toggled off and on, toggle it off and then on again using the same wizard. 3. If a complete uninstall and reinstall was performed, restore the previous Microsoft Entra Connect configuration by running the installer and selecting 'Restore from a backup' if a backup was taken, or reconfigure the connection and synchronization settings manually. 4. After any rollback action, run the validation steps to confirm password writeback is functioning correctly.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
