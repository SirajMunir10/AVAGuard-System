# Implementation: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Implementation

## Scenario / Query
How to configure Syslog and Common Event Format (CEF) data streaming from Linux-based devices into Microsoft Sentinel using the Azure Monitor Agent (AMA)?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace with Azure Monitor Agent (AMA) deployed on Linux-based Syslog-supporting devices or a dedicated log forwarder

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Install the Azure Monitor Agent (AMA) directly on the device or on a dedicated Linux-based log forwarder.
2. Ensure the device's built-in Syslog daemon collects local events of the specified types and forwards them locally to the agent.
3. The AMA receives plain Syslog or CEF event messages from the Syslog daemon over UDP.
4. The Syslog daemon forwards events to the agent internally, communicating over TCP or UDS (Unix Domain Sockets), depending on the version.
5. The AMA transmits these events to the Microsoft Sentinel workspace.
6. After successful configuration, Syslog messages appear in the Log Analytics Syslog table, and CEF messages in the CommonSecurityLog table.

## Validation
1. On the Linux device or log forwarder, verify the Azure Monitor Agent is installed and running: `systemctl status azuremonitoragent` or `sudo journalctl -u azuremonitoragent --no-pager | tail -20`. 2. Check that the Syslog daemon (rsyslog or syslog-ng) is configured to forward events to the AMA: for rsyslog, confirm the configuration file (e.g., /etc/rsyslog.d/10-azuremonitoragent.conf) contains lines like `*.* @@127.0.0.1:25226` or `*.* @127.0.0.1:25226` depending on protocol. 3. Validate that the AMA is receiving events: `sudo /opt/microsoft/azuremonitoragent/bin/agentadmin --check` or inspect logs at `/var/opt/microsoft/azuremonitoragent/log/mdsd.log` for incoming syslog messages. 4. In Microsoft Sentinel, navigate to Logs and run a query to confirm data ingestion: `Syslog | where TimeGenerated > ago(10m) | take 10` for syslog, or `CommonSecurityLog | where TimeGenerated > ago(10m) | take 10` for CEF. 5. Verify the Data Connector status in Sentinel: go to Data connectors, select 'Syslog via AMA' or 'CEF via AMA', and confirm the connector shows 'Connected' and data flow is active.

## Rollback
1. Remove the AMA from the Linux device: `sudo /opt/microsoft/azuremonitoragent/bin/agentadmin --uninstall` or use the Azure portal to delete the Data Collection Rule (DCR) association. 2. Revert the Syslog daemon configuration: delete or comment out the forwarding rule added for the AMA (e.g., remove the line `*.* @@127.0.0.1:25226` from /etc/rsyslog.d/10-azuremonitoragent.conf) and restart the daemon: `sudo systemctl restart rsyslog` or `sudo systemctl restart syslog-ng`. 3. If a dedicated log forwarder was used, stop and disable the AMA service: `sudo systemctl stop azuremonitoragent && sudo systemctl disable azuremonitoragent`. 4. In Microsoft Sentinel, disable the Syslog via AMA or CEF via AMA data connector to stop data ingestion. 5. Optionally, delete the Data Collection Rule (DCR) associated with the connector from the Azure portal under Monitor > Data Collection Rules.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/connect-data-sources>
