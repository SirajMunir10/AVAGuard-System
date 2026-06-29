# Troubleshooting: Password Reset (DecryptionError)

**Domain:** Entra ID
**Subdomain:** Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve DecryptionError during SSPR writeback?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** SSPR writeback

## Symptoms
- Error decrypting the password that arrived from the cloud

## Error Codes
- `DecryptionError`

## Root Causes
1. Decryption key mismatch between the cloud service and your on-premises environment

## Remediation Steps
1. Disable and then re-enable password writeback in your on-premises environment

## Validation
1. On the Entra ID Connect server, open PowerShell as Administrator and run: `Get-ADSyncGlobalSettings | Select-Object -ExpandProperty Parameters | Where-Object {$_.Name -like '*PasswordWriteback*'}` to confirm the password writeback feature is enabled. 2. In the Entra admin center, navigate to Protection > Password reset > Properties and verify that 'Password writeback' is set to 'Yes'. 3. Trigger a test SSPR for a user and confirm no DecryptionError appears in the audit logs.

## Rollback
1. On the Entra ID Connect server, open the Synchronization Service Manager. 2. Under the Connectors tab, select the on-premises AD connector and click Properties. 3. In the Properties dialog, navigate to the 'Configure Password Reset' tab and uncheck 'Enable password writeback for this Active Directory forest'. 4. Click OK to save the change. 5. Re-enable password writeback by checking the same box and clicking OK. 6. Run a full synchronization cycle to restore the original state.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
