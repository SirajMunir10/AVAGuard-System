# Troubleshooting: Device Identity

**Domain:** Entra ID
**Subdomain:** Device Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot HTTP > 400 error responses from Microsoft Entra authentication service or WS-Trust endpoint during hybrid join?

## Environment Context
- **Tenant Type:** federated
- **Configuration:** WS-Trust required for federated authentication

## Symptoms
- Received an error response (HTTP > 400) from the Microsoft Entra authentication service or WS-Trust endpoint

## Error Codes
N/A

## Root Causes
1. Network connectivity issue to a required endpoint
2. Server error from Microsoft Entra authentication service or WS-Trust endpoint

## Remediation Steps
1. For server errors, check events 1081 and 1088 (Microsoft Entra operational logs) for the error code from the Microsoft Entra authentication service and the error description from the WS-Trust endpoint
2. For connectivity issues, check event 1022 (Microsoft Entra analytics logs) for the URL being accessed, and event 1084 (Microsoft Entra operational logs) for the suberror code from the network stack

## Validation
1. Open Event Viewer and navigate to Applications and Services Logs > Microsoft > Windows > User Device Registration > Admin. Verify that events 1081 and 1088 are present with no error codes indicating server failures. 2. Check event 1022 in the same log to confirm the URL accessed is a valid Microsoft Entra endpoint (e.g., https://enterpriseregistration.windows.net). 3. Verify event 1084 shows a suberror code of 0 (no network stack error). 4. Run 'dsregcmd /status' and confirm the device state shows 'AzureAdJoined : YES' and 'DomainJoined : YES'.

## Rollback
1. If validation fails, revert any recent network changes (e.g., firewall rules, proxy settings) that may have blocked access to required endpoints. 2. Restore original DNS settings if modified. 3. If WS-Trust endpoint was disabled, re-enable it in AD FS or federation server configuration. 4. Re-run 'dsregcmd /leave' and then 'dsregcmd /join' to re-initiate hybrid join if the device state is incorrect.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
