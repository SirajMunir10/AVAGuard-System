# Hardening: Microsoft Defender for Identity

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Identity
**Incident Type:** Hardening

## Scenario / Query
How to audit entity tag changes in Microsoft Defender for Identity?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log enabled

## Symptoms
- Tags added or removed from entities unexpectedly

## Error Codes
N/A

## Root Causes
1. A tag was added or removed from an entity (TaggingConfigurationUpdated)

## Remediation Steps
1. Review the audit log for TaggingConfigurationUpdated activities
2. Ensure only authorized administrators can modify entity tags

## Validation
1. Sign in to the Microsoft 365 Defender portal (https://security.microsoft.com).
2. Navigate to 'Audit' under 'Solutions' > 'Audit log'.
3. Set the 'Date' range to cover the period of unexpected tag changes.
4. In the 'Activities' filter, search for and select 'TaggingConfigurationUpdated'.
5. Run the search and confirm that the audit log shows only authorized administrators (e.g., Global Admin, Security Admin) as the user who performed the activity.
6. Verify that the 'Item' column shows the affected entity (e.g., device, user) and that the 'Details' column indicates the tag added or removed.
7. Optionally, export the audit log results to a CSV file for record-keeping.

## Rollback
1. If an unauthorized tag change is detected, identify the affected entity from the audit log.
2. Sign in to the Microsoft 365 Defender portal with an account that has the 'Security Administrator' or 'Global Administrator' role.
3. Navigate to 'Settings' > 'Endpoints' > 'Device management' > 'Tags' (or the relevant entity tag management page).
4. For the affected entity, add back any tag that was incorrectly removed, or remove any tag that was incorrectly added, based on the audit log details.
5. To prevent recurrence, review the roles assigned to users who performed the unauthorized change and adjust permissions as needed (e.g., remove unnecessary 'Security Administrator' or 'Global Administrator' roles).
6. Consider creating an alert policy in the Microsoft 365 Defender portal to notify administrators when 'TaggingConfigurationUpdated' activities occur.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
