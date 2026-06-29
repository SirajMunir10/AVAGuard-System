# Implementation: Audit Log

**Domain:** Purview
**Subdomain:** Audit Log
**Incident Type:** Implementation

## Scenario / Query
How to search the audit log for activities related to the Patients application in Microsoft Teams?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Environment configured to support the Patients app in Microsoft Teams

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Search the audit log for activities related to the Patients app
2. If your environment is configured to support the Patients app, an additional activity group for these activities is available in the Activities picker list

## Validation
1. Navigate to Microsoft Purview compliance portal > Audit > Search. 2. In the Activities picker, verify that 'Patients app activities' group is listed (if environment is configured for Patients app). 3. Select one or more activities from that group, set a date range covering the incident period, and run a search. 4. Confirm that the search returns relevant audit records for the Patients app. 5. Export the results and verify that the 'Operation' field contains expected values such as 'PatientAccessed' or 'PatientUpdated'.

## Rollback
1. If the audit search fails or returns no results, verify that audit logging is enabled in the Microsoft 365 Defender portal (Settings > Cloud Apps > Audit log). 2. Ensure the user performing the search has the 'Audit Logs' role in Purview compliance portal. 3. Confirm that the environment is correctly configured for the Patients app by checking Teams admin center > Teams apps > Manage apps for 'Patients' and verifying it is allowed. 4. If the Patients app activities group is missing, re-enable the app via Teams admin center and wait up to 24 hours for audit schema updates. 5. Retry the audit search after confirming configuration.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
- <https://learn.microsoft.com/en-us/purview/audit-log-activities (Audit logs for Patients app)>
