# Troubleshooting: Network Watcher

**Domain:** Azure
**Subdomain:** Network Watcher
**Incident Type:** Troubleshooting

## Scenario / Query
How to interpret the connection troubleshoot results from Azure Network Watcher, including status, latency, probes, hop-by-hop path, and issues?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Network Watcher connection troubleshoot

## Symptoms
- ConnectionStatus is Unreachable
- ProbesFailed count is greater than 0
- Hops[].Issues[].Type indicates CPU, Memory, GuestFirewall, DnsResolution, NetworkSecurityRule, or UserDefinedRoute

## Error Codes
N/A

## Root Causes
1. Network connectivity issue between source and destination
2. Hop-by-hop path issue (e.g., VirtualAppliance, VnetLocal, Internet)
3. Issue at a hop with Origin Inbound, Outbound, or Local
4. Issue severity Error or Warning at a hop

## Remediation Steps
1. Check ConnectionStatus field: if Unreachable, investigate further
2. Review AvgLatencyInMs, MinLatencyInMs, MaxLatencyInMs for latency issues (only if status is Reachable)
3. Examine Number of probes sent and ProbesFailed (max 100 each)
4. Analyze Hops array: for each hop, check Type, Address, ResourceId, NextHopIds
5. For each hop, review Issues array: note Origin (Inbound, Outbound, Local), Severity (Error, Warning), Type (CPU, Memory, GuestFirewall, DnsResolution, NetworkSecurityRule, UserDefinedRoute), and Context (key-value pairs)
6. Check NextHopAnalysis.NextHopType (HyperNetGateway, Internet, None, VirtualAppliance, VirtualNetworkGateway, VnetLocal) and NextHopAnalysis.NextHopIpAddress
7. Review SourceSecurityRuleAnalysis.Results[].Profile: Source, Destination, DestinationPort, Protocol

## Validation
1. Run 'az network watcher test-connectivity --source-resource <sourceVM> --dest-resource <destVM> --dest-port <port>' and verify ConnectionStatus is 'Reachable'. 2. Check that ProbesFailed is 0. 3. Confirm AvgLatencyInMs, MinLatencyInMs, MaxLatencyInMs are within expected range. 4. For each hop in Hops[], ensure Issues[] is empty. 5. Verify NextHopAnalysis.NextHopType is as expected (e.g., 'VirtualNetworkGateway') and NextHopIpAddress is correct. 6. Confirm SourceSecurityRuleAnalysis.Results[].Profile shows allowed Source, Destination, DestinationPort, Protocol.

## Rollback
1. If ConnectionStatus is 'Unreachable', revert any recent network configuration changes (e.g., NSG rules, route tables, firewall policies). 2. If ProbesFailed > 0, restore previous NSG rules or route tables that were modified. 3. If latency is high, revert any changes to virtual appliance or bandwidth settings. 4. If Issues[] appear at a hop, undo changes to that hop's configuration (e.g., VM size, DNS settings, firewall rules). 5. If NextHopAnalysis shows unexpected type, revert route table or gateway changes. 6. If SourceSecurityRuleAnalysis shows blocked traffic, restore original security rules.

## References
- <https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-connectivity-overview>
