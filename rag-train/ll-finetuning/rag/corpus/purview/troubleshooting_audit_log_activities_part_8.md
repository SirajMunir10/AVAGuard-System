# Troubleshooting: Audit Log Activities

**Domain:** Purview
**Subdomain:** Audit Log Activities
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify changes to Teams settings such as interoperability, org chart view, private meeting scheduling, channel meeting scheduling, video calling, screen sharing, Giphys, content rating, custom memes, stickers, bots, extensions, side-loading of bots, or channel email?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log search enabled

## Symptoms
- Teams setting changed (e.g., interoperability, org chart view, private meeting scheduling, channel meeting scheduling, video for Skype meetings, screen sharing for Skype meetings, animated images, content rating, customizable images from internet, editable images, org-wide bots, individual bots, extensions or tabs, side loading of bots, channel email)

## Error Codes
N/A

## Root Causes
1. Team owner performed a TeamSettingChanged operation

## Remediation Steps
1. Search audit log for TeamSettingChanged operation
2. Review Item column for description of setting changed (e.g., 'Skype for Business interoperability', 'Org chart view', 'Private meeting scheduling', 'Channel meeting scheduling', 'Video for Skype meetings', 'Screen sharing for Skype meetings', 'Animated images', 'Content rating', 'Customizable images from the Internet', 'Editable images', 'Org-wide bots', 'Individual bots', 'Extensions or tabs', 'Side loading of Bots', 'Channel email')

## Validation
Search the unified audit log for the TeamSettingChanged operation and confirm that the Item column contains the expected setting description (e.g., 'Skype for Business interoperability', 'Org chart view', 'Private meeting scheduling', 'Channel meeting scheduling', 'Video for Skype meetings', 'Screen sharing for Skype meetings', 'Animated images', 'Content rating', 'Customizable images from the Internet', 'Editable images', 'Org-wide bots', 'Individual bots', 'Extensions or tabs', 'Side loading of Bots', 'Channel email'). Use the following command in the Microsoft 365 Defender portal or via Search-UnifiedAuditLog -Operations TeamSettingChanged -StartDate <date> -EndDate <date> and verify that the Item property matches the changed setting.

## Rollback
If the remediation fails or causes issues, restore the Teams setting to its previous value by having a Teams administrator navigate to the Teams admin center, select the affected team, go to Settings, and manually revert the specific setting (e.g., disable interoperability, turn off org chart view, disable private meeting scheduling, etc.). Alternatively, use the Set-Team PowerShell cmdlet with the appropriate parameter (e.g., Set-Team -GroupId <id> -AllowCreatePrivateMeetings $false) to revert the change. No automated rollback is available via audit log alone.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
