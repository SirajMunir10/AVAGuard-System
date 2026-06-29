# Troubleshooting: Device Registration (STATUS_NETWORK_UNREACHABLE (-1073741252/ 0xc000023c))

**Domain:** Entra ID
**Subdomain:** Device Registration
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Microsoft Entra hybrid join failures on Windows current devices when encountering STATUS_NETWORK_UNREACHABLE (-1073741252/0xc000023c), STATUS_BAD_NETWORK_PATH (-1073741634/0xc00000be), or STATUS_UNEXPECTED_NETWORK_ERROR (-1073741628/0xc00000c4)?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Federated authentication with WS-Trust endpoint

## Symptoms
- Received an error response (HTTP > 400) from the Microsoft Entra authentication service or WS-Trust endpoint

## Error Codes
- `STATUS_NETWORK_UNREACHABLE (-1073741252/ 0xc000023c)`
- `STATUS_BAD_NETWORK_PATH (-1073741634/ 0xc00000be)`
- `STATUS_UNEXPECTED_NETWORK_ERROR (-1073741628/ 0xc00000c4)`

## Root Causes
1. Network connectivity issue to a required endpoint

## Remediation Steps
N/A

## Validation
1. Verify network connectivity to the required endpoints: Test-NetConnection -ComputerName enterpriseregistration.microsoft.com -Port 443. 2. Confirm WS-Trust endpoint reachability: Test-NetConnection -ComputerName sts.yourdomain.com -Port 443 (replace with your actual federation server). 3. Check that the device can resolve DNS for the endpoints: Resolve-DnsName enterpriseregistration.microsoft.com. 4. Run dsregcmd /status and confirm the 'AzureAdJoined' status is 'YES' and 'DomainJoined' is 'YES'. 5. Review the dsregcmd /status output for any error codes under 'Previous Registration' or 'Last Error'.

## Rollback
1. If network changes were made (e.g., firewall rules, proxy settings), revert those changes to the previous configuration. 2. If DNS records were modified, restore the original DNS entries. 3. If the device was manually unjoined from Azure AD, rejoin it using: dsregcmd /join. 4. If the device was removed from the local domain, rejoin it to the domain using standard domain join procedures. 5. If the WS-Trust endpoint was disabled or modified, re-enable or restore the original endpoint configuration.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
