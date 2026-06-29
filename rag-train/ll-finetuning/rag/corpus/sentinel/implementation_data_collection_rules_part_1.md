# Implementation: Data Collection Rules

**Domain:** Sentinel
**Subdomain:** Data Collection Rules
**Incident Type:** Implementation

## Scenario / Query
How do I configure ingestion-time data transformation in Microsoft Sentinel to filter and enrich data before querying?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Data Collection Rules (DCRs) in Log Analytics portal, API, or ARM template

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Choose the appropriate Data Collection Rule (DCR) type for your data connector.
2. Configure the DCR in the Log Analytics portal, via API, or using an ARM template.
3. Apply the DCR to filter and enrich output tables before running queries.

## Validation
1. In the Log Analytics workspace, run: `Usage | where TimeGenerated > ago(1h) | summarize count() by DataType` to confirm transformed data is flowing. 2. Query the target table (e.g., `CommonSecurityLog | take 10`) and verify that filtered/enriched fields appear as expected. 3. Check the DCR status via Azure CLI: `az monitor data-collection rule show --name <DCR-name> --resource-group <RG-name> --query 'provisioningState'` – should return 'Succeeded'.

## Rollback
1. Remove the transformation from the DCR by editing the `transformKql` property to an empty string or the original KQL. 2. If the DCR was created solely for transformation, delete it: `az monitor data-collection rule delete --name <DCR-name> --resource-group <RG-name>`. 3. Revert any ARM template deployment to the previous version. 4. Confirm data returns to untransformed state by querying the table and comparing with a backup or known baseline.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/configure-data-transformation>
