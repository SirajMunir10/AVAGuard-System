# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
How to apply a sensitivity label to a new team in Microsoft Teams?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Sensitivity labels configured in Microsoft Purview compliance portal

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Users can select sensitivity labels when they create new teams in Microsoft Teams.
2. When they select the label from the Sensitivity dropdown, the privacy setting might change to reflect the label configuration.
3. Depending on the external users access setting you selected for the label, users can or can't add people outside the organization to the team.
4. After you create the team, the sensitivity label appears in the upper-right corner of all channels.
5. The service automatically applies the same sensitivity label to the Microsoft 365 group and the connected SharePoint team site.

## Validation
1. In Microsoft Teams, create a new team and verify that the 'Sensitivity' dropdown appears in the team creation wizard. 2. Select a sensitivity label that has been published to the user and confirm that the privacy setting (Public/Private) automatically adjusts according to the label's configuration. 3. After the team is created, check that the sensitivity label name is displayed in the upper-right corner of every channel within the team. 4. In the Microsoft 365 admin center, navigate to Groups and locate the associated Microsoft 365 group; confirm that the same sensitivity label is applied to the group. 5. In SharePoint Online, open the connected team site and verify that the sensitivity label is also applied to the site.

## Rollback
1. If the sensitivity label is not visible or cannot be selected during team creation, ensure that the label is published to the user or group in the Microsoft Purview compliance portal (Sensitivity labels > Label policies). 2. If the privacy setting does not change as expected, edit the sensitivity label in the Purview compliance portal and verify that the 'Privacy and external user access' settings are configured correctly. 3. If the label does not appear on channels after creation, remove the label from the team by editing the team settings in Teams and selecting 'None' for sensitivity, then reapply the label. 4. If the label is not applied to the Microsoft 365 group or SharePoint site, use PowerShell (Set-UnifiedGroup -Identity <GroupName> -SensitivityLabel <LabelGuid>) to manually assign the label to the group, which will propagate to the site.

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
