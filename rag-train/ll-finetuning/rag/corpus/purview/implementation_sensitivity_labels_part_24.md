# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
How do I configure private team discoverability and shared channel controls for a sensitivity label applied to a Microsoft 365 group or team?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Sensitivity labels configured for containers (Teams, groups, sites) with scope including groups and sites

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. For Private teams discoverability, use the 'Allow users to discover private teams that have this label applied' checkbox when you've configured a Teams policy that allows private teams discovery.
2. When the checkbox is selected (the default setting), a private team with the sensitivity label applied will be discoverable for a user who is allowed to discover private teams.
3. When the checkbox is cleared, a private team with the sensitivity label applied will remain hidden and won't be discoverable for all users.
4. For Teams shared channels, when a team has a sensitivity label applied, you can allow or prevent other teams from being invited to the original team's shared channels.
5. Options for Teams shared channels include: Internal only, Same label only, and Private team only.
6. Only the last option (Private team only) can potentially remove previously invited teams, and none of the options affect invitations to individual users.
7. If you select an option that's not compatible with previous settings on the Privacy and external user access page, you see a validation message to change your selection. Alternatively, you can go back in the configuration to change the dependent setting.

## Validation
1. Verify the sensitivity label is applied to a test Microsoft 365 group or team. 2. For private team discoverability: a. Confirm the 'Allow users to discover private teams that have this label applied' checkbox is selected or cleared as intended. b. As a user with permissions to discover private teams, search for the team in Teams to confirm it appears (if enabled) or does not appear (if disabled). 3. For shared channel controls: a. Check the current shared channel settings for the team by running: Get-TeamChannel -GroupId <GroupId> | Where-Object {$_.MembershipType -eq 'Shared'} | Select-Object DisplayName, MembershipType. b. Attempt to invite a team from another tenant or with a different label to a shared channel and confirm the invitation is allowed or blocked per the configured option (Internal only, Same label only, Private team only). c. If the option is set to 'Private team only', verify that previously invited teams from other tenants or labels are removed from the shared channel membership.

## Rollback
1. To revert private team discoverability: a. Navigate to the sensitivity label configuration in the Microsoft Purview compliance portal. b. Change the 'Allow users to discover private teams that have this label applied' checkbox to its previous state (select if it was cleared, clear if it was selected). c. Save the label configuration. 2. To revert shared channel controls: a. In the same sensitivity label configuration, change the shared channel option back to the previous setting (e.g., from 'Private team only' to 'Same label only' or 'Internal only'). b. If the previous setting allowed broader sharing, re-invite any teams that were removed by the change. c. If a validation message appears due to incompatibility with the Privacy and external user access page, adjust the dependent setting on that page to match the previous configuration.

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
