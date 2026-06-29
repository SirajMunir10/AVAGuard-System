# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
How do I create and publish a sensitivity label configured for sites and groups in Microsoft Purview?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Sensitivity labels configured for site and group settings

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Create and configure the sensitivity label with site and group settings.
2. Add this label to a label policy that applies to just a few test users.
3. Wait for the change to replicate: For a new label, wait at least one hour, unless your configured settings include Teams shared channel controls. If that's the case, wait at least 24 hours. For an existing label, wait at least 24 hours.
4. After this wait period, use one of the test user accounts to create a team, Microsoft 365 group, or SharePoint site with the label that you created.
5. If there are no errors during this creation operation, it is safe to publish the label to all users in your tenant.

## Validation
1. Sign in to the Microsoft Purview compliance portal (https://compliance.microsoft.com) as a test user included in the label policy. 2. Navigate to Microsoft Teams, SharePoint, or Outlook to create a new team, Microsoft 365 group, or SharePoint site. 3. During creation, verify that the newly created sensitivity label appears in the sensitivity picker. 4. Select the label and complete the creation. 5. Confirm that the team, group, or site is created without errors. 6. As an admin, go to the Microsoft Purview compliance portal > Information protection > Label policies, select the policy, and verify the label is listed under 'Labels'. 7. Use the Get-AzureADMSGroup cmdlet in PowerShell to check the assigned label on the created group: Get-AzureADMSGroup -SearchString '<GroupName>' | Select-Object Id, DisplayName, Mail, AssignedLabels.

## Rollback
1. If the label causes issues during creation of teams, groups, or sites, remove the label from the test policy: In the Microsoft Purview compliance portal, go to Information protection > Label policies, select the policy, and under 'Labels to publish', remove the problematic label. 2. If the label was already published to all users, create a new label policy that excludes all users and assign it to the label to effectively block its application: In the label policy, set 'Users and groups' to 'None' or remove all assigned users. 3. Alternatively, delete the label entirely: In the Microsoft Purview compliance portal, go to Information protection > Labels, select the label, and choose 'Delete label'. Note: Deleting a label may take up to 24 hours to replicate and will not remove the label from already labeled content. 4. For PowerShell rollback, use Remove-Label -Identity '<LabelName>' after connecting to Security & Compliance Center PowerShell.

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
