# Troubleshooting: Cost Management + Billing

**Domain:** Azure
**Subdomain:** Cost Management + Billing
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve a missing billing account in the Azure portal when the user has two identities (work/school and personal) with the same email address?

## Environment Context
- **Tenant Type:** Azure portal user with multiple identity types
- **Configuration:** User has both a work or school account and a personal account associated with the same email address

## Symptoms
- Billing account not visible in the Cost Management + Billing page
- User has two identities with the same email address

## Error Codes
N/A

## Root Causes
1. User signed in with an identity that does not have permissions to view the billing account

## Remediation Steps
1. Sign in to the Azure portal in an InPrivate/Incognito window
2. If your email address has two identities, you'll see an option to select a personal account or a work or school account
3. Select one of the accounts
4. If you can't see the billing account in the Cost Management + Billing page in the Azure portal, repeat steps 1 and 2 and select the other identity

## Validation
1. Open an InPrivate or Incognito browser window and navigate to https://portal.azure.com. 2. If prompted, select the work or school account identity (not the personal account). 3. Go to Cost Management + Billing. 4. Verify that the expected billing account is listed. 5. If not visible, sign out, repeat steps 1-3 using the personal account identity. 6. Confirm the billing account appears under at least one identity.

## Rollback
1. Sign out of the Azure portal. 2. Clear browser cache and cookies. 3. Reopen a normal (non-private) browser window. 4. Sign in with the original identity used before troubleshooting. 5. Navigate to Cost Management + Billing to confirm the billing account visibility returns to its previous state (i.e., not visible). 6. If the account becomes visible under the wrong identity, sign out and repeat steps 1-5 to restore the original condition.

## References
- <https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/troubleshoot-account-not-found>
