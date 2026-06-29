# Troubleshooting: Microsoft Defender for Endpoint (ERROR: The system was unable to find the specified registry key or value.)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate a Windows device alert using the investigation package in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Windows devices

## Symptoms
- Suspicious connectivity made by a process
- Potential attacker persistency on the device
- Suspicious URLs or command and control infrastructure
- Lateral movement or remote connections

## Error Codes
- `ERROR: The system was unable to find the specified registry key or value.`

## Root Causes
1. Registry key for auto start entry point (ASEP) not found
2. Suspicious network connections to unknown URLs or C&C infrastructure
3. Compromised hosts on the network identified via ARP cache
4. Recently used files indicating deleted applications

## Remediation Steps
1. Collect the investigation package for the Windows device
2. Review the ASEP registry files to identify attacker persistency; if registry key is missing, note the error message
3. Analyze Installed programs CSV file to identify suspicious software
4. Examine ActiveNetConnections.txt for suspicious TCP/IP connections
5. Check Arp.txt for compromised or suspicious systems on the network
6. Review DnsCache.txt for suspicious DNS entries
7. Inspect IpConfig.txt for network adapter configurations
8. Analyze FirewallExecutionLog.txt and pfirewall.log from %windir%\system32\logfiles\firewall\pfirewall.log
9. Review Prefetch folder from %SystemRoot%\Prefetch and PrefetchFilesList.txt for recently used files and copy failures

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
