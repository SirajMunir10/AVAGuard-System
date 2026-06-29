# Optimization: Data Lifecycle Management

**Domain:** Purview
**Subdomain:** Data Lifecycle Management
**Incident Type:** Optimization

## Scenario / Query
A Microsoft 365 tenant has retention labels applied to SharePoint sites and OneDrive accounts, but the labels are not being automatically applied to new documents. The organization wants to optimize label application to ensure that all new documents inherit the correct retention label without manual intervention. What configuration changes are needed?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Purview compliance portal
- **Configuration:** Retention labels published to locations, but auto-application not enabled

## Symptoms
- Retention labels are published but not automatically applied to new documents
- Users must manually apply retention labels to new files
- Compliance officer reports gaps in retention coverage for newly created content

## Error Codes
N/A

## Root Causes
1. Retention labels were published but not configured for auto-application based on a sensitive info type or query
2. Auto-application policy was not created or enabled for the label
3. SharePoint and OneDrive locations were not included in the auto-application policy scope

## Remediation Steps
1. In the Microsoft Purview compliance portal, navigate to Data Lifecycle Management > Retention labels.
2. Select the retention label that should be auto-applied and choose 'Auto-apply a label'.
3. Create a new auto-application policy: specify a name, choose 'Apply label to content that contains sensitive info' or 'Apply label to content that matches a query' as appropriate.
4. Select the locations: SharePoint sites and OneDrive accounts.
5. Define the condition (e.g., sensitive info type or KQL query) that triggers label application.
6. Review and create the policy. Wait up to 7 days for the policy to take effect on existing and new content.

## Validation
After 7 days, verify that new documents in the targeted SharePoint sites and OneDrive accounts automatically receive the retention label. Use Content Explorer in Purview to confirm label assignment.

## Rollback
Disable or delete the auto-application policy in the Purview compliance portal. Existing labels will remain, but new content will no longer be auto-labeled.

## References
- <https://learn.microsoft.com/en-us/purview/apply-retention-labels-automatically>
