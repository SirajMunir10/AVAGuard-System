# Implementation: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Implementation

## Scenario / Query
What Dragon Copilot admin activities are logged in the Microsoft 365 audit log?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Dragon Copilot configured

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Accepted terms: AcceptedTerms - Terms of service were accepted.
2. Activated subscription: ActivatedSubscription - A subscription was activated.
3. Added group member: AddedGroupMember - A user was added to a group.
4. Canceled deprovision: CanceledDeprovision - A previously queued deprovision was cancelled.
5. Created billing plan: CreatedBillingPlan - A billing plan was created.
6. Created child organization: CreatedChildOrganization - A child organization was created.
7. Created data export configuration: CreatedDataExportConfig - A data export configuration was created.
8. Created EHR connector: CreatedEhrConnector - An EHR connector was created.
9. Created EHR instance: CreatedEhrInstance - An EHR integration instance was created.
10. Created EHR user: CreatedEhrUser - An EHR user mapping was created.
11. Created environment: CreatedEnvironment - A new Dragon Copilot environment was created.
12. Created extension: CreatedExtension - An extension was installed.
13. Created group: CreatedGroup - A user group was created.
14. Created organization role assignment: CreatedOrganizationRoleAssignment - An organization role assignment was created.
15. Created role assignment: CreatedRoleAssignment - A role was assigned to a user.
16. Deleted billing plan: DeletedBillingPlan - A billing plan was deleted.
17. Deleted data export configuration: DeletedDataExportConfig - A data export configuration was deleted.
18. Deleted EHR instance: DeletedEhrInstance - An EHR integration instance was removed.
19. Deleted EHR user: DeletedEhrUser - An EHR user mapping was deleted.
20. Deleted environment: DeletedEnvironment - An environment was deleted.
21. Deleted group: DeletedGroup - A user group was deleted.
22. Deleted organization role assignment: DeletedOrganizationRoleAssignment - An organization role assignment was deleted.
23. Deleted role assignment: DeletedRoleAssignment - A role assignment was removed.
24. Deleted setting: DeletedSetting - A configuration setting was deleted.
25. Deprovisioned product: DeprovisionedProduct - A product was deprovisioned from an environment.
26. Listed billing plans: ListedBillingPlans - Billing plans were listed.
27. Listed EHR instances: ListedEhrInstances - EHR instances were listed.
28. Listed environments: ListedEnvironments - All environments were listed.
29. Listed extensions: ListedExtensions - Extensions were listed.

## Validation
1. Sign in to the Microsoft Purview compliance portal. 2. Navigate to Audit > Search. 3. Set the Date range to cover the period of interest. 4. In the Activities list, search for and select 'AcceptedTerms', 'ActivatedSubscription', 'AddedGroupMember', 'CanceledDeprovision', 'CreatedBillingPlan', 'CreatedChildOrganization', 'CreatedDataExportConfig', 'CreatedEhrConnector', 'CreatedEhrInstance', 'CreatedEhrUser', 'CreatedEnvironment', 'CreatedExtension', 'CreatedGroup', 'CreatedOrganizationRoleAssignment', 'CreatedRoleAssignment', 'DeletedBillingPlan', 'DeletedDataExportConfig', 'DeletedEhrInstance', 'DeletedEhrUser', 'DeletedEnvironment', 'DeletedGroup', 'DeletedOrganizationRoleAssignment', 'DeletedRoleAssignment', 'DeletedSetting', 'DeprovisionedProduct', 'ListedBillingPlans', 'ListedEhrInstances', 'ListedEnvironments', 'ListedExtensions'. 5. Click Search. 6. Verify that the search results include records for each of the selected activities, confirming that Dragon Copilot admin activities are being logged in the audit log.

## Rollback
If the audit log does not show the expected Dragon Copilot activities, verify that auditing is enabled for the tenant by running the following cmdlet in Exchange Online PowerShell: 'Get-AdminAuditLogConfig | Format-List UnifiedAuditLogIngestionEnabled'. If the property is 'False', enable auditing by running 'Set-AdminAuditLogConfig -UnifiedAuditLogIngestionEnabled $true'. Then, re-run the audit log search as described in the validation steps. If auditing is already enabled, ensure that the user performing the search has the 'Audit Log' role in the Microsoft Purview compliance portal. If the issue persists, contact Microsoft Support.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
