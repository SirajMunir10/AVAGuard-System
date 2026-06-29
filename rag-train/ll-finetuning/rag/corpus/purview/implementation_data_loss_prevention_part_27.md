# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to implement DLP policies scoped to administrative units in Microsoft Purview?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Administrative units configured in Microsoft Entra ID

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Assign administrative unit admins to one of the same roles or role groups as administrators of unrestricted DLP policies to create and manage DLP policies for their administrative unit.
2. Unrestricted administrators can create and scope DLP policies to entire organization, edit all DLP policies, create and scope DLP policies to administrative units, and view all alerts and events from all DLP policies.
3. Administrative Unit Restricted administrators must be a member of/assigned to a role group/role that can administer DLP, can create and scope DLP policies only to the administrative unit that they're assigned to, edit DLP policies that are associated to their administrative unit, and view alerts and events only from the DLP policies that are scoped to their administrative unit.

## Validation
1. Confirm that the administrative unit admin is assigned to a DLP-related role (e.g., 'DLP Compliance Management' or 'Information Protection Admin') by running in Exchange Online PowerShell: Get-ManagementRoleAssignment -RoleAssignee <adminUPN> | Where-Object {$_.Role -like '*DLP*' -or $_.Role -like '*DataLossPrevention*'}. 2. Verify the DLP policy is scoped to the correct administrative unit by running: Get-DlpCompliancePolicy -Identity <PolicyName> | Format-List Name, AdminUnits. 3. As the administrative unit admin, attempt to create a new DLP policy scoped to their assigned administrative unit via the Purview compliance portal or New-DlpCompliancePolicy -Name 'TestAU' -AdminUnits <AUName>. 4. Confirm that the admin cannot create or edit DLP policies outside their administrative unit by attempting to scope a policy to a different AU or the entire organization and expecting an access denied error.

## Rollback
1. Remove the administrative unit admin from the DLP-related role by running: Remove-ManagementRoleAssignment -Identity <AssignmentName> -Confirm:$false. 2. Delete any test DLP policies created during validation by running: Remove-DlpCompliancePolicy -Identity 'TestAU' -Confirm:$false. 3. If the unrestricted administrator needs to revert changes, they can edit or delete the scoped DLP policy via the Purview portal or Set-DlpCompliancePolicy -Identity <PolicyName> -AdminUnits $null to remove the administrative unit scope. 4. Restore the original role assignments by re-adding the admin to the previous role group if needed: Add-ManagementRoleAssignment -Role <RoleName> -SecurityGroup <GroupName> -Member <AdminUPN>.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
