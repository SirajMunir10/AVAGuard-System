# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
How to configure site sharing permissions for a SharePoint site using PowerShell advanced settings with a sensitivity label?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Sensitivity labels applied to SharePoint sites

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the Set-Label cmdlet with the -AdvancedSettings parameter to configure the MembersCanShare setting.
2. Example: Set-Label -Identity 8faca7b8-8d20-48a3-8ea2-0f96310a848e -AdvancedSettings @{MembersCanShare="MemberShareNone"}
3. The three options for MembersCanShare are: MemberShareAll (Site owners and members can share files, folders, and the site), MemberShareFileAndFolder (Site owners and members, and people with Edit permissions can share files and folders, but only site owners can share the site), MemberShareNone (Only site owners can share files, folders, and the site).

## Validation
Run the following PowerShell command to confirm the sensitivity label's MembersCanShare setting: Get-Label -Identity 8faca7b8-8d20-48a3-8ea2-0f96310a848e | Format-List AdvancedSettings. Verify that the output includes 'MembersCanShare' with the expected value (e.g., 'MemberShareNone'). Additionally, test the SharePoint site sharing behavior by attempting to share a file or the site as a member; only site owners should be able to share if the setting is 'MemberShareNone'.

## Rollback
To revert the change, run: Set-Label -Identity 8faca7b8-8d20-48a3-8ea2-0f96310a848e -AdvancedSettings @{MembersCanShare="MemberShareAll"}. Then confirm the rollback by running Get-Label -Identity 8faca7b8-8d20-48a3-8ea2-0f96310a848e | Format-List AdvancedSettings to ensure the value is restored to 'MemberShareAll'.

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
