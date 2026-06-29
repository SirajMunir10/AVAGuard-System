# Troubleshooting: Password Writeback

**Domain:** Entra ID
**Subdomain:** Password Writeback
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve ServiceBusError due to blocked outbound connections?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Microsoft Entra Connect with password writeback enabled

## Symptoms
- ServiceBusError event indicating error connecting to your tenant's Service Bus instance

## Error Codes
N/A

## Root Causes
1. Blocking outbound connections in your on-premises environment

## Remediation Steps
1. Check your firewall to ensure that you allow connections over TCP 443
2. Allow connections to https://ssprdedicatedsbprodncu.servicebus.windows.net
3. Try again
4. If still having problems, try disabling and then re-enabling password writeback

## Validation
1. On the Microsoft Entra Connect server, open PowerShell as Administrator and run: Test-NetConnection -ComputerName ssprdedicatedsbprodncu.servicebus.windows.net -Port 443. Verify the output shows TcpTestSucceeded: True.
2. In the Microsoft Entra admin center, navigate to Protection > Password reset > Properties, and confirm Password writeback is set to Yes.
3. Trigger a password reset for a test user synced from on-premises and verify the change is written back successfully (check the user's on-premises account password is updated).
4. Review the Microsoft Entra Connect event logs (Event Viewer > Applications and Services Logs > Microsoft > Azure AD Connect) for any recent ServiceBusError events; confirm no new errors appear.

## Rollback
1. If the issue persists after allowing outbound connections, disable password writeback: In the Microsoft Entra admin center, go to Protection > Password reset > Properties, set Password writeback to No, and save.
2. On the Microsoft Entra Connect server, run the Microsoft Entra Connect wizard, select Customize synchronization options, and on the Optional features page, uncheck Password writeback. Complete the wizard.
3. Re-enable password writeback by following the same steps in reverse: in the wizard, check Password writeback, and in the admin center, set Password writeback to Yes.
4. If the problem continues, verify that no other firewall or proxy rules are blocking outbound TCP 443 to *.servicebus.windows.net and that the service endpoint is not restricted by your network policy.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
