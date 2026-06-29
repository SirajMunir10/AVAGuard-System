# Troubleshooting: Device Identity

**Domain:** Entra ID
**Subdomain:** Device Identity
**Incident Type:** Troubleshooting

## Scenario / Query
Why does Microsoft Entra hybrid join fail on a down-level Windows device with the error 'You aren't signed on as a domain user'?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Down-level Windows device, hybrid join

## Symptoms
- You aren't signed on as a domain user

## Error Codes
N/A

## Root Causes
1. The signed in user isn't a domain user (for example, a local user). Microsoft Entra hybrid join on down-level devices is supported only for domain users.
2. The client isn't able to connect to a domain controller.

## Remediation Steps
1. Ensure the user is signed on as a domain user, not a local user.
2. Verify the client can connect to a domain controller.

## Validation
1. Confirm the user is signed on with a domain account: run 'whoami' and verify the output shows a domain\username format (e.g., CONTOSO\jdoe).
2. Test connectivity to a domain controller: run 'nltest /dsgetdc:DOMAIN_NAME' (replace DOMAIN_NAME with your domain) and confirm it returns a domain controller name and status 'DC has DS'. Alternatively, run 'ping <DC_IP>' and 'Test-ComputerSecureChannel -Server <DC_NAME>' in PowerShell.
3. Verify the device can resolve the domain: run 'nslookup <domain_name>' and confirm it returns a valid IP address of a domain controller.

## Rollback
1. If the user was incorrectly signed in as a local user, sign out and sign in again as a domain user (e.g., DOMAIN\username).
2. If connectivity to a domain controller fails, check network settings: ensure the device is on the corporate network or VPN, verify DNS settings point to internal DNS servers that can resolve the domain, and check firewall rules allow traffic to the domain controller (e.g., LDAP, Kerberos).
3. If the domain controller is unreachable, contact your network administrator to restore connectivity or use an alternate domain controller.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-legacy>
