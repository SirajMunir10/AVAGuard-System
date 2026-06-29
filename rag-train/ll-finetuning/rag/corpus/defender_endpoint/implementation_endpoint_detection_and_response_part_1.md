# Implementation: Endpoint Detection and Response

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint Detection and Response
**Incident Type:** Implementation

## Scenario / Query
How to initiate deep analysis for a file in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** File view page

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select the file to go to the file view
2. Select the three dots at the top of the file's page to access the Deep analysis action

## Validation
1. Navigate to the file's page in Microsoft 365 Defender (https://security.microsoft.com).
2. Confirm the file is selected and its details are displayed.
3. Click the three dots (more options) at the top of the file page.
4. Verify that 'Deep analysis' appears in the dropdown menu.
5. Initiate deep analysis and confirm the analysis is submitted successfully (status changes to 'Analysis in progress').

## Rollback
1. If deep analysis was initiated accidentally, cancel the analysis from the file's page (if cancel option is available) or wait for completion.
2. No further rollback is needed as deep analysis is a read-only action that does not modify the file or environment.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-file-alerts>
