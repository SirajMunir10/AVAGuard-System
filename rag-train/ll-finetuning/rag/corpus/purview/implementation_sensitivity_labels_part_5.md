# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
How to enable sensitivity labels for containers and synchronize labels to Microsoft Entra ID?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Sensitivity labels for containers (Microsoft 365 groups, Teams, and SharePoint sites)

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Follow the instructions from the Microsoft Entra documentation to enable sensitivity label support: Assign sensitivity labels to Microsoft 365 groups in Microsoft Entra ID.
2. Connect to Security & Compliance PowerShell. For example, in a PowerShell session that you run as administrator, sign in with a global administrator account.
3. Run the following command to ensure your sensitivity labels can be used with Microsoft 365 groups: Execute-AzureAdLabelSync

## Validation
1. In Microsoft Entra admin center, go to Groups > All groups, select a group, and verify that 'Sensitivity' label is visible and can be assigned. 2. Connect to Security & Compliance PowerShell as administrator, run `Get-AzureADMSGroup | Select-Object DisplayName, MailNickname, SensitivityLabelId` to confirm labels are applied. 3. In SharePoint admin center, check a site's settings to ensure the sensitivity label is enforced.

## Rollback
1. In Microsoft Entra admin center, navigate to Groups > Settings > General and disable 'Sensitivity labels for Microsoft 365 groups' if enabled. 2. Connect to Security & Compliance PowerShell and run `Execute-AzureAdLabelSync -Force` to revert label synchronization. 3. Remove any assigned sensitivity labels from groups via Microsoft Entra admin center or PowerShell.

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
