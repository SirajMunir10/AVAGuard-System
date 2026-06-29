# Hardening: Data Collection and Retention

**Domain:** Sentinel
**Subdomain:** Data Collection and Retention
**Incident Type:** Hardening

## Scenario / Query
A security administrator notices that Microsoft Sentinel is ingesting logs from a critical domain controller but the Data Collection Rule (DCR) does not enforce any data transformation to filter or mask sensitive fields. How can the administrator apply a Data Collection Rule transformation to remove or obfuscate sensitive data before ingestion into Sentinel?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Microsoft Sentinel workspace with Azure Monitor Agent (AMA) and Data Collection Rules (DCRs) enabled

## Symptoms
- Sensitive fields (e.g., user principal names, IP addresses) appear in raw logs stored in the Log Analytics workspace
- No data transformation or filtering is applied during log ingestion
- Compliance requirements mandate masking of personally identifiable information (PII) before storage

## Error Codes
N/A

## Root Causes
1. Data Collection Rule does not include a transformKql element to filter or transform incoming data
2. Administrator is unaware of the DCR transformation capability in Sentinel

## Remediation Steps
1. 1. Identify the existing DCR associated with the data source (e.g., via Azure portal or PowerShell).
2. 2. Edit the DCR to add a `transformKql` property under the `dataFlows` section. For example, to remove a sensitive column named 'UserPrincipalName', use: `source | project-away UserPrincipalName`.
3. 3. Save the updated DCR. The transformation is applied to all new data ingested after the change.
4. 4. Verify that the transformation is working by querying the workspace for recent logs and confirming the sensitive field is absent.

## Validation
Run a KQL query in the Sentinel workspace to check that the sensitive column no longer appears in logs ingested after the DCR update. Example: `SecurityEvent | where TimeGenerated > ago(1h) | where isnotempty(UserPrincipalName)` should return no results.

## Rollback
Edit the DCR again and remove the `transformKql` line from the `dataFlows` section, then save. This restores original ingestion behavior.

## References
- <https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/data-collection-rule-overview#transformations>
