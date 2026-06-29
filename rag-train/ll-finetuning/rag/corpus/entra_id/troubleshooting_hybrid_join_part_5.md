# Troubleshooting: Hybrid Join (0x80072ee2)

**Domain:** Entra ID
**Subdomain:** Hybrid Join
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve WININET_E_TIMEOUT (0x80072ee2/-2147012894) error during Microsoft Entra hybrid join?

## Environment Context
- **Tenant Type:** Microsoft Entra hybrid joined
- **Configuration:** N/A

## Symptoms
- WININET_E_TIMEOUT (0x80072ee2/-2147012894) error

## Error Codes
- `0x80072ee2`
- `-2147012894`

## Root Causes
1. General network time out trying to register the device at DRS

## Remediation Steps
1. Check network connectivity to https://enterpriseregistration.windows.net

## Validation
1. On the affected device, open a web browser and navigate to https://enterpriseregistration.windows.net. Verify that the page loads without timeout errors. 2. Run the following PowerShell command as Administrator: Test-NetConnection -ComputerName enterpriseregistration.windows.net -Port 443. Confirm the output shows TcpTestSucceeded: True. 3. Check the device registration status by running: dsregcmd /status. Ensure the 'AzureAdJoined' field shows 'YES' and 'DomainJoined' shows 'YES'.

## Rollback
1. If the remediation fails, restore any previous network proxy or firewall settings that were modified to allow connectivity to https://enterpriseregistration.windows.net. 2. If network changes were made, revert to the original DNS or routing configuration. 3. If the device was manually unjoined from Azure AD, rejoin it using: dsregcmd /join.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
