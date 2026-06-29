# Troubleshooting: Audit Log Activities

**Domain:** Purview
**Subdomain:** Audit Log Activities
**Incident Type:** Troubleshooting

## Scenario / Query
How to detect impersonation attempts in Microsoft Teams using audit logs?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log search enabled

## Symptoms
- Potential impersonation activity by external message senders

## Error Codes
N/A

## Root Causes
1. An external message sender is detected to have potential impersonation activity

## Remediation Steps
1. Search for TeamsImpersonationDetected activity in audit log
2. Review the details of the detected impersonation attempt

## Validation
1. Navigate to Microsoft Purview compliance portal > Audit > Search audit log. 2. Set 'Activities' filter to 'TeamsImpersonationDetected'. 3. Set 'Start date' and 'End date' to cover the period of suspected impersonation. 4. Run the search and confirm that one or more audit log entries appear with the activity 'TeamsImpersonationDetected'. 5. For each entry, expand the details and verify that the 'Item' field contains the external sender's identifier and the 'User' field shows the impersonated user.

## Rollback
1. If the audit log search returns no results or incorrect entries, verify that audit log search is enabled in the Microsoft 365 Defender portal (Settings > Microsoft 365 Defender > Audit log). 2. If disabled, enable it and wait up to 24 hours for historical data to populate. 3. If the search still fails, clear any custom date or activity filters and run a broad audit log search for 'TeamsImpersonationDetected' without date restrictions. 4. If no impersonation events are found, consider that the impersonation attempt may not have been logged or may have been blocked by other security controls; review Teams external access settings and anti-phishing policies.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
