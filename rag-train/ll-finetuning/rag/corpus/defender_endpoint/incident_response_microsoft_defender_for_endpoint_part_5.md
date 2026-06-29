# Incident Response: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Incident Response

## Scenario / Query
How do I isolate a compromised device from the network to prevent lateral movement and data exfiltration?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Web proxy environments (PAC, WPAD, static/direct proxy) may prevent recovery from full isolation; use selective isolation instead.

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Isolate the device from the network using the device isolation capability in Microsoft Defender for Endpoint.
2. In environments that use web proxies (including Proxy Auto Configuration (PAC), WPAD, or static/direct proxy configurations), use selective isolation instead of full isolation to ensure devices can recover.
3. For macOS, device isolation is supported for client version 101.98.84 and above.
4. For Linux, ensure the following prerequisites are enabled: iptables, ip6tables, and Linux kernel with CONFIG_NETFILTER, CONFIG_IP_NF_IPTABLES, and CONFIG_IP_NF_MATCH_OWNER for kernel version lower than 5.x, or CONFIG_NETFILTER_XT_MATCH_OWNER from 5.x kernel.
5. Full isolation is available for devices running Windows 11, Windows 10 version 1703 or later, Windows Server 2012 R2 and later, and Azure Stack HCI OS version 23H2 and later.
6. Device isolation is supported when Defender is running in passive mode on all supported Windows, macOS, and Linux operating systems.
7. You can also use live response to run the isolation action.

## Validation
1. In Microsoft Defender for Endpoint portal, navigate to the device page and verify the 'Isolation status' shows 'Isolated' or 'Selectively isolated' as appropriate. 2. From a separate management console, attempt to ping or establish a network connection to the isolated device; confirm the connection fails. 3. For macOS, run 'mdatp health --details isolation' on the device and confirm 'isolationStatus' is 'full' or 'selective'. 4. For Linux, run 'sudo mdatp health --details isolation' and verify 'isolationStatus' is 'full' or 'selective'. 5. Check the device timeline in Defender for Endpoint for an 'Isolation' event with status 'Success'.

## Rollback
1. In Microsoft Defender for Endpoint portal, navigate to the device page and select 'Release from isolation'. 2. For live response, run the command 'release from isolation' on the device. 3. After release, verify network connectivity by pinging the device from a separate management console. 4. For macOS, run 'mdatp health --details isolation' and confirm 'isolationStatus' is 'none'. 5. For Linux, run 'sudo mdatp health --details isolation' and confirm 'isolationStatus' is 'none'. 6. Check the device timeline for a 'Release from isolation' event with status 'Success'.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
