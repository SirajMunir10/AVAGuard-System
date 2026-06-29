# Troubleshooting: Microsoft Defender for Office 365

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Office 365
**Incident Type:** Troubleshooting

## Scenario / Query
What roles are required to access Microsoft Defender for Office 365 alerts?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Microsoft Defender for Office 365

## Symptoms
- Unable to access Microsoft Defender for Office 365 alerts

## Error Codes
N/A

## Root Causes
1. Insufficient role permissions

## Remediation Steps
1. Assign one of the following Microsoft Entra global roles: Global Administrator, Security Administrator, Security Operator, Global Reader, Security Reader
2. Assign one of the following Office 365 Security & Compliance Role Groups: Compliance Administrator, Organization Management
3. Assign a custom role with appropriate permissions

## Validation
1. Sign in to the Microsoft 365 Defender portal (https://security.microsoft.com) as a user with the assigned role. 2. Navigate to Incidents & alerts > Alerts. 3. Verify that the alerts page loads and displays alert data without errors. 4. Run the following PowerShell command to confirm the role assignment: Get-MgRoleManagementDirectoryRoleAssignment -Filter "principalId eq '<user-object-id>'" | Format-List roleDefinitionId. 5. Cross-check the roleDefinitionId with the list of allowed roles from the documentation.

## Rollback
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) as a Global Administrator. 2. Navigate to Identity > Users > All users, select the affected user, then click Assigned roles. 3. Remove the role that was assigned during remediation by clicking Remove assignment. 4. If a custom role was created, navigate to Identity > Roles & admins > Roles & admins, select the custom role, and delete it. 5. Verify the user no longer has access by signing in as the user and attempting to access the Alerts page in the Microsoft 365 Defender portal.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts>
