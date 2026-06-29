# Governance: Microsoft Entra ID (Azure AD) Governance

**Domain:** Azure
**Subdomain:** Microsoft Entra ID (Azure AD) Governance
**Incident Type:** Governance

## Scenario / Query
An administrator notices that a user in Azure AD has been assigned a highly privileged role (e.g., Global Administrator) but the assignment was not approved through the organization's Privileged Identity Management (PIM) activation process. How can the organization enforce that all privileged role assignments require PIM activation and approval?

## Environment Context
- **Tenant Type:** Production
- **Configuration:** Azure AD PIM is enabled but not enforced for all role assignments; some roles are assigned directly as 'Active' instead of 'Eligible'.

## Symptoms
- Users have permanent active role assignments instead of eligible assignments requiring activation.
- No approval workflow is triggered when a user is assigned a privileged role.
- Audit logs show direct role assignments bypassing PIM.

## Error Codes
N/A

## Root Causes
1. Role assignments were made directly in Azure AD without using PIM.
2. PIM settings do not require approval for activation of certain roles.
3. No governance policy enforces that all privileged roles must be managed through PIM.

## Remediation Steps
1. 1. In the Azure portal, navigate to Microsoft Entra ID > Privileged Identity Management > Azure AD roles > Settings.
2. 2. For each privileged role, select the role and then select 'Edit' to modify the activation settings.
3. 3. Under 'Activation', set 'Require approval to activate' to 'Yes' and select the approvers.
4. 4. Under 'Assignment', set 'Allow permanent eligible assignment' to 'No' and 'Expire eligible assignments after' to a desired duration.
5. 5. Remove any existing direct active role assignments and re-assign the roles as 'Eligible' via PIM.
6. 6. Use Azure AD audit logs to review and revoke any unauthorized direct assignments.

## Validation
Verify that all privileged role assignments appear as 'Eligible' in PIM and that activation requires approval. Attempt to assign a privileged role directly via Azure AD â€“ it should be blocked or flagged by policy.

## Rollback
If needed, revert PIM settings to allow permanent active assignments and remove approval requirements. Re-assign roles directly if emergency access is required (document and monitor such changes).

## References
- <https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-change-default-settings>
