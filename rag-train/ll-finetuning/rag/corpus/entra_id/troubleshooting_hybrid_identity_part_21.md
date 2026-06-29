# Troubleshooting: Hybrid Identity

**Domain:** Entra ID
**Subdomain:** Hybrid Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Authentication Agent errors using Event Viewer logs?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Pass-through Authentication

## Symptoms
- Authentication Agent errors

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Open the Event Viewer application on the server.
2. Navigate to Application and Service Logs\Microsoft\AzureAdConnect\AuthenticationAgent\Admin.
3. For detailed analytics, enable the 'Session' log by right-clicking inside the Event Viewer application.
4. Do not run the Authentication Agent with the Session log enabled during normal operations; use only for troubleshooting.
5. Note: The log contents are only visible after the log is disabled again.

## Validation
1. Open Event Viewer on the server. 2. Navigate to 'Application and Service Logs\Microsoft\AzureAdConnect\AuthenticationAgent\Admin'. 3. Verify that no new error events (Event ID 1, 2, or 3) are present. 4. If troubleshooting is complete, ensure the 'Session' log is disabled (right-click the 'Session' log and select 'Disable Log'). 5. Confirm that the Authentication Agent service is running (Run 'Get-Service AzureADConnectAuthenticationAgent' and verify Status is 'Running').

## Rollback
1. If errors persist, re-enable the 'Session' log for detailed troubleshooting: right-click inside Event Viewer, select 'View', then 'Show Analytic and Debug Logs', right-click 'Session' log, and select 'Enable Log'. 2. Collect the session log entries. 3. After collection, disable the 'Session' log immediately to avoid performance impact. 4. If the Authentication Agent service is not running, start it with 'Start-Service AzureADConnectAuthenticationAgent'. 5. If issues continue, refer to the official troubleshooting guide at https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-pass-through-authentication.

## References
- <https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-pass-through-authentication>
