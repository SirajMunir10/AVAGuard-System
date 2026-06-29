# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
How do I configure private teams discoverability and shared channel controls for sensitivity labels?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Sensitivity labels with scope including groups and sites

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. On the Define protection settings for groups and sites page, select the options you want to configure: Private teams discoverability and shared channel controls.
2. Configure the settings to prevent users who can discover private teams from finding a private team with this sensitivity label applied.
3. Configure channel sharing controls for invitations to other teams.

## Validation
1. Verify that the sensitivity label is applied to a test private team. 2. As a user who is not a member of that team, attempt to discover the team via the Teams client search or the 'Discover private teams' option. Confirm that the team does not appear in search results. 3. As a team owner, attempt to share a channel with a user from another organization or team. Confirm that the sharing option is blocked or restricted according to the configured controls. 4. Use the Get-SensitivityLabel PowerShell cmdlet to confirm the label's policy settings for groups and sites are correctly applied.

## Rollback
1. Navigate to the Microsoft Purview compliance portal > Information protection > Sensitivity labels. 2. Edit the sensitivity label that was modified. 3. On the 'Define protection settings for groups and sites' page, revert the private teams discoverability setting to its original state (e.g., 'Allow users who can discover private teams to find this team'). 4. Revert the shared channel controls to allow invitations to other teams as previously configured. 5. Save the label changes and publish the updated label policy. 6. Verify that the previous behavior is restored by repeating the validation steps.

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
