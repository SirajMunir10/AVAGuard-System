# Troubleshooting: Data Connectors

**Domain:** Sentinel
**Subdomain:** Data Connectors
**Incident Type:** Troubleshooting

## Scenario / Query
A Microsoft Sentinel workspace shows no data ingestion from the Azure Activity connector, even though the connector is enabled. How do I troubleshoot this issue?

## Environment Context
- **Tenant Type:** Enterprise (Azure AD tenant with Azure subscription)
- **Configuration:** Azure Activity connector enabled in Microsoft Sentinel, but no Activity logs appear in the workspace.

## Symptoms
- Azure Activity connector shows status as 'Connected' but no data in the workspace
- No AzureActivity table entries in Log Analytics
- No errors or alerts in the connector health blade

## Error Codes
N/A

## Root Causes
1. Diagnostic settings for the subscription are not configured to stream Activity logs to the Log Analytics workspace used by Sentinel
2. The Azure Policy required to deploy diagnostic settings is not assigned or is out of scope

## Remediation Steps
1. 1. In the Azure portal, navigate to Monitor > Activity log > Export Activity Logs.
2. 2. Ensure a diagnostic setting exists for the subscription that sends 'Administrative', 'Security', 'ServiceHealth', 'Alert', 'Recommendation', 'Policy', and 'Autoscale' categories to the Log Analytics workspace used by Sentinel.
3. 3. If missing, create a new diagnostic setting: select 'Stream to a Log Analytics workspace' and choose the correct workspace.
4. 4. Wait up to 30 minutes for data to appear in the AzureActivity table.
5. 5. If the connector was deployed via policy, verify the policy assignment is scoped to the correct management group or subscription and is in 'Compliant' state.

## Validation
Run the following KQL query in the Sentinel workspace: AzureActivity | take 10. If results appear, ingestion is working.

## Rollback
Remove the diagnostic setting created in step 3, or disable the Azure Activity connector in Sentinel.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/troubleshoot-azure-activity-log-connector>
