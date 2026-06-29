# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
How to configure protection settings for groups and sites in sensitivity labels after enabling labels for containers?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Sensitivity labels enabled for containers

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Follow the general instructions to create or edit a sensitivity label and make sure you select Groups & sites for the label's scope.
2. On the Define protection settings for groups and sites page, select the options you want to configure: Privacy and external user access settings, External sharing and Conditional Access settings, Private teams discoverability and shared channel controls, and Apply a label to channel meetings.

## Validation
1. Verify that the sensitivity label is published and applied to a test Microsoft 365 group or team. 2. Run the following PowerShell command to confirm the label's protection settings: Get-AzureADMSGroup -SearchString '<GroupName>' | Select-Object -Property Id, DisplayName, Mail, Visibility, 'Microsoft 365 Label' | Format-List. 3. Check that the group's privacy setting matches the label configuration (e.g., Private or Public). 4. Confirm external user access is restricted as defined by the label. 5. Validate that external sharing settings for the associated SharePoint site are enforced per the label. 6. Ensure Conditional Access policies are applied correctly by testing access from an unmanaged device. 7. Verify that private teams discoverability and shared channel controls are set as expected. 8. Confirm that the label is applied to channel meetings by creating a new channel meeting and checking the meeting options.

## Rollback
1. Remove the sensitivity label from the affected groups and sites by reassigning a different label or no label via the Microsoft Purview compliance portal. 2. In PowerShell, run: Set-AzureADMSGroup -Id '<GroupId>' -MailEnabled $false -SecurityEnabled $true -Visibility 'Private' to reset privacy to default. 3. Reset external user access settings by running: Set-AzureADMSGroup -Id '<GroupId>' -AllowExternalMembers $true. 4. For SharePoint sites, use: Set-SPOSite -Identity '<SiteURL>' -SharingCapability ExternalUserAndGuestSharing to restore default sharing. 5. Remove any Conditional Access policy assignments that were tied to the label. 6. Reset private teams discoverability by setting: Set-Team -GroupId '<GroupId>' -ShowInTeamsSearchAndSuggestions $true. 7. Disable shared channel controls by running: Set-Team -GroupId '<GroupId>' -AllowSharedChannels $true. 8. Remove the label from channel meetings by clearing the meeting label policy in Teams admin center.

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
