# Troubleshooting: Network Watcher

**Domain:** Azure
**Subdomain:** Network Watcher
**Incident Type:** Troubleshooting

## Scenario / Query
How to diagnose and troubleshoot network connectivity issues in Azure using the connection troubleshoot feature of Network Watcher?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Complex networks with network security groups, firewalls, user-defined routes

## Symptoms
- Connectivity issues in complex Azure networks
- High Mean Time To Resolution (MTTR) for network problems

## Error Codes
N/A

## Root Causes
1. Platform or user configuration issue
2. Network security group misconfiguration
3. User-defined route misconfiguration
4. Blocked ports

## Remediation Steps
1. Use the connection troubleshoot feature of Azure Network Watcher
2. Perform connectivity test with different destination types (VM, URI, FQDN, or IP Address)
3. Review results for configuration issues impacting reachability
4. Check latency (minimum, maximum, and average between source and destination)
5. Examine graphical topology view from source to destination
6. Review number of probes failed during the connection troubleshoot check
7. Follow step-by-step guide or corresponding documentation provided for faster resolution

## Validation
1. Run the connection troubleshoot test again using the same source and destination parameters. 2. Verify that the test result shows 'Reachable' with zero probes failed. 3. Confirm that the latency metrics (minimum, maximum, average) are within expected baseline. 4. Review the graphical topology to ensure no NSG or route blocks are shown. 5. Check that the step-by-step guide or documentation link is accessible and matches the resolved configuration.

## Rollback
1. Revert any NSG rule changes that were made during remediation by restoring the previous NSG configuration. 2. Revert any UDR changes by restoring the previous route table configuration. 3. If firewall rules were modified, restore the original firewall policy. 4. Re-run the connection troubleshoot test to confirm the original issue reappears. 5. Document the rollback actions taken and notify the incident management team.

## References
- <https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-connectivity-overview>
