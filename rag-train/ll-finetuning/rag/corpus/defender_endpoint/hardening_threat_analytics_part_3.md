# Hardening: Threat Analytics

**Domain:** Defender for Endpoint
**Subdomain:** Threat Analytics
**Incident Type:** Hardening

## Scenario / Query
How to assess and improve endpoint exposure to a threat using the Endpoints exposure section in Threat Analytics?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Microsoft Defender Vulnerability Management integration

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Review the Endpoints exposure section in the threat analytics report to understand the organization's Exposure level to the threat.
2. Check the deployment status of supported software security updates for vulnerabilities found on onboarded devices.
3. Use data from Microsoft Defender Vulnerability Management to drill down into detailed information via links in the report.

## Validation
1. Navigate to Microsoft 365 Defender portal (https://security.microsoft.com) > Threat analytics. 2. Select the relevant threat report. 3. In the 'Endpoints exposure' section, confirm the Exposure level is displayed and matches expected organizational posture. 4. Verify that the list of affected devices and their vulnerability details are populated. 5. Check that links to Microsoft Defender Vulnerability Management (e.g., 'Open vulnerability page') are functional and lead to detailed vulnerability information.

## Rollback
1. If the Endpoints exposure section is missing or inaccurate, ensure Microsoft Defender Vulnerability Management integration is enabled in Microsoft 365 Defender settings (Settings > Endpoints > General > Advanced features > Microsoft Defender Vulnerability Management). 2. If deployment status of security updates is not showing, verify that devices are properly onboarded to Defender for Endpoint and that vulnerability assessment is active. 3. If drill-down links fail, confirm that the user has appropriate permissions (e.g., Security Reader or Security Administrator) to access Defender Vulnerability Management data. 4. Re-run the threat analytics report after any configuration changes to verify data refresh.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/threat-analytics>
