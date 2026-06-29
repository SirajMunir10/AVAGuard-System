# Implementation: Privileged Identity Management

**Domain:** Azure
**Subdomain:** Privileged Identity Management
**Incident Type:** Implementation

## Scenario / Query
Who can manage assignments for Azure resource roles in Privileged Identity Management?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Privileged Identity Management for Azure resources

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Only a subscription administrator, a resource Owner, or a resource User Access Administrator can manage assignments for other administrators for Azure resource roles in Privileged Identity Management.
2. Users who are Privileged Role Administrators, Security Administrators, or Security Readers don't by default have access to view assignments to Azure resource roles in Privileged Identity Management.

## Validation
1. Sign in to the Azure portal (https://portal.azure.com) with an account that is a subscription administrator, resource Owner, or resource User Access Administrator.
2. Navigate to 'Microsoft Entra ID' > 'Privileged Identity Management' > 'Azure resources'.
3. Select the relevant Azure resource (e.g., subscription, resource group, or resource).
4. Under 'Manage', click 'Assignments' and verify that you can view, create, and modify role assignments for Azure resource roles.
5. Confirm that users who are Privileged Role Administrators, Security Administrators, or Security Readers cannot see assignments for Azure resource roles by signing in with one of those roles and checking that the 'Assignments' blade is not visible or accessible.

## Rollback
1. If the remediation introduced unintended access, remove any unauthorized assignments: In PIM for Azure resources, select the resource, go to 'Assignments', and deactivate or remove the assignment for the user who should not have management capabilities.
2. To restore default visibility restrictions, ensure that no custom roles or assignments grant 'Privileged Role Administrator', 'Security Administrator', or 'Security Reader' users access to Azure resource role assignments. If such access was inadvertently granted, remove those assignments.
3. If the issue persists, verify that the subscription administrator, resource Owner, or resource User Access Administrator roles are correctly assigned only to intended users via Azure RBAC (Access control (IAM) for the resource).

## References
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure>
