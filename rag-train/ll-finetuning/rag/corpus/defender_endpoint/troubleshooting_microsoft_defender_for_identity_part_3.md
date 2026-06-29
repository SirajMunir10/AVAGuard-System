# Troubleshooting: Microsoft Defender for Identity

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to audit directory services account configuration changes in Microsoft Defender for Identity?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log enabled

## Symptoms
- Directory services accounts set modified unexpectedly

## Error Codes
N/A

## Root Causes
1. The Directory services accounts set was modified (DirectoryServicesAccountConfigurationUpdated)

## Remediation Steps
1. Review the audit log for DirectoryServicesAccountConfigurationUpdated activities
2. Verify the changes against authorized administrators

## Validation
1. Sign in to the Microsoft 365 Defender portal (https://security.microsoft.com) as a Global Administrator or Security Administrator.
2. Navigate to Audit > Search.
3. Set the Date range to cover the time of the unexpected change.
4. In the Activities list, select 'Updated directory services account configuration' (GUID: 1c6e9a7a-9a10-4c2c-8a4d-4c8e8e8e8e8e).
5. Click Search and confirm that the audit log shows entries for DirectoryServicesAccountConfigurationUpdated with the old and new values of the directory services account.
6. Verify that the 'User' field for each entry matches an authorized administrator who should have made the change.
7. If no audit entries appear, check that audit logging is enabled in the Microsoft 365 Defender portal under Settings > Microsoft 365 Defender > Audit log.

## Rollback
1. If the change was unauthorized, identify the specific directory services account that was modified from the audit log details.
2. Sign in to the Microsoft 365 Defender portal (https://security.microsoft.com) as a Global Administrator.
3. Navigate to Settings > Microsoft 365 Defender > Directory services accounts.
4. Select the affected account and click Edit.
5. Revert the account settings to the previous values recorded in the audit log (e.g., domain, username, password).
6. Click Save and confirm the update.
7. After saving, run a new audit search for DirectoryServicesAccountConfigurationUpdated to verify the rollback action is logged.
8. If the account cannot be edited, contact Microsoft Support for assistance in restoring the configuration from a backup or previous state.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
