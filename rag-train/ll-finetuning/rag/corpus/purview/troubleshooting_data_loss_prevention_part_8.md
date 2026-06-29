# Troubleshooting: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Troubleshooting

## Scenario / Query
Why can't I view the DLP alert management dashboard or edit alert configuration options in a DLP policy?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policies

## Symptoms
- Unable to view DLP alert management dashboard
- Unable to edit alert configuration options in a DLP policy

## Error Codes
N/A

## Root Causes
1. User is not a member of the required role groups: Compliance Administrator, Compliance Data Administrator, Security Administrator, Security Operator, Security Reader, Information Protection Admin, Information Protection Analyst, or Information Protection Investigator
2. User does not have the Manage alerts role and either DLP Compliance Management or View-Only DLP Compliance Management role
3. User is not a member of the Content Explorer Content Viewer role group for Content preview and Matched sensitive content and context features

## Remediation Steps
1. Ensure the user is a member of one of the following role groups: Compliance Administrator, Compliance Data Administrator, Security Administrator, Security Operator, Security Reader, Information Protection Admin, Information Protection Analyst, Information Protection Investigator
2. Assign the Manage alerts role and either DLP Compliance Management or View-Only DLP Compliance Management role to the user
3. Add the user to the Content Explorer Content Viewer role group for Content preview and Matched sensitive content and context features

## Validation
1. Sign in to the Microsoft Purview compliance portal (https://compliance.microsoft.com) as the affected user. 2. Navigate to Data Loss Prevention > Alerts. Confirm the DLP alert management dashboard is displayed and alerts are visible. 3. Open an existing DLP policy and verify the 'Edit alert configuration' option is available and can be modified. 4. Run the following PowerShell cmdlet to confirm the user's role assignments: Get-RoleGroupMember -Identity "Compliance Administrator" | Where-Object {$_.Name -eq "<user>"} (repeat for each required role group). 5. Run: Get-RoleGroupMember -Identity "Content Explorer Content Viewer" | Where-Object {$_.Name -eq "<user>"}. 6. Run: Get-ManagementRoleAssignment -Role "Manage alerts" -GetEffectiveUsers | Where-Object {$_.EffectiveUserName -eq "<user>"}. 7. Run: Get-ManagementRoleAssignment -Role "DLP Compliance Management" -GetEffectiveUsers | Where-Object {$_.EffectiveUserName -eq "<user>"} (or View-Only DLP Compliance Management).

## Rollback
1. Remove the user from the role groups added during remediation: Remove-RoleGroupMember -Identity "Compliance Administrator" -Member "<user>" (repeat for each role group added: Compliance Data Administrator, Security Administrator, Security Operator, Security Reader, Information Protection Admin, Information Protection Analyst, Information Protection Investigator). 2. Remove the Manage alerts role assignment: Remove-ManagementRoleAssignment -Identity "<assignment name>" -Confirm:$false (retrieve assignment name via Get-ManagementRoleAssignment -Role "Manage alerts" -GetEffectiveUsers). 3. Remove the DLP Compliance Management or View-Only DLP Compliance Management role assignment: Remove-ManagementRoleAssignment -Identity "<assignment name>" -Confirm:$false. 4. Remove the user from the Content Explorer Content Viewer role group: Remove-RoleGroupMember -Identity "Content Explorer Content Viewer" -Member "<user>". 5. Verify the user can no longer view the DLP alert management dashboard or edit alert configuration options.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-learn>
