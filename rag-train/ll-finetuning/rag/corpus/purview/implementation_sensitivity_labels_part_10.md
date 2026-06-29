# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
How do I apply a sensitivity label to channel meetings and channel chats?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Sensitivity labels with scope including meetings

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. This additional option is applicable only if you are editing an existing label where the scope includes meetings, and you've configured labels to protect meetings.
2. Select a sensitivity label to automatically apply to channel meetings and all channel chats.
3. For non-channel meetings, you can select a default label as a policy setting.

## Validation
1. Verify that the sensitivity label is published and scoped to meetings: Run `Get-Label | Where-Object {$_.Settings -match 'Meetings'}` in the Security & Compliance PowerShell. 2. Confirm the label is applied to a channel meeting: Create a new channel meeting in Teams, then run `Get-Meeting -Identity '<meeting-id>' | Select-Object SensitivityLabel` to check the label. 3. Check channel chat labeling: Send a message in the associated channel chat, then use `Get-ChatMessage -ChatId '<chat-id>' | Select-Object SensitivityLabel` to verify the label is applied.

## Rollback
1. Remove the automatic label assignment for channel meetings: In the Purview compliance portal, edit the sensitivity label and clear the 'Automatically apply this label to channel meetings' option. 2. Reset the default label for non-channel meetings: In the label policy settings, set the default label to 'None' or remove the label assignment. 3. If the label was incorrectly applied to existing meetings or chats, use `Set-Meeting -Identity '<meeting-id>' -SensitivityLabel $null` and `Set-ChatMessage -ChatId '<chat-id>' -SensitivityLabel $null` to remove the label.

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
