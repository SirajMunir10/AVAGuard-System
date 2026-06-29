# Troubleshooting: Retention Policies

**Domain:** Purview
**Subdomain:** Retention Policies
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify when retention settings for a retention policy have been changed in Microsoft Purview?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Retention policies configured in Purview compliance portal

## Symptoms
- Retention policy behavior changes unexpectedly
- Items are retained or deleted differently than expected

## Error Codes
N/A

## Root Causes
1. Administrator changed retention settings for an existing retention policy

## Remediation Steps
1. Audit the SetRetentionComplianceRule activity in the audit log to identify the change
2. Review the specific retention settings that were modified, including retention duration and actions at expiration

## Validation
1. Go to Microsoft Purview compliance portal > Audit. 2. Search for 'SetRetentionComplianceRule' activity between the time the behavior changed and now. 3. Confirm that one or more audit log entries show modifications to retention duration or expiration actions. 4. Open each relevant audit record and verify the 'ModifiedProperties' field to see exactly which settings were changed (e.g., RetentionDuration, RetentionAction). 5. Compare the current retention policy settings in Data Lifecycle Management > Retention policies with the audit log details to ensure the policy now matches expected values.

## Rollback
1. In Microsoft Purview compliance portal, go to Data Lifecycle Management > Retention policies. 2. Select the affected retention policy. 3. Edit the policy to restore the previous retention duration and expiration actions as identified from the audit log (before the change). 4. Save the policy. 5. Monitor the audit log for a new 'SetRetentionComplianceRule' event confirming the rollback. 6. Verify that items are now retained or deleted as originally expected.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
