# Hardening: Cost Management

**Domain:** Azure
**Subdomain:** Cost Management
**Incident Type:** Hardening

## Scenario / Query
How to configure and respond to credit alerts for Azure Prepayment consumption under an Enterprise Agreement?

## Environment Context
- **Tenant Type:** Enterprise Agreement
- **Configuration:** Azure Prepayment (monetary commitment)

## Symptoms
- Credit alert generated at 90% of Azure Prepayment credit balance
- Credit alert generated at 100% of Azure Prepayment credit balance
- Alert reflected in cost alerts
- Email sent to account owners

## Error Codes
N/A

## Root Causes
1. Azure Prepayment credit balance consumed at 90% threshold
2. Azure Prepayment credit balance consumed at 100% threshold

## Remediation Steps
1. Monitor cost alerts for credit alert notifications
2. Check email sent to account owners for alert details
3. Review Azure Prepayment balance and adjust spending or add funds as needed

## Validation
1. Navigate to Cost Management + Billing in the Azure portal. 2. Under 'Cost Management', select 'Cost alerts'. 3. Verify that no active credit alerts (e.g., 'Azure Prepayment credit balance at 90%' or 'Azure Prepayment credit balance at 100%') are present. 4. Check the 'Alert history' tab to confirm that previous credit alerts have been resolved or are no longer firing. 5. Optionally, use Azure CLI: `az consumption budget list --scope /providers/Microsoft.Billing/billingAccounts/{billingAccountId} --query "[?contains(name, 'credit')].{Name:name, CurrentSpend:currentSpend.amount, Threshold:amount}"` to confirm current spending is below the alert threshold.

## Rollback
1. If the remediation (e.g., adding funds or adjusting spending) causes issues, restore the Azure Prepayment balance by contacting your Microsoft account team or reseller to reverse any fund addition (if possible). 2. If spending adjustments were made, revert any budget or spending limit changes via Cost Management > Budgets. 3. To re-enable alerts, navigate to Cost Management > Cost alerts and ensure alert rules for credit thresholds (e.g., 90% and 100%) are active. 4. Use Azure CLI to reset alert rules: `az consumption budget create --scope /providers/Microsoft.Billing/billingAccounts/{billingAccountId} --budget-name "credit_alert_90" --amount {originalThreshold} --time-grain Monthly --category Cost --notification-email {originalEmail}`. 5. Confirm that email notifications are re-enabled for account owners.

## References
- <https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/cost-mgt-alerts-monitor-usage-spending>
