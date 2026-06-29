# Implementation: Cost Management

**Domain:** Azure
**Subdomain:** Cost Management
**Incident Type:** Implementation

## Scenario / Query
How to create and configure budget alerts in Azure Cost Management to notify when spending reaches or exceeds defined thresholds?

## Environment Context
- **Tenant Type:** Enterprise Agreement or Microsoft Customer Agreement
- **Configuration:** Budgets defined by cost (Azure portal) or by cost/consumption usage (Azure Consumption API)

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Create budgets using the Azure portal or the Azure Consumption API.
2. In the Azure portal, define budgets by cost.
3. Using the Azure Consumption API, define budgets by cost or by consumption usage.
4. Set the alert condition in the budget to define when spending reaches or exceeds the amount.
5. Specify alert recipients in the budget's alert recipients list to receive email notifications.
6. For Enterprise Agreement customers, use the Azure portal to create and edit budgets.
7. For Microsoft Customer Agreement customers, use the Budgets REST API to create budgets programmatically.
8. To send email alerts in a different language, use the Budget API and refer to supported locales for budget alert emails.

## Validation
1. In the Azure portal, navigate to Cost Management + Billing > Cost Management > Budgets. Verify the budget appears in the list with the correct name, amount, and time grain. 2. Select the budget and confirm the alert conditions (e.g., threshold percentage, operator) match the intended configuration. 3. Check the Alert recipients list to ensure the correct email addresses are included. 4. (Optional) If using the Azure Consumption API, run: az consumption budget show --budget-name <budget_name> --resource-group <resource_group> (or equivalent REST call) and verify the properties 'amount', 'timeGrain', 'notifications' contain the expected threshold and recipient details.

## Rollback
1. In the Azure portal, navigate to Cost Management + Billing > Cost Management > Budgets. Select the budget to modify or delete. 2. To revert to a previous configuration, edit the budget amount, alert threshold, or alert recipients back to the original values and click Save. 3. To remove the budget entirely, click Delete and confirm. 4. If using the Azure Consumption API, use the Budgets - CreateOrUpdate operation with the previous configuration payload, or use Budgets - Delete to remove the budget. 5. For Enterprise Agreement customers, use the Azure portal to edit or delete budgets. For Microsoft Customer Agreement customers, use the Budgets REST API to update or delete budgets programmatically.

## References
- <https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/cost-mgt-alerts-monitor-usage-spending>
