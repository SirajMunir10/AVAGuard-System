# Implementation: Threat Analytics

**Domain:** Defender for Endpoint
**Subdomain:** Threat Analytics
**Incident Type:** Implementation

## Scenario / Query
How to access and use the analyst report in Microsoft Defender Threat Analytics to get expert insight from Microsoft security researchers?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Threat Analytics enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to the Analyst report section in Microsoft Defender Threat Analytics.
2. Read through the detailed expert write-up provided by Microsoft security researchers.
3. Review attack chains, including tactics and techniques mapped to the MITRE ATT&CK framework.
4. Follow exhaustive lists of recommendations and powerful threat hunting guidance.

## Validation
1. Navigate to the Microsoft 365 Defender portal (https://security.microsoft.com).
2. In the left navigation, select 'Threat analytics' under 'Endpoints' or 'Incidents & alerts'.
3. Confirm that the Threat Analytics dashboard loads and displays a list of threat reports.
4. Select a specific threat report and verify that the 'Analyst report' tab is visible and contains a detailed write-up from Microsoft security researchers.
5. Within the analyst report, confirm that the attack chain section includes tactics and techniques mapped to the MITRE ATT&CK framework.
6. Verify that the report includes exhaustive lists of recommendations and powerful threat hunting guidance.
7. Optionally, use the 'Export' feature to download the report and confirm the content matches the online version.

## Rollback
1. If the Threat Analytics page fails to load or the analyst report is not accessible, verify that the user account has the required permissions (e.g., Security Reader, Security Administrator, or Global Reader).
2. Check that the 'Threat Analytics' feature is enabled in the Microsoft 365 Defender settings under 'Permissions' > 'Roles' or 'Settings' > 'Endpoints' > 'General' > 'Advanced features'.
3. If the feature was recently disabled, re-enable it by toggling 'Threat Analytics' to 'On' and saving the changes.
4. If the analyst report content appears incomplete or outdated, clear the browser cache and cookies, then reload the portal.
5. As a last resort, contact Microsoft Support to report the issue and request restoration of default Threat Analytics settings.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/threat-analytics>
