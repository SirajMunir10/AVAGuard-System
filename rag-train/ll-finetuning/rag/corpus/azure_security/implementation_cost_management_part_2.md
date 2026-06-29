# Implementation: Cost Management

**Domain:** Azure
**Subdomain:** Cost Management
**Incident Type:** Implementation

## Scenario / Query
How to configure department spending quota alerts in Azure Cost Management?

## Environment Context
- **Tenant Type:** Enterprise Agreement
- **Configuration:** Department spending quotas configured in Azure portal

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Configure spending quotas in the Azure portal.
2. Set thresholds (e.g., 50% or 75% of the quota) to trigger alerts.
3. When a threshold is met, an email is generated to department owners and shown in cost alerts.

## Validation
1. Navigate to Cost Management + Billing in the Azure portal. 2. Select 'Cost alerts' under 'Cost Management'. 3. Verify that the department spending quota alert appears in the list with the correct threshold (e.g., 50% or 75%). 4. Confirm that the alert status is 'Active' and the associated department is correct. 5. Optionally, use Azure CLI: `az costmanagement alert list --scope '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}'` and verify the alert properties include the expected threshold and quota.

## Rollback
1. In the Azure portal, go to 'Cost Management + Billing' > 'Cost alerts'. 2. Select the department spending quota alert you configured. 3. Click 'Delete' to remove the alert. 4. Confirm deletion. 5. Alternatively, use Azure CLI: `az costmanagement alert delete --scope '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' --alert-id '{alertId}'` to remove the alert.

## References
- <https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/cost-mgt-alerts-monitor-usage-spending>
