# Implementation: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Implementation

## Scenario / Query
How do I configure the policy match preservation time period for a communication compliance policy?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Communication Compliance policy settings

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select the More actions (ellipsis) button in the row for the policy you want to change, then select Edit.
2. On the Name and describe your policy page in the policy workflow, under Preserve policy matches, make a selection.
3. If you leave the Global Setting selection, the policy uses the time period selected in the global Policy Match Preservation setting.
4. If you choose any other time period, it takes precedence over the selection in the global setting.

## Validation
1. Navigate to Microsoft Purview compliance portal > Communication Compliance > Policies. 2. Select the policy you edited, then click 'Edit'. 3. On the 'Name and describe your policy' page, verify that the 'Preserve policy matches' dropdown shows the expected time period (e.g., '7 days', '30 days', or 'Global Setting'). 4. If a custom time period was set, confirm it differs from the global setting by checking the global setting at Communication Compliance > Settings > Policy Match Preservation. 5. Use PowerShell: `Get-CommunicationCompliancePolicy -Identity "<PolicyName>" | fl RetentionDuration` to confirm the retention duration value matches the chosen period.

## Rollback
1. Navigate to Microsoft Purview compliance portal > Communication Compliance > Policies. 2. Select the policy you changed, click 'More actions' (ellipsis) > 'Edit'. 3. On the 'Name and describe your policy' page, under 'Preserve policy matches', select the previous time period or 'Global Setting' to revert. 4. If reverting to global, confirm the global setting at Communication Compliance > Settings > Policy Match Preservation is set to the desired default. 5. Use PowerShell: `Set-CommunicationCompliancePolicy -Identity "<PolicyName>" -RetentionDuration <PreviousValue>` to restore the original retention duration.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
