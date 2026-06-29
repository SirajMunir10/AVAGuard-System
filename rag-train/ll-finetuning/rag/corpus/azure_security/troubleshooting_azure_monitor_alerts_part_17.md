# Troubleshooting: Azure Monitor Alerts

**Domain:** Azure
**Subdomain:** Azure Monitor Alerts
**Incident Type:** Troubleshooting

## Scenario / Query
Why did my alert processing rule not fire or fire unexpectedly?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Alert processing rule scope and filter conditions

## Symptoms
- Alert processing rule did not fire when expected
- Alert processing rule fired when not expected

## Error Codes
N/A

## Root Causes
1. Mismatch between alert processing rule scope and filter conditions and the properties of the fired alert

## Remediation Steps
1. Examine the alert processing rule scope and filter conditions
2. Compare the alert processing rule scope and filter conditions to the properties of the fired alert

## Validation
1. Navigate to Azure Monitor > Alerts > Alert processing rules. Select the rule in question and review its 'Scope' and 'Filter' conditions. 2. Identify the specific alert that fired or did not fire. Go to Azure Monitor > Alerts > Alert instances and locate the alert by time range and criteria. 3. Compare the alert's properties (e.g., resource ID, severity, signal type, custom properties) against the rule's scope and filters. Confirm that all conditions match exactly for a rule that should have fired, or that at least one condition does not match for a rule that should not have fired. 4. Use Azure Resource Graph or CLI to query the rule definition: `az monitor alert-processing-rule show --resource-group <rg> --name <rule-name>`. Verify the `scopes` and `conditions` array match the expected alert properties.

## Rollback
1. If the rule fired unexpectedly, edit the alert processing rule to narrow its scope or add more restrictive filter conditions (e.g., add a 'Severity equals' filter or limit to specific resource groups). 2. If the rule did not fire when expected, broaden the scope or remove overly restrictive filters. For example, change the scope from a single resource to a resource group, or remove a filter that excludes the alert's properties. 3. After modifying the rule, wait for the next alert matching the new conditions to confirm behavior. 4. If the issue persists, consider creating a new alert processing rule with corrected conditions and disabling the original rule.

## References
- <https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-troubleshoot>
