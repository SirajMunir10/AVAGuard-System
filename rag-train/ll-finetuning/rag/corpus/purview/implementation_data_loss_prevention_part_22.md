# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to scope DLP policies using administrative units in Microsoft Purview?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Administrative units configured in Entra ID

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Understand the difference between an unrestricted admin and an administrative unit restricted admin.
2. Apply unrestricted admin scope policies to all of the following in your organization (depending on the locations that are selected) or to subgroups of your organization, called Administrative Unit restricted policies: distribution groups, cloud app instances, on-premises repositories, Fabric and Power BI workspaces.
3. For administrative unit restricted admin, only pick from the administrative units that they're assigned to.
4. Note that DLP supports admin unit scoping for some of the locations protected under Enterprise applications & devices.
5. At the second level of DLP policy scoping, both unrestricted and administrative unit restricted administrators see only the users, distribution groups, groups, and accounts that were included in the first level of policy scoping and that are available for that location.

## Validation
1. Confirm that the DLP policy is scoped to the intended administrative unit by running: Get-DlpCompliancePolicy -Identity "PolicyName" | Format-List Name, ExchangeLocation, SharePointLocation, OneDriveLocation, TeamsLocation, EndpointDlpLocation, PowerBILocation, ThirdPartyAppLocation, AdminUnits. 2. Verify that the policy applies only to members of the specified administrative unit by checking that users/groups outside the unit are not affected: Get-DlpComplianceRule -Policy "PolicyName" | Format-List Name, Condition, Action. 3. For unrestricted admin policies, confirm that the policy scope includes all relevant locations (e.g., all distribution groups, cloud app instances) by reviewing the policy in the Microsoft Purview compliance portal under Data Loss Prevention > Policies > select policy > Edit policy > Locations.

## Rollback
1. Remove the administrative unit restriction from the DLP policy by setting the AdminUnits parameter to $null: Set-DlpCompliancePolicy -Identity "PolicyName" -AdminUnits $null. 2. If the policy was newly created, delete it: Remove-DlpCompliancePolicy -Identity "PolicyName". 3. Revert to the previous policy configuration by restoring from a backup or reapplying the original policy settings. 4. For unrestricted admin policies, narrow the scope back to the original set of locations if the broad scope caused unintended enforcement.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
