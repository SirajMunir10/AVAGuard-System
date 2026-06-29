# Troubleshooting: Azure Monitor Alerts

**Domain:** Azure
**Subdomain:** Azure Monitor Alerts
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve issues where Azure Monitor cannot create, update, or manage alert rules due to the Geneva Alert RP application being disabled or deleted?

## Environment Context
- **Tenant Type:** Microsoft Entra tenant
- **Configuration:** Geneva Alert RP enterprise application

## Symptoms
- Azure Monitor unable to create, update, or manage alert rules as expected

## Error Codes
N/A

## Root Causes
1. Geneva Alert RP enterprise application is disabled or deleted in the Microsoft Entra tenant

## Remediation Steps
1. Contact your tenant administrator
2. Ask them to verify that the Geneva Alert RP enterprise application exists in the Microsoft Entra tenant
3. Ask them to verify that the Geneva Alert RP enterprise application is not disabled or removed
4. If the application is missing or disabled, restore or re-enable it

## Validation
1. Sign in to the Azure portal (https://portal.azure.com) as a tenant administrator. 2. Navigate to Microsoft Entra ID > Enterprise applications. 3. In the search box, type 'Geneva Alert RP' and verify that the application appears in the list. 4. Select the application and go to Properties. 5. Confirm that 'Enabled for users to sign-in?' is set to 'Yes'. 6. If the application is missing or disabled, proceed with the remediation steps. 7. After remediation, repeat steps 1-5 to confirm the application is present and enabled. 8. Additionally, attempt to create or update an alert rule in Azure Monitor to verify the issue is resolved.

## Rollback
1. If the remediation (restoring or re-enabling the Geneva Alert RP enterprise application) causes unexpected issues, sign in to the Azure portal as a tenant administrator. 2. Navigate to Microsoft Entra ID > Enterprise applications. 3. Search for 'Geneva Alert RP' and select it. 4. Go to Properties. 5. Set 'Enabled for users to sign-in?' to 'No' to disable the application, or delete the application if it was restored and needs to be removed. 6. Confirm the change and verify that Azure Monitor alert rule management returns to the previous state. 7. If the application was restored from a deleted state and needs to be removed, use the 'Delete' option in the application's overview page.

## References
- <https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-troubleshoot>
