# Hardening: Microsoft Defender for Identity

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Identity
**Incident Type:** Hardening

## Scenario / Query
How to audit remediation action configuration changes in Microsoft Defender for Identity?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log enabled

## Symptoms
- Manage action accounts mode or set modified unexpectedly

## Error Codes
N/A

## Root Causes
1. The Manage action accounts mode was modified (EntityRemediatorConfigurationUpdated)
2. The Manage action accounts set was modified (RemediationActionConfigurationUpdated)

## Remediation Steps
1. Review the audit log for EntityRemediatorConfigurationUpdated and RemediationActionConfigurationUpdated activities
2. Ensure only authorized administrators can modify remediation action configurations

## Validation
1. Sign in to the Microsoft 365 Defender portal (https://security.microsoft.com) as a Global Administrator or Security Administrator.
2. Navigate to Audit > Search.
3. Set the Date range to cover the period of the suspected change.
4. In the Activities list, search for and select 'EntityRemediatorConfigurationUpdated' and 'RemediationActionConfigurationUpdated'.
5. Run the search and confirm that no unexpected entries appear for these activities.
6. If entries appear, verify that the User field shows only authorized administrators.
7. Additionally, run the following PowerShell command to check current remediation configuration:
   Get-MDATPConfiguration | Select-Object -Property RemediationActionConfiguration, ManageActionAccountsMode
8. Confirm that the values match the expected, authorized settings.

## Rollback
1. If unauthorized changes are found in the audit log, identify the specific user and time of the change.
2. Contact the user to understand the reason for the change and request they revert it.
3. If the user is not available or the change must be undone immediately, use the Microsoft 365 Defender portal to manually restore the previous configuration:
   - Navigate to Settings > Endpoints > Advanced features.
   - Under 'Remediation actions', set 'Manage action accounts mode' and 'Manage action accounts set' to the previously known correct values.
4. Alternatively, use PowerShell to revert:
   Set-MDATPConfiguration -RemediationActionConfiguration <previous_value> -ManageActionAccountsMode <previous_mode>
5. After reverting, re-run the audit search to confirm no further unauthorized changes occur.
6. If the change was made by a compromised account, immediately reset the account's credentials and revoke any active sessions.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
