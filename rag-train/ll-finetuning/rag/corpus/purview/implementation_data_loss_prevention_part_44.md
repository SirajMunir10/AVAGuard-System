# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How do I configure DLP policy actions for Exchange, SharePoint, and OneDrive locations?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with conditions filter

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select Exchange with the Restrict access or encrypt the content in Microsoft 365 locations action.
2. Choose from these options: Block users from accessing shared SharePoint, OneDrive, and Teams content; Block everyone (only the content owner, last modifier, and site admin will continue to have access); Block only people from outside your organization (users inside your organization continue to have access); Encrypt email messages (applies only to content in Exchange).

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Select the DLP policy that was configured. 3. Under 'Locations', confirm that Exchange, SharePoint, and OneDrive are toggled on. 4. Under 'Actions', verify that for Exchange the action 'Restrict access or encrypt the content in Microsoft 365 locations' is selected. 5. For SharePoint and OneDrive, confirm the chosen action (e.g., 'Block users from accessing shared SharePoint, OneDrive, and Teams content' or 'Block everyone' or 'Block only people from outside your organization'). 6. Use Test-DlpPolicy (PowerShell) to simulate a policy match and confirm the intended action is triggered.

## Rollback
1. In Microsoft Purview compliance portal > Data Loss Prevention > Policies, select the DLP policy. 2. Under 'Locations', uncheck Exchange, SharePoint, or OneDrive as needed to disable the policy for those workloads. 3. Alternatively, under 'Actions', change the action to 'Notify users with email and policy tip' (no restrictive action) or remove the restrictive action entirely. 4. If the policy was created via PowerShell, use Remove-DlpCompliancePolicy -Identity <PolicyName> to delete it, or use Set-DlpCompliancePolicy -Identity <PolicyName> -ExchangeLocation $null -SharePointLocation $null -OneDriveLocation $null to remove locations.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
