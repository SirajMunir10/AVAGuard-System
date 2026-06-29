# Troubleshooting: Hybrid Join (0x80072ee7)

**Domain:** Entra ID
**Subdomain:** Hybrid Join
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve WININET_E_NAME_NOT_RESOLVED (0x80072ee7/-2147012889) error during Microsoft Entra hybrid join?

## Environment Context
- **Tenant Type:** Microsoft Entra hybrid joined
- **Configuration:** N/A

## Symptoms
- WININET_E_NAME_NOT_RESOLVED (0x80072ee7/-2147012889) error

## Error Codes
- `0x80072ee7`
- `-2147012889`

## Root Causes
1. The server name or address couldn't be resolved

## Remediation Steps
1. Check network connectivity to https://enterpriseregistration.windows.net

## Validation
1. On the affected device, open a web browser and navigate to https://enterpriseregistration.windows.net. Confirm the page loads without errors. 2. Run 'nslookup enterpriseregistration.windows.net' from a command prompt and verify it returns a valid IP address. 3. Run 'Test-NetConnection enterpriseregistration.windows.net -Port 443' in PowerShell and confirm TcpTestSucceeded is True. 4. Check the device's proxy or firewall logs to ensure traffic to *.msappproxy.net and *.windows.net is allowed. 5. Re-attempt the hybrid join process and verify no WININET_E_NAME_NOT_RESOLVED error appears.

## Rollback
1. If the remediation causes connectivity issues, restore previous proxy or firewall rules that were blocking the URLs. 2. If DNS changes were made, revert to the original DNS server settings. 3. If network configuration was modified, use the 'netsh interface ip reset' command to reset TCP/IP stack to defaults. 4. Re-run the hybrid join process and confirm the original error persists, indicating rollback was successful.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
