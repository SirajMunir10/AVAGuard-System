# Troubleshooting: Password Writeback

**Domain:** Entra ID
**Subdomain:** Password Writeback
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot password writeback not working due to Service Bus listener issues?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Microsoft Entra Connect with password writeback enabled

## Symptoms
- PasswordResetService event indicating password writeback isn't working
- Writeback client returns an error if either Service Host isn't running

## Error Codes
N/A

## Root Causes
1. Service Bus listens for requests on two separate relays for redundancy; each relay connection is managed by a unique Service Host
2. Either Service Host isn't running

## Remediation Steps
1. Try disabling and then re-enabling password writeback
2. If this doesn't help, include a copy of your event log along with the tracking ID specified when you open a support request

## Validation
1. Open Event Viewer and navigate to 'Applications and Services Logs > Microsoft > Windows > PasswordResetService'. Verify that no error events (Event ID 31001 or similar) related to Service Bus listener or writeback failure are present. 2. Run 'Get-Service -Name *AzureAD*' on the Microsoft Entra Connect server and confirm that both Service Host services (e.g., 'Azure AD Connect Password Writeback Service Host 1' and 'Azure AD Connect Password Writeback Service Host 2') are in 'Running' state. 3. Initiate a test password reset from the on-premises environment and confirm the password is written back to Microsoft Entra ID within a few minutes.

## Rollback
1. Re-enable password writeback in Microsoft Entra Connect by running the Azure AD Connect wizard, selecting 'Customize synchronization options', and ensuring the 'Password writeback' checkbox is checked. 2. Restart both Service Host services using 'Restart-Service -Name *AzureAD*PasswordWriteback*' (or the exact service names from the environment). 3. If the issue persists, collect the event logs (Applications and Services Logs > Microsoft > Windows > PasswordResetService) and the tracking ID from the error, then open a support request with Microsoft as documented.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
