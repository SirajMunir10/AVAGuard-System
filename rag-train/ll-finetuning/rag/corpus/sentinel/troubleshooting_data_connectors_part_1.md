# Troubleshooting: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Troubleshooting

## Scenario / Query
How do I troubleshoot a Microsoft Sentinel data connector that shows a 'Disconnected' status and is not ingesting events?

## Environment Context
- **Tenant Type:** Azure tenant with Microsoft Sentinel enabled
- **Configuration:** Data connector for Windows Security Events via Azure Monitor Agent (AMA)

## Symptoms
- Data connector status shows 'Disconnected' in the Microsoft Sentinel portal
- No new events appear in the Log Analytics workspace for the connected table
- Heartbeat table shows missing or outdated entries for the monitored machines

## Error Codes
N/A

## Root Causes
1. Azure Monitor Agent is not installed or is not running on the source machine
2. Data collection rule (DCR) is not properly associated with the source machine
3. Network connectivity issues between the source machine and the Log Analytics workspace
4. Insufficient permissions for the agent to send data to the workspace

## Remediation Steps
1. Verify that the Azure Monitor Agent is installed and running on the source machine. Use the Azure portal or the following command on the machine: `Get-Service -Name 'AzureMonitorAgent'`
2. Check that the data collection rule (DCR) is correctly assigned to the source machine. In the Azure portal, navigate to the DCR and confirm the machine is listed under 'Resources'.
3. Test network connectivity from the source machine to the Log Analytics workspace endpoint using `Test-NetConnection <workspace-id>.ods.opinsights.azure.com -Port 443`
4. Ensure the managed identity of the source machine has the 'Monitoring Metrics Publisher' role on the Log Analytics workspace
5. Wait 15 minutes after applying changes and re-check the connector status in Sentinel

## Validation
After remediation, the connector status should change to 'Connected' and new events should appear in the Log Analytics workspace within 15 minutes.

## Rollback
If the connector remains disconnected, remove the machine from the DCR, reinstall the Azure Monitor Agent, and reassign the DCR.

## References
- <https://learn.microsoft.com/en-us/azure/azure-monitor/agents/azure-monitor-agent-troubleshoot>
