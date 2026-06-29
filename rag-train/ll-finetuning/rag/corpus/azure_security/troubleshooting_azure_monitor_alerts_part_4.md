# Troubleshooting: Azure Monitor Alerts (Failed to create alert rule <Rule Name>. There was a problem with the server, Please try again in a few minutes.)

**Domain:** Azure
**Subdomain:** Azure Monitor Alerts
**Incident Type:** Troubleshooting

## Scenario / Query
Log search alert rule creation failed with error 'Failed to create alert rule <Rule Name>. There was a problem with the server, Please try again in a few minutes.'

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Log search alert rule creation fails in Azure portal
- Error message: 'Failed to create alert rule <Rule Name>. There was a problem with the server, Please try again in a few minutes.'

## Error Codes
- `Failed to create alert rule <Rule Name>. There was a problem with the server, Please try again in a few minutes.`

## Root Causes
1. Combined size of all data in the log search alert rule properties exceeds 64 KB (or 32 K string characters)

## Remediation Steps
1. Check if the alert rule is using a large query, has many dimensions, action group, or a long description, whose combined size could be greater than 64 KB

## Validation
1. In the Azure portal, navigate to Monitor > Alerts > Alert rules. 2. Attempt to create a new log search alert rule with the same query, dimensions, action groups, and description as the failed rule. 3. Confirm that the rule is created successfully without the error 'Failed to create alert rule <Rule Name>. There was a problem with the server, Please try again in a few minutes.' 4. Alternatively, use Azure CLI: `az monitor scheduled-query create --resource-group <rg> --name <rule-name> --scopes <scope> --condition <condition> --action-groups <ag> --description <desc>` and verify it returns a valid rule object.

## Rollback
1. If the remediation fails, reduce the combined size of the alert rule properties by: a. Shortening the query. b. Reducing the number of dimensions. c. Removing unnecessary action groups. d. Truncating the description. 2. Retry creating the alert rule with the reduced properties. 3. If the issue persists, delete the partially created rule (if any) using Azure CLI: `az monitor scheduled-query delete --resource-group <rg> --name <rule-name>` and recreate with further size reductions.

## References
- <https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-troubleshoot>
