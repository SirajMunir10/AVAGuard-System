# Governance: Access Reviews

**Domain:** Entra ID
**Subdomain:** Access Reviews
**Incident Type:** Governance

## Scenario / Query
A security auditor reports that guest users have been retaining access to internal SharePoint sites for over a year without any recertification. How can I enforce periodic access reviews for all guest users in Entra ID?

## Environment Context
- **Tenant Type:** Production
- **Configuration:** Access reviews are not configured for guest users; guest user access is granted via B2B collaboration.

## Symptoms
- Guest users have access to internal resources beyond the required period
- No access review campaigns are scheduled for guest users
- Audit logs show no recertification events for guest accounts

## Error Codes
N/A

## Root Causes
1. Access reviews are not configured for guest users in Entra ID Identity Governance
2. No recurring review policy is assigned to guest users

## Remediation Steps
1. Sign in to the Entra admin center as a Global Administrator or Identity Governance Administrator
2. Navigate to Identity Governance > Access reviews > select 'New access review'
3. Select 'Teams + Groups' as the scope, then choose 'All Microsoft 365 groups with guest users'
4. Set the review to recur monthly or quarterly, and assign reviewers (e.g., group owners)
5. Enable 'Auto-apply results to resource' to automatically remove access for denied guests
6. Configure 'If reviewer doesn't respond' to 'Remove access' to enforce action on non-response
7. Review and create the access review

## Validation
After the access review completes, verify that denied guest users are removed from the group membership. Use Entra ID audit logs to confirm removal events.

## Rollback
If auto-apply causes unintended removals, disable auto-apply in the access review settings and manually restore guest access via Azure AD PowerShell using Restore-AzureADMSDeletedDirectoryObject.

## References
- <https://learn.microsoft.com/en-us/entra/id-governance/access-reviews-plan-deployment-guest-users>
