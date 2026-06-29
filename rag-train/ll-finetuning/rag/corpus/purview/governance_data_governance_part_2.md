# Governance: Data Governance

**Domain:** Purview
**Subdomain:** Data Governance
**Incident Type:** Governance

## Scenario / Query
A user reports that they cannot apply a sensitivity label to a file in Microsoft 365, and the label is not visible in the sensitivity bar. The label was published to all users in the tenant, and the user is licensed for Microsoft 365 E5. What should be checked to resolve this governance issue?

## Environment Context
- **Tenant Type:** Microsoft 365 E5
- **Configuration:** Sensitivity labels published via Microsoft Purview Compliance Portal, label policy assigned to all users

## Symptoms
- Sensitivity label does not appear in the sensitivity bar for the user
- Label policy shows as assigned but label is not applied

## Error Codes
N/A

## Root Causes
1. The user may not have the Azure Information Protection unified labeling client installed or the built-in labeling for Office apps may be disabled
2. The label policy may not have propagated yet (up to 24 hours)
3. The user may be using a version of Office that does not support sensitivity labels

## Remediation Steps
1. Verify that the user has a supported Office version (Microsoft 365 Apps for enterprise, version 2006 or later, or Office for the web)
2. Ensure the Azure Information Protection unified labeling client is installed if using Windows with older Office versions
3. Check the label policy assignment in the Microsoft Purview compliance portal under Information Protection > Label policies
4. Wait up to 24 hours for policy propagation or force a policy refresh by restarting Office applications
5. If the issue persists, use the AIP client diagnostic tool to check label policy download status

## Validation
The user should see the sensitivity label in the sensitivity bar and be able to apply it to documents and emails.

## Rollback
Remove the user from the label policy assignment or delete the label policy if no longer needed.

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels>
