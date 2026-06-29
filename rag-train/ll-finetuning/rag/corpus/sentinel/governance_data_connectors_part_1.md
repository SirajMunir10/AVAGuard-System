# Governance: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Governance

## Scenario / Query
A Microsoft Sentinel workspace is ingesting data from multiple regions and sources, but the Security Operations team has no centralized view of which data connectors are enabled, which data types are being collected, and whether any connectors have failed or been disabled. How can the team use Sentinel's built-in monitoring and workbooks to audit the current connector status and data ingestion health?

## Environment Context
- **Tenant Type:** Enterprise (multi-region, multiple data sources)
- **Configuration:** Microsoft Sentinel workspace with multiple data connectors (e.g., Azure Activity, Office 365, AWS CloudTrail, Windows Security Events via AMA)

## Symptoms
- No single dashboard or report showing all enabled data connectors and their status
- Inability to quickly identify a connector that has stopped sending data
- Audit or compliance requests require manual checking of each connector's configuration

## Error Codes
N/A

## Root Causes
1. Lack of a governance process to regularly review connector health and data ingestion
2. No use of Sentinel's built-in 'Data connectors health monitoring' workbook or the 'Get-AzSentinelDataConnector' PowerShell cmdlet

## Remediation Steps
1. Open Microsoft Sentinel, navigate to 'Workbooks', and select the 'Data connectors health monitoring' workbook template (or create a custom workbook using the SentinelHealth data table).
2. Use the workbook to review the status of all data connectors, including last data received time, errors, and configuration changes.
3. Alternatively, run the PowerShell cmdlet 'Get-AzSentinelDataConnector -ResourceGroupName <rg> -WorkspaceName <ws>' to list all connectors and their properties.
4. Document the expected data sources and establish a recurring review cadence (e.g., weekly) using the workbook or a scheduled Azure Automation runbook that exports connector status.

## Validation
After implementing the workbook or PowerShell check, the team can confirm that all expected connectors appear with a 'Connected' status and recent data timestamps. Any missing or failed connectors will be immediately visible.

## Rollback
If the workbook is deleted, it can be re-created from the template. If PowerShell cmdlets are used, no permanent changes are made; simply stop using the cmdlet.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/monitor-data-connector-health>
- <https://learn.microsoft.com/en-us/powershell/module/az.sentinel/get-azsentineldataconnector>
