# Troubleshooting: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Troubleshooting

## Scenario / Query
How to filter messages by detected language in Communication Compliance?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Communication Compliance policy

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Sign in to the Microsoft Purview portal with credentials for an admin account in your Microsoft 365 organization.
2. Go to the Communication Compliance solution.
3. Select Policies in the left navigation, then select a policy to see policy matches (if any) for that policy.
4. On the Policy page, select either the Pending or Resolved tab to display the items for filtering.
5. Select Filters.
6. Select one or more filter checkboxes, then select Apply.
7. To save the selected filters as a filter query, select Save the query after you configure at least one filter value.
8. Enter a name for the filter query, then select Save. This filter is available to use for only this policy and is listed in the Saved filter queries section of the Filters page.

## Validation
1. Sign in to the Microsoft Purview portal (https://compliance.microsoft.com) with admin credentials.
2. Navigate to Communication Compliance > Policies.
3. Select the policy you configured.
4. On the Policy page, select the Pending or Resolved tab.
5. Click Filters and verify that the language filter checkboxes (e.g., 'Detected language') are available and selectable.
6. Select one or more language filters, click Apply, and confirm that the displayed messages are filtered by the selected language(s).
7. Optionally, click Save the query, enter a name, and save. Verify the saved query appears under 'Saved filter queries' on the Filters page.

## Rollback
1. Sign in to the Microsoft Purview portal with admin credentials.
2. Go to Communication Compliance > Policies.
3. Select the policy where filters were applied.
4. On the Policy page, select the Pending or Resolved tab.
5. Click Filters and uncheck any language filter checkboxes that were selected.
6. Click Apply to remove the language filter and restore the default view.
7. If a filter query was saved, click Filters, locate the saved query under 'Saved filter queries', and delete it by selecting the delete option (e.g., trash icon) next to the query name.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
