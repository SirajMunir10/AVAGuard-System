# Hardening: Microsoft Defender for Identity

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Identity
**Incident Type:** Hardening

## Scenario / Query
How to audit changes to Microsoft Defender for Identity exclusion configurations?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log enabled

## Symptoms
- Unexpected global exclusions added, deleted, or updated for alerts or entities

## Error Codes
N/A

## Root Causes
1. A global exclusion was added for an alert or for an entity (ExclusionConfigurationAdded)
2. A global exclusion was deleted for an alert or for an entity (ExclusionConfigurationDeleted)
3. A global exclusion was updated for an alert or for an entity (ExclusionConfigurationUpdated)

## Remediation Steps
1. Review the audit log for ExclusionConfigurationAdded, ExclusionConfigurationDeleted, and ExclusionConfigurationUpdated activities
2. Ensure only authorized administrators can modify exclusion configurations

## Validation
1. Sign in to the Microsoft 365 Defender portal (https://security.microsoft.com) as a user with the Audit Log or Security Reader role.
2. Navigate to **Audit** > **Solutions** > **Audit** (or go directly to https://compliance.microsoft.com/auditlogsearch).
3. Under the **Search** tab, configure the following filters:
   - **Date range**: Select a range that covers the suspected unauthorized changes.
   - **Activities**: Choose **ExclusionConfigurationAdded**, **ExclusionConfigurationDeleted**, and **ExclusionConfigurationUpdated** from the list of Defender for Identity activities.
4. Click **Search** and review the results. Confirm that only authorized administrators appear in the **User** column for any exclusion modifications.
5. If no unexpected activities are found, the remediation is successful. If any unauthorized activities appear, further investigation is required.

## Rollback
1. If an unauthorized exclusion was added (ExclusionConfigurationAdded), identify the specific exclusion details from the audit log entry (e.g., exclusion type, value).
2. In the Microsoft 365 Defender portal, go to **Settings** > **Identities** > **Exclusions** (or navigate to the Defender for Identity exclusion configuration page).
3. Locate the unauthorized exclusion and delete it by selecting it and choosing **Remove** or **Delete**.
4. If an exclusion was incorrectly deleted (ExclusionConfigurationDeleted), re-add the exclusion using the original details from the audit log (if available) or from a backup of the configuration.
5. If an exclusion was incorrectly updated (ExclusionConfigurationUpdated), revert the exclusion to its previous state using the audit log details or a known good configuration backup.
6. After making changes, repeat the validation steps to confirm the exclusion configuration is now correct and only authorized changes are present.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
