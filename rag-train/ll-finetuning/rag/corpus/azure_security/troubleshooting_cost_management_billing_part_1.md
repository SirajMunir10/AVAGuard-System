# Troubleshooting: Cost Management + Billing

**Domain:** Azure
**Subdomain:** Cost Management + Billing
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot when unable to view a billing account in the Azure portal?

## Environment Context
- **Tenant Type:** Azure subscription
- **Configuration:** Cost Management + Billing page

## Symptoms
- Unable to see billing account in the Azure portal
- Access to billing account page requires authorization

## Error Codes
N/A

## Root Causes
1. User may have access to multiple billing accounts (e.g., personal Azure sign-up, Enterprise Agreement, Microsoft Customer Agreement)
2. Authorization or directory context may be incorrect

## Remediation Steps
1. Try signing in to the Azure portal
2. Try changing directories in the Azure portal

## Validation
1. Sign in to the Azure portal (https://portal.azure.com) with the user account that should have billing access. 2. Navigate to Cost Management + Billing. 3. If the billing account is still not visible, click the Settings gear icon in the top-right corner of the portal, then select 'Directory + subscription'. 4. In the 'Directory + subscription' pane, verify the current directory shown. 5. Switch to a different directory from the list (e.g., the directory associated with the Enterprise Agreement or Microsoft Customer Agreement). 6. After switching, navigate again to Cost Management + Billing and confirm the billing account appears. 7. If multiple billing accounts are expected, repeat steps 3-6 for each directory to ensure the correct billing account is accessible.

## Rollback
1. If switching directories does not resolve the issue or causes access problems, switch back to the original directory by repeating steps 3-4 of the validation and selecting the original directory. 2. If the user still cannot see the billing account, verify that the user has the necessary permissions (e.g., billing reader, billing contributor, or billing owner) on the billing account by contacting the billing account administrator. 3. If permissions are confirmed correct, clear the browser cache and cookies, then sign out and sign back in to the Azure portal. 4. As a last resort, open a support request from the Azure portal Help + support blade, providing details of the troubleshooting steps taken.

## References
- <https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/troubleshoot-account-not-found>
