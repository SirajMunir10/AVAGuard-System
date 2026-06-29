# Governance: Data Loss Prevention (DLP) â€“ Policy Tuning

**Domain:** Purview
**Subdomain:** Data Loss Prevention (DLP) â€“ Policy Tuning
**Incident Type:** Governance

## Scenario / Query
A DLP policy that was working correctly suddenly stops applying to new SharePoint Online documents, even though the policy shows as 'Enabled' in the Microsoft Purview compliance portal. What governance misconfiguration could cause this, and how do I verify and fix it?

## Environment Context
- **Tenant Type:** Enterprise (E5)
- **Configuration:** Microsoft Purview DLP policy scoped to SharePoint Online sites via 'Locations' setting; policy was created more than 90 days ago and has not been modified recently.

## Symptoms
- DLP policy no longer triggers on newly uploaded documents in SharePoint Online
- Policy status shows 'Enabled' in Microsoft Purview compliance portal
- No DLP rule matches appear in Activity Explorer for the affected sites
- Other DLP policies continue to work correctly

## Error Codes
N/A

## Root Causes
1. The DLP policyâ€™s 'Locations' configuration may have become stale or lost its scope due to a known issue where policies older than 90 days require re-application of location scoping after a tenant-level update (e.g., SharePoint Online service update).
2. The policy may have been inadvertently disabled by a change in the 'Policy mode' setting (e.g., switched from 'Test' to 'Disabled' or 'Turn off policy').

## Remediation Steps
1. 1. Sign in to the Microsoft Purview compliance portal (https://compliance.microsoft.com).
2. 2. Navigate to Data Loss Prevention > Policies and select the affected policy.
3. 3. Click 'Edit policy' and review the 'Locations' tab. Ensure the correct SharePoint sites are still selected and that the policy is not scoped to 'All sites' if that was not the original intent.
4. 4. Under 'Policy settings', confirm the 'Policy mode' is set to 'Turn on policy immediately' (or the intended mode).
5. 5. If the policy appears correct, save the policy without changes to force a refresh of the policy distribution to SharePoint Online.
6. 6. Wait up to 24 hours for the policy to fully propagate, then test by uploading a sensitive document to the affected site.
7. 7. If the issue persists, use the 'Test' mode to validate rule matches before re-enabling enforcement.

## Validation
After remediation, upload a test document containing sensitive content (e.g., a credit card number) to the affected SharePoint site. Verify that the DLP policy blocks or alerts as expected. Check Activity Explorer for a matching DLP rule match event.

## Rollback
If the policy was inadvertently changed, revert to the previous known-good configuration using the 'Restore' option in the policy history (if available) or manually re-apply the original location scoping and mode settings.

## References
- Microsoft Learn: 'Create and deploy a DLP policy' â€“ https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy?view=o365-worldwide
- Microsoft Learn: 'Get started with DLP policy recommendations' â€“ https://learn.microsoft.com/en-us/purview/dlp-policy-recommendations?view=o365-worldwide
