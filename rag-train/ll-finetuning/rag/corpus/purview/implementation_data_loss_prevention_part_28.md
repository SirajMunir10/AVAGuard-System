# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to configure DLP policy locations for Exchange Online, SharePoint, OneDrive, Teams, and other Microsoft services?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy location scoping

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. For Exchange Online, use distribution groups (assigned or dynamic), security groups, non-email enabled security groups (assigned or dynamic), or Microsoft 365 groups (assigned or dynamic) for data-in-motion site locations, and in preview, adaptive scopes at the policy level.
2. If the policy is scoped to an administrative unit that includes SharePoint sites, the policy will only apply to all sites in the administrative unit, no further scoping is possible for data-at-rest and data-in-use.
3. For SharePoint sites and OneDrive accounts, use distribution groups, security groups, non-email enabled security groups, or Microsoft 365 groups (group members only, not the group as an entity) for data-at-rest and data-in-use.
4. For Teams chat and channel messages, use distribution groups, security groups, mail-enabled security groups, or Microsoft 365 groups (group members only, not the group as an entity) for data-in-motion and data-in-use.
5. For cloud app instances (non-Microsoft cloud apps), use distribution groups, security groups, non-email enabled security groups, Microsoft 365 groups (group members only, not the group as an entity), or dynamic groups for data-at-rest, data-in-use, and data-in-motion.
6. For on-premises repositories (file shares and SharePoint), use data-at-rest location.
7. For Fabric and Power BI, use data-in-use location.
8. For third-party apps and Microsoft 365 Copilot (preview), use account or distribution group for data-at-rest and data-in-use, only available in the Custom policy template.
9. For managed cloud apps, use account or distribution group for data-in-motion, only available in the Custom policy template.
10. For unmanaged cloud apps, use account or distribution group for data-in-motion, only available in the Custom policy template.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Select the DLP policy you configured. 3. Under 'Locations', verify that the correct services (Exchange, SharePoint, OneDrive, Teams, etc.) are toggled on. 4. For each location, click 'Edit' and confirm that the included groups or scopes match the intended configuration (e.g., distribution groups, security groups, adaptive scopes). 5. Use the 'Test' option (if available) to simulate a DLP rule match for each location. 6. Run the following PowerShell commands to validate policy assignment: Get-DlpCompliancePolicy -Identity "<PolicyName>" | Format-List ExchangeLocation, SharePointLocation, OneDriveLocation, TeamsLocation, AdditionalLocations. 7. Check the DLP policy reports in Purview to confirm that policy matches are being generated for the expected locations.

## Rollback
1. In Microsoft Purview compliance portal > Data Loss Prevention > Policies, select the policy. 2. Under 'Locations', toggle off any location that was incorrectly added or remove the specific groups/scopes that caused issues. 3. If the entire policy is problematic, delete the policy by selecting it and clicking 'Delete policy'. 4. Alternatively, use PowerShell: Remove-DlpCompliancePolicy -Identity "<PolicyName>" to remove the policy. 5. If only a specific location scope needs to be reverted, use Set-DlpCompliancePolicy -Identity "<PolicyName>" -ExchangeLocation $null (or other location parameters) to clear the location. 6. Reapply any previous working configuration from backup or documentation.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
