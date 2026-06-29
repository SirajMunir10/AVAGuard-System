# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
How do I configure privacy settings for containers using sensitivity labels in Microsoft Purview?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Sensitivity labels configured for containers (Teams, Groups, Sites)

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Keep the default of Public if you want anyone in your organization to access the container where this label is applied.
2. Select Private if you want access to be restricted to only approved members in your organization.
3. Select None when you want to protect content in the container by using the sensitivity label, but still let users configure the privacy setting themselves.
4. The settings of Public or Private set and lock the privacy setting when you apply this label to the container.
5. Your chosen setting replaces any previous privacy setting that might be configured for the container, and locks the privacy value so it can be changed only by first removing the sensitivity label from the container.
6. After you remove the sensitivity label, the privacy setting from the label remains and users can now change it again.

## Validation
1. Verify the sensitivity label is published and applied to a test container (e.g., Microsoft 365 Group or Teams team).
2. Run: Get-UnifiedGroup -Identity <GroupName> | fl AccessType, SensitivityLabel
   Confirm AccessType matches the configured privacy (Public/Private/None).
3. Attempt to change the container’s privacy setting via Teams or SharePoint admin center; verify it is locked (cannot be changed) when label is applied.
4. Remove the label from the container and confirm the privacy setting remains as set by the label, and that users can now modify it.

## Rollback
1. If the privacy setting is incorrect or causes access issues, remove the sensitivity label from the container:
   Set-UnifiedGroup -Identity <GroupName> -SensitivityLabelIdentity $null
2. Manually adjust the container’s privacy setting to the desired value:
   Set-UnifiedGroup -Identity <GroupName> -AccessType (Public/Private)
3. If the label was set to 'None', no rollback is needed as users retain control.
4. Re-publish the original label if needed, ensuring the privacy setting is set correctly before applying.

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
