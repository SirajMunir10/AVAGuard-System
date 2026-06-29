# Troubleshooting: Cost Management + Billing

**Domain:** Azure
**Subdomain:** Cost Management + Billing
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve the issue where a billing account is not visible on the Cost Management + Billing page due to signing in to the wrong Microsoft Entra tenant?

## Environment Context
- **Tenant Type:** Microsoft Entra tenant
- **Configuration:** Billing account associated with a single Microsoft Entra tenant

## Symptoms
- Billing account not visible on the Cost Management + Billing page

## Error Codes
N/A

## Root Causes
1. Signed in to an incorrect Microsoft Entra tenant

## Remediation Steps
1. Sign in to the Azure portal
2. Select your profile (email address) at the top right of the page
3. Select Switch directory
4. Select a directory under the All directories section

## Validation
1. In the Azure portal, click your profile icon (email address) at the top right. 2. Select 'Switch directory'. 3. Under 'All directories', verify that the directory containing your billing account appears and is marked as 'Current' or is selected. 4. Navigate to 'Cost Management + Billing' and confirm the billing account is now visible.

## Rollback
1. In the Azure portal, click your profile icon (email address) at the top right. 2. Select 'Switch directory'. 3. Under 'All directories', select the original directory you were signed into before the change. 4. Confirm the portal switches back to that directory and that the billing account remains hidden (as expected if the account is not associated with that tenant).

## References
- <https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/troubleshoot-account-not-found>
