# Governance: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Governance

## Scenario / Query
How to audit sensitivity label activities for Microsoft 365 Groups and group-connected Teams sites?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Sensitivity labels for Microsoft 365 Groups and Teams sites

## Symptoms
- Sensitivity label changes for Microsoft 365 Groups or group-connected Teams sites not appearing in Purview audit log

## Error Codes
N/A

## Root Causes
1. Sensitivity labels for Microsoft 365 Groups and group-connected Teams sites are audited with group management in Microsoft Entra ID, not in Purview audit log

## Remediation Steps
1. Use Microsoft Entra ID audit logs to review sensitivity label activities for Microsoft 365 Groups and group-connected Teams sites
2. Refer to Audit logs in Microsoft Entra ID documentation for more information

## Validation
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) as a Global Administrator or Security Administrator.
2. Navigate to Identity > Monitoring & health > Audit logs.
3. Set the 'Activity' filter to 'Add group' or 'Update group' to capture sensitivity label changes.
4. In the results, select a log entry and verify that the 'Target' field shows the group name and the 'Modified properties' section includes 'SensitivityLabelId' or 'SensitivityLabel'.
5. Confirm that the audit event timestamp matches the expected time of the sensitivity label change.

## Rollback
1. If sensitivity label activities are not appearing in Microsoft Entra ID audit logs, verify that Microsoft Entra ID P1 or P2 license is assigned to the tenant (audit logging requires a premium license).
2. Ensure that the user performing the sensitivity label change has the appropriate permissions (e.g., Global Administrator, Groups Administrator, or Sensitivity Label Administrator).
3. Check that the Microsoft Entra ID audit log retention period has not expired (default is 30 days; can be extended with a premium license).
4. If audit logs are still missing, open a support request with Microsoft via the Microsoft 365 admin center (https://admin.microsoft.com) > Support > New service request, referencing the 'Audit logs in Microsoft Entra ID' documentation.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
- <https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-audit-logs>
