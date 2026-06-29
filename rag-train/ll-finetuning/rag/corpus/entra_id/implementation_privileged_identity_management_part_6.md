# Implementation: Privileged Identity Management

**Domain:** Entra ID
**Subdomain:** Privileged Identity Management
**Incident Type:** Implementation

## Scenario / Query
Who can manage assignments for Microsoft Entra roles in Privileged Identity Management?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Privileged Identity Management

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Only a user who is in the Privileged Role Administrator or Global Administrator role can manage assignments for other administrators for Microsoft Entra roles in Privileged Identity Management.
2. Global Administrators, Security Administrators, Global Readers, and Security Readers can view assignments to Microsoft Entra roles in Privileged Identity Management.

## Validation
1. Sign in to the Microsoft Entra admin center as a user assigned the Privileged Role Administrator or Global Administrator role. 2. Navigate to Identity Governance > Privileged Identity Management > Microsoft Entra roles. 3. Select a role assignment for an administrator and verify that you can modify or remove the assignment. 4. Sign in as a user with only Security Administrator, Global Reader, or Security Reader roles. 5. Navigate to the same PIM blade and confirm you can view assignments but cannot modify or remove them.

## Rollback
1. If the remediation fails (e.g., an unauthorized user cannot manage assignments), ensure the user is added to the Privileged Role Administrator or Global Administrator role via Microsoft Entra ID > Roles and administrators. 2. If the issue is that a user can manage assignments when they should not, remove the user from the Privileged Role Administrator or Global Administrator role. 3. Verify changes by repeating the validation steps.

## References
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure>
