# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
How to apply sensitivity labels to Microsoft 365 groups?

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
1. Return to the Microsoft Entra documentation for instructions: Assign a label to a new group in Azure portal
2. Assign a label to an existing group in Azure portal
3. Remove a label from an existing group in Azure portal

## Validation
1. In the Microsoft Entra admin center, navigate to Identity > Groups > All groups. Select the target group and verify that the 'Sensitivity' field displays the expected label. 2. For a new group, create a group via the Azure portal and confirm the 'Sensitivity' dropdown includes the desired label. 3. Use Microsoft Graph PowerShell: `Get-MgGroup -GroupId <GroupId> | Select-Object Id, DisplayName, SensitivityLabelId` to confirm the label ID matches the expected label's ID from the Purview compliance portal.

## Rollback
1. In the Microsoft Entra admin center, go to Identity > Groups > All groups, select the group, and under 'Properties', change the 'Sensitivity' dropdown to '(None)' or a previous label. 2. For a newly created group with an incorrect label, delete the group via the Azure portal or PowerShell: `Remove-MgGroup -GroupId <GroupId>`. 3. Use Microsoft Graph PowerShell to remove a label: `Update-MgGroup -GroupId <GroupId> -SensitivityLabelId $null`.

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
