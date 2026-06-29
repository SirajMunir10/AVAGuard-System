# Implementation: Privileged Identity Management

**Domain:** Entra ID
**Subdomain:** Privileged Identity Management
**Incident Type:** Implementation

## Scenario / Query
How do I set up Privileged Identity Management (PIM) in Microsoft Entra ID?

## Environment Context
- **Tenant Type:** Microsoft Entra ID tenant with PIM license
- **Configuration:** PIM setup requires appropriate licensing (Azure AD Premium P2 or Microsoft Entra ID Governance)

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Set up Privileged Identity Management (PIM) in the Microsoft Entra admin center.
2. After setup, navigate to the left navigation menu to see Tasks, Manage, and Activity options.
3. As an administrator, choose between managing Microsoft Entra roles, managing Azure resource roles, or PIM for Groups.
4. Select the appropriate option to see the corresponding set of options for that management area.

## Validation
1. Confirm that the tenant has an Azure AD Premium P2 or Microsoft Entra ID Governance license assigned. Run: Get-MgOrganization | Select-Object AssignedPlans. 2. Verify PIM is enabled by navigating to the Microsoft Entra admin center > Identity Governance > Privileged Identity Management. 3. Check that the left navigation menu displays Tasks, Manage, and Activity options. 4. As an administrator, select 'Microsoft Entra roles' and confirm the 'Roles' and 'Settings' pages load correctly. 5. Select 'Azure resources' and verify that at least one subscription or resource is discoverable. 6. Select 'PIM for Groups' and confirm that groups appear under 'Groups'.

## Rollback
1. If PIM setup fails or causes issues, remove any unintended role assignments: In Microsoft Entra admin center > Privileged Identity Management > Microsoft Entra roles > Assignments, select each assignment and choose 'Remove'. 2. For Azure resources, navigate to Privileged Identity Management > Azure resources > select the resource > Assignments, and remove any assignments. 3. For PIM for Groups, go to Privileged Identity Management > Groups > select the group > Assignments, and remove assignments. 4. If needed, disable PIM for a specific resource: In Azure resources, select the resource > Settings > uncheck 'Enable PIM for this resource' and save. 5. To fully disable PIM, contact Microsoft Support as there is no self-service disable option documented.

## References
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure>
