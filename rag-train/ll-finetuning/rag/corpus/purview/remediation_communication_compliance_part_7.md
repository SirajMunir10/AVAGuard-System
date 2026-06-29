# Remediation: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Remediation

## Scenario / Query
How do I edit or delete a custom tag applied to a policy match in Communication Compliance?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Communication Compliance policy with custom tags

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. On Policies, select a policy to view the policy matches for that policy.
2. Select the checkbox for the policy match that has the custom tag you want to edit.
3. Select Tag as on the command bar.
4. In the Tag item pane, select the ellipsis next to the custom tag.
5. Select Edit, make your changes, or select Delete to delete the tag.
6. Select Save.

## Validation
1. Navigate to Microsoft Purview compliance portal > Communication Compliance > Policies. 2. Select the policy where the custom tag was edited or deleted. 3. Locate the specific policy match that previously had the custom tag. 4. Verify that the tag now displays the updated label (if edited) or no longer appears (if deleted). 5. Optionally, use the 'Export items' feature to confirm the tag change is reflected in the exported report.

## Rollback
1. On the same policy match, select the checkbox again. 2. Click 'Tag as' on the command bar. 3. In the Tag item pane, select the ellipsis next to the custom tag. 4. If the tag was edited, select 'Edit' and revert to the original label, then 'Save'. 5. If the tag was deleted, you must re-create the custom tag by selecting 'Add tag' and entering the original tag name and color, then 'Save'. 6. Confirm the tag is restored by viewing the policy match details.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
