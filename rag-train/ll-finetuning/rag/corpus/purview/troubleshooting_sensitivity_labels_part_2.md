# Troubleshooting: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Troubleshooting

## Scenario / Query
How to safely delete a published sensitivity label configured for sites and groups to avoid creation failures for new teams, groups, and sites?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Sensitivity labels with site and group settings enabled, included in label policies

## Symptoms
- Creation failures for new teams, groups, and sites

## Error Codes
N/A

## Root Causes
1. Deleting a sensitivity label that has site and group settings enabled and is included in one or more label policies

## Remediation Steps
1. Remove the sensitivity label from all label policies that include the label.
2. Wait at least one hour.
3. After this wait period, try creating a team, group, or site and confirm that the label is no longer visible.
4. If the sensitivity label isn't visible, you can now safely delete the label.

## Validation
After the wait period, try creating a team, group, or site and confirm that the label is no longer visible.

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
