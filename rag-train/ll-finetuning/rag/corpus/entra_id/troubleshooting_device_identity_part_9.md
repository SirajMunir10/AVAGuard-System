# Troubleshooting: Device Identity (E_INVALIDDATA (0x8007000d/-2147024883))

**Domain:** Entra ID
**Subdomain:** Device Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to fix E_INVALIDDATA error during Microsoft Entra hybrid join?

## Environment Context
- **Tenant Type:** federated
- **Configuration:** On-premises environment with outbound proxy

## Symptoms
- Server response JSON couldn't be parsed

## Error Codes
- `E_INVALIDDATA (0x8007000d/-2147024883)`

## Root Causes
1. Proxy returning an HTTP 200 with an HTML authorization page

## Remediation Steps
1. If the on-premises environment requires an outbound proxy, the IT admin must ensure that the system context on the device can discover and silently authenticate to the outbound proxy.

## Validation
1. On the affected device, open an elevated PowerShell console and run: `netsh winhttp show proxy` to confirm the proxy is configured for the system context. 2. Verify the proxy does not intercept or modify traffic to *.msappproxy.net and *.manage.microsoft.com by running: `curl -v https://enterpriseregistration.windows.net` and checking that the response is a valid JSON (not an HTML page). 3. Run `dsregcmd /status` and confirm that the 'AzureAdJoined' field shows 'YES' and 'DomainJoined' shows 'YES'. 4. Check the Event Viewer under Applications and Services Logs > Microsoft > Windows > User Device Registration > Admin for Event ID 304 (successful registration).

## Rollback
1. If the proxy configuration causes issues, remove the system-level proxy by running in an elevated command prompt: `netsh winhttp reset proxy`. 2. Revert any changes made to proxy bypass lists or authentication settings. 3. Restart the device and verify that the original connectivity (e.g., to on-premises resources) is restored. 4. If hybrid join was partially completed, run `dsregcmd /leave` to unjoin the device from Azure AD, then reattempt the join after correcting the proxy configuration.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
