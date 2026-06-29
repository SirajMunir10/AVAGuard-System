# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to configure DLP policy actions for adding recipients to To, Cc, or Bcc boxes with restrictions?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with actions 'Add recipient to the To box', 'Add recipient to the Cc box', 'Add recipient to the Bcc box'

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure recipient count is <= 10.
2. Ensure recipients cannot be distribution lists (DL) or security groups (SG).
3. Configure the DLP policy action accordingly.

## Validation
1. Open the Microsoft Purview compliance portal (https://compliance.microsoft.com).
2. Navigate to Data Loss Prevention > Policies.
3. Select the DLP policy that was configured with the 'Add recipient to the To/Cc/Bcc box' action.
4. Click 'Edit policy' and go to the 'Actions' section for the relevant rule.
5. Verify that the action 'Add recipient to the To box', 'Add recipient to the Cc box', or 'Add recipient to the Bcc box' is present.
6. Confirm that the recipient list contains no more than 10 entries.
7. Confirm that none of the recipients are distribution lists or security groups (i.e., all recipients are individual user mailboxes or mail-enabled users).
8. Use the 'Test with sample data' feature (if available) to simulate a DLP rule match and verify that the specified recipients are added to the message headers as expected.
9. Optionally, run the following PowerShell command to retrieve the DLP policy configuration and inspect the action details:
   Get-DlpComplianceRule -Identity "<RuleName>" | Format-List Actions

## Rollback
1. Open the Microsoft Purview compliance portal (https://compliance.microsoft.com).
2. Navigate to Data Loss Prevention > Policies.
3. Select the DLP policy that contains the problematic action.
4. Click 'Edit policy' and go to the 'Actions' section for the rule that includes the 'Add recipient to the To/Cc/Bcc box' action.
5. Remove the action entirely by unchecking or deleting the 'Add recipient to the To box', 'Add recipient to the Cc box', or 'Add recipient to the Bcc box' action.
6. Alternatively, modify the recipient list to comply with the restrictions (reduce to 10 or fewer recipients and ensure no distribution lists or security groups are included).
7. Save the policy changes and allow time for replication.
8. If the policy was recently created and causes issues, consider disabling the policy temporarily by setting its state to 'Disabled' in the policy settings.
9. To revert via PowerShell, use:
   Set-DlpComplianceRule -Identity "<RuleName>" -RemoveActions @("AddRecipientToToBox", "AddRecipientToCcBox", "AddRecipientToBccBox")
   (Replace with the specific action(s) that need to be removed.)

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
