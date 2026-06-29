# Implementation: Incident Investigation

**Domain:** Sentinel
**Subdomain:** Incident Investigation
**Incident Type:** Implementation

## Scenario / Query
How to document investigation steps and enrich incidents with comments in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Access the Comments tab on the incident details page.
2. Document steps taken during investigation to ensure accurate reporting and collaboration.
3. Run a playbook on an incident that fetches relevant information from external sources (e.g., checking a file for malware at VirusTotal).
4. Have the playbook place the external source's response and any other defined information in the incident's comments.

## Validation
1. Navigate to Microsoft Sentinel > Incidents. Select an incident and click 'View full details'. Confirm the 'Comments' tab is visible. 2. Add a test comment (e.g., 'Validation test comment') and verify it appears in the comments list. 3. Run a playbook that fetches external data (e.g., VirusTotal) and writes to comments. After execution, open the incident's comments and confirm the external response is recorded. 4. Use Azure Resource Graph or Log Analytics: `SentinelAudit | where ActivityType == 'Add comment'` to verify comment creation events.

## Rollback
1. Delete any test comments added during validation: In the incident details page, click the 'Comments' tab, locate the test comment, and select 'Delete'. 2. If a playbook was run and wrote unwanted comments, remove those comments manually via the same 'Delete' option. 3. If the playbook caused unintended changes to incident status or owner, reset the incident status to its original state (e.g., 'New' or 'Active') and reassign the original owner via the incident details page. 4. Review playbook settings and disable or modify the playbook if it is not behaving as expected.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/investigate-cases>
