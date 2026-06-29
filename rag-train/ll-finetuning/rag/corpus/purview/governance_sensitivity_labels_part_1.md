# Governance: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Governance

## Scenario / Query
How do sensitivity labels for containers affect Teams shared channels?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Teams shared channels with sensitivity labels

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. If a team has any shared channels, they automatically inherit sensitivity label settings from their parent team.
2. The inherited label cannot be removed or replaced with a different label.

## Validation
1. Confirm that the parent team has a sensitivity label assigned by running: Get-UnifiedGroup -Identity <TeamName> | fl SensitivityLabel. 2. Verify that any shared channel under that team shows the same label by running: Get-UnifiedGroup -Identity <SharedChannelMailbox> | fl SensitivityLabel. 3. Attempt to change the label on the shared channel via Set-UnifiedGroup -Identity <SharedChannelMailbox> -SensitivityLabel <DifferentLabelGuid> and confirm the command fails with an error indicating inheritance. 4. Check the audit log for label assignment events on the shared channel to ensure no unauthorized label changes occurred.

## Rollback
1. If the remediation (assigning a label to the parent team) caused unintended access restrictions, remove the label from the parent team by running: Set-UnifiedGroup -Identity <TeamName> -SensitivityLabel $null. 2. Verify that the shared channels now show no label: Get-UnifiedGroup -Identity <SharedChannelMailbox> | fl SensitivityLabel. 3. If the parent team label cannot be removed due to policy, adjust the label policy in the Microsoft Purview compliance portal to exclude the team or modify its settings. 4. Reapply any previous label configuration using Set-UnifiedGroup with the original label GUID if known.

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
