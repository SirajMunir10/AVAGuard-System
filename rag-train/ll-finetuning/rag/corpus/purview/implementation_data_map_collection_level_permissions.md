# Implementation: Data Map â€“ Collection-level permissions

**Domain:** Purview
**Subdomain:** Data Map â€“ Collection-level permissions
**Incident Type:** Implementation

## Scenario / Query
A Microsoft Purview administrator has created a new collection hierarchy in the Microsoft Purview governance portal but cannot assign data source curation or data reading permissions to users at the root collection level. The 'Add role assignment' button is grayed out for all roles except 'Collection admins'. What is the cause and how should the administrator resolve this?

## Environment Context
- **Tenant Type:** Production
- **Configuration:** Microsoft Purview account with default root collection; administrator is a member of the 'Collection admins' role group at the root collection.

## Symptoms
- The 'Add role assignment' button is disabled for 'Data curators' and 'Data readers' roles at the root collection.
- Only 'Collection admins' role assignment is available at the root collection level.
- The administrator can create subcollections but cannot delegate permissions to non-administrators at the root.

## Error Codes
N/A

## Root Causes
1. By design, the root collection in Microsoft Purview does not support direct assignment of 'Data curators' or 'Data readers' roles. Only 'Collection admins' can be assigned at the root collection. This is a documented architectural constraint to ensure that root-level administrative control is reserved for collection administrators.

## Remediation Steps
1. 1. Navigate to the root collection in the Microsoft Purview governance portal.
2. 2. Create a subcollection under the root collection (e.g., 'Finance' or 'Engineering').
3. 3. Select the newly created subcollection.
4. 4. Click 'Role assignments' and then 'Add role assignment'.
5. 5. Choose 'Data curators' or 'Data readers' and select the appropriate users or groups.
6. 6. Click 'OK' to save the assignment.
7. 7. Verify that the assigned users can now access the data sources registered under that subcollection.

## Validation
After creating a subcollection and assigning the desired roles, users with 'Data curators' or 'Data readers' permissions can access and manage data sources within that subcollection. The administrator can confirm by logging in as a test user and attempting to browse or curate assets in the subcollection.

## Rollback
To remove a role assignment, navigate to the subcollection's 'Role assignments' page, select the role, and delete the user or group entry.

## References
- <https://learn.microsoft.com/en-us/purview/collection-permissions#root-collection>
