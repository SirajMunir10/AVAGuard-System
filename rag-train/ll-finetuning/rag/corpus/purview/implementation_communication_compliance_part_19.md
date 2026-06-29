# Implementation: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Implementation

## Scenario / Query
How do I apply a custom tag to multiple policy matches in bulk in Communication Compliance?

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
2. Select the checkboxes for multiple policy matches if you want to apply a custom tag in bulk.
3. Select Tag as on the command bar.
4. In the Tag item pane, select Add a new tag.
5. Enter the name of the new tag, then press Enter to add the new tag.
6. Select the checkbox for the new tag to apply it to the policy match.
7. In the Comment box, add a comment to describe the purpose of the tag (optional).
8. Select Save.

## Validation
1. Navigate to Microsoft Purview compliance portal > Communication Compliance > Policies. 2. Select the policy used in the bulk tagging operation. 3. Verify that the policy matches previously selected now display the custom tag in the 'Tags' column. 4. Click on a tagged match to open details and confirm the tag name and optional comment appear in the 'Tags' section. 5. Run the following PowerShell command to confirm the tag is applied: Get-CommunicationCompliancePolicy -Identity "<PolicyName>" | Get-CommunicationComplianceMessage -Tag "<CustomTagName>" | Format-Table Subject, Tags

## Rollback
1. Navigate to Microsoft Purview compliance portal > Communication Compliance > Policies. 2. Select the policy where the custom tag was applied. 3. Select the policy matches that were bulk-tagged. 4. On the command bar, select 'Tag as' and then 'Clear tag'. 5. In the 'Tag item' pane, uncheck the custom tag and select 'Save'. 6. Alternatively, run the following PowerShell command to remove the tag from all affected messages: Get-CommunicationCompliancePolicy -Identity "<PolicyName>" | Get-CommunicationComplianceMessage -Tag "<CustomTagName>" | ForEach-Object { Set-CommunicationComplianceMessage -Identity $_.Identity -Tags @() }

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
