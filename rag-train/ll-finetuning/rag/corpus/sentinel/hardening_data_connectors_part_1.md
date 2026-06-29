# Hardening: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Hardening

## Scenario / Query
A security administrator notices that Microsoft Sentinel is ingesting security events from Azure VMs using the legacy 'Security Events' connector instead of the newer 'Windows Security Events via AMA' connector. The administrator wants to harden the deployment by migrating to the Azure Monitor Agent (AMA) based connector to benefit from improved security, performance, and future support. What steps should be taken to migrate from the legacy connector to the AMA-based connector?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Microsoft Sentinel workspace with legacy Security Events connector (Legacy Agent) enabled for Windows VMs

## Symptoms
- Security events are being collected using the legacy Log Analytics Agent (MMA) based connector
- The 'Windows Security Events via AMA' connector is not enabled
- Alerts and incidents are generated from legacy connector data

## Error Codes
N/A

## Root Causes
1. The workspace was originally configured with the legacy Security Events connector before the AMA-based connector was available
2. No migration plan was executed to transition to the AMA-based connector

## Remediation Steps
1. 1. Identify all Windows VMs currently using the legacy Security Events connector in the Sentinel workspace.
2. 2. Install the Azure Monitor Agent (AMA) on those VMs using the Azure portal, PowerShell, or Azure Policy.
3. 3. Enable the 'Windows Security Events via AMA' data connector in Microsoft Sentinel and configure the desired security event filtering (e.g., All Events, Common, Minimal).
4. 4. Verify that security events are being collected via the new connector by checking the Sentinel logs (e.g., SecurityEvent table populated from AMA).
5. 5. Once data flow is confirmed, disable the legacy Security Events connector and uninstall the Log Analytics Agent from the VMs to avoid duplicate ingestion and cost.

## Validation
Run the following KQL query in Sentinel to confirm events are being collected from the AMA-based connector: SecurityEvent | where TimeGenerated > ago(1h) | summarize count() by _ResourceId. Ensure the _ResourceId values correspond to the VMs with AMA installed.

## Rollback
If issues arise, re-enable the legacy Security Events connector and reinstall the Log Analytics Agent on the VMs. Keep both connectors temporarily until the AMA-based connector is stable.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/migration-security-events-connector>
