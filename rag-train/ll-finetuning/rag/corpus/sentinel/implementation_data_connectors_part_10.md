# Implementation: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Implementation

## Scenario / Query
How do I connect custom logs from Windows or Linux computers to Microsoft Sentinel using the Log Analytics custom log collection agent?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Log Analytics workspace with Microsoft Sentinel enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Follow the steps in each Microsoft Sentinel data connector page.
2. After successful configuration, the data appears in custom tables.

## Validation
1. In the Log Analytics workspace, run the following query to confirm custom log data is being ingested: `YourCustomLog_CL | take 10`. 2. Verify the custom log table appears in the Log Analytics workspace under 'Tables' with a '_CL' suffix. 3. Check the Azure Monitor Agent (AMA) or Log Analytics agent health via the 'Heartbeat' table: `Heartbeat | where Category == 'Direct Agent' | project Computer, TimeGenerated`. 4. Confirm the data connector status in Microsoft Sentinel under 'Data connectors' shows 'Connected' for the custom log connector.

## Rollback
1. Remove the custom log data connector in Microsoft Sentinel by selecting the connector and clicking 'Delete'. 2. Delete the custom log table from the Log Analytics workspace via the 'Tables' blade or using the Azure CLI: `az monitor log-analytics workspace table delete --workspace-name <workspace> --resource-group <rg> --name <table_name>`. 3. Uninstall the Azure Monitor Agent or Log Analytics agent from the Windows or Linux computers if the custom log collection was the only purpose. 4. Revert any custom log collection configuration files (e.g., in /etc/rsyslog.d/ or C:\Program Files\Microsoft Monitoring Agent\Agent\Health Service State\) to their original state.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/connect-data-sources>
- <https://learn.microsoft.com/en-us/azure/sentinel/custom-logs-via-ama-data-connector>
