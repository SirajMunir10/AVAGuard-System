# Troubleshooting: Network Connectivity (ERROR_WINHTTP_TIMEOUT (12002))

**Domain:** Entra ID
**Subdomain:** Network Connectivity
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve network-related errors (ERROR_WINHTTP_TIMEOUT, ERROR_WINHTTP_NAME_NOT_RESOLVED, ERROR_WINHTTP_CANNOT_CONNECT, ERROR_WINHTTP_CONNECTION_ERROR) during hybrid join?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** outbound proxy required in on-premises environment

## Symptoms
- Events 1022 (Microsoft Entra analytics logs) and 1084 (Microsoft Entra operational logs) contain the URL being accessed

## Error Codes
- `ERROR_WINHTTP_TIMEOUT (12002)`
- `ERROR_WINHTTP_NAME_NOT_RESOLVED (12007)`
- `ERROR_WINHTTP_CANNOT_CONNECT (12029)`
- `ERROR_WINHTTP_CONNECTION_ERROR (12030)`

## Root Causes
1. Common general network-related issues
2. Outbound proxy requires discovery and silent authentication by the device computer account

## Remediation Steps
1. Ensure that the computer account of the device can discover and silently authenticate to the outbound proxy

## Validation
1. On a domain-joined Windows device, open an elevated PowerShell prompt and run: 'netsh winhttp show proxy'. Verify that the proxy server address and port are correctly configured. 2. Run: 'Test-NetConnection -ComputerName <your_proxy_server> -Port <proxy_port>' to confirm connectivity to the proxy. 3. Check Event Viewer > Applications and Services Logs > Microsoft > Windows > User Device Registration > Admin for Event ID 1022 and 1084; ensure no ERROR_WINHTTP_TIMEOUT, ERROR_WINHTTP_NAME_NOT_RESOLVED, ERROR_WINHTTP_CANNOT_CONNECT, or ERROR_WINHTTP_CONNECTION_ERROR entries appear. 4. Run: 'dsregcmd /status' and confirm that the device shows 'AzureAdJoined : YES' and 'DomainJoined : YES'.

## Rollback
1. If proxy settings were changed, revert to the original proxy configuration by running: 'netsh winhttp reset proxy' (if no proxy was previously set) or 'netsh winhttp set proxy <original_proxy>:<original_port>' (if a proxy was previously configured). 2. If Group Policy was used to set proxy settings, remove or revert the policy to its previous state. 3. Restart the device to ensure all changes take effect. 4. Re-run 'dsregcmd /status' to confirm the device returns to its previous join state.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
