# Implementation: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Implementation

## Scenario / Query
How do I create a custom tag for a policy match in Communication Compliance?

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
1. On Policies, select a policy to view the policy matches for that policy.
2. Select the checkbox for the policy match that you want to create a custom tag for.
3. Select Tag as on the command bar.
4. In the Tag item pane, select Add a new tag.
5. Enter the name of the new tag, then press Enter to add the new tag.
6. Select the checkbox for the new tag to apply it to the policy match.
7. In the Comment box, add a comment to describe the purpose of the tag (optional).
8. Select Save.

## Validation
1. Navigate to Microsoft Purview compliance portal > Communication Compliance > Policies. 2. Select the policy used in remediation. 3. Verify the policy match list includes the match that was tagged. 4. Select that match and confirm the 'Tag' column displays the custom tag name. 5. Open the match details and check the 'Tags' section shows the custom tag and optional comment.

## Rollback
1. In the same policy match list, select the checkbox for the match with the custom tag. 2. Select 'Tag as' on the command bar. 3. In the 'Tag item' pane, clear the checkbox for the custom tag. 4. Optionally, delete the custom tag by selecting 'Add a new tag', clicking the 'X' next to the tag name, and confirming removal. 5. Select 'Save'.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
