# Implementation: Security Baselines

**Domain:** Intune
**Subdomain:** Security Baselines
**Incident Type:** Implementation

## Scenario / Query
How to view available security baseline templates and their versions in Microsoft Intune?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Endpoint security > Security baselines

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to the Microsoft Intune admin center.
2. Go to Endpoint security > Security baselines.
3. View the list of available baselines, including the name of each security baseline template, how many profiles use that type of baseline, how many separate instances (versions) of the baseline type are available, and a Last Published date.
4. To view more information about baseline versions, select a baseline type (e.g., Security Baseline for Windows 10 and later) to open its Profiles pane, then select Versions.
5. Intune displays details about the versions of that baseline in use by your profiles, including the most recent and current baseline version.
6. Select a single version to view deeper details about the profiles that use that version.

## Validation
1. Navigate to the Microsoft Intune admin center (https://intune.microsoft.com).
2. Go to Endpoint security > Security baselines.
3. Confirm the list displays baseline names, profile counts, version counts, and Last Published dates.
4. Select a baseline type (e.g., 'Security Baseline for Windows 10 and later') and click 'Versions'.
5. Verify that version details appear, including the most recent and current baseline version.
6. Select a single version and confirm that deeper profile details are shown.

## Rollback
No rollback is required because viewing security baseline templates and versions is a read-only operation that does not change any configuration.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/security-baselines>
