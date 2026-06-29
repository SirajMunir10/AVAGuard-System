# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
How to configure private team discoverability and shared channel controls for a sensitivity label?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Sensitivity labels with container settings for Teams

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
5. Options include 'Internal only', 'Same label only', and 'Private team only'.
6. Only the last option can potentially remove previously invited teams, and none of the options affect invitations to individual users.

## Validation
1. Verify that the sensitivity label is applied to a private team. 2. Navigate to Teams admin center > Teams > Manage teams, select the team, and check 'Discoverability' to confirm the setting matches the label configuration. 3. As a user who is allowed to discover private teams, search for the team in Teams; if the checkbox was selected, the team should appear; if cleared, it should not. 4. For shared channels, in the same team properties, check 'Shared channel settings' to confirm the invited teams restriction matches the label option (Internal only, Same label only, or Private team only). 5. Attempt to invite a team from outside the allowed scope and verify the invitation is blocked.

## Rollback
1. Edit the sensitivity label in Microsoft Purview compliance portal > Information protection > Labels. 2. Under 'Teams and groups settings', adjust the 'Allow users to discover private teams that have this label applied' checkbox to the previous state. 3. For shared channels, change the 'Allow other teams to be invited to this team's shared channels' option to the previous setting. 4. Save the label changes and wait for replication (up to 24 hours). 5. Reapply the label to the team if necessary via Teams admin center or PowerShell.

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
