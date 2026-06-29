# Implementation: Threat Analytics

**Domain:** Defender for Endpoint
**Subdomain:** Threat Analytics
**Incident Type:** Implementation

## Scenario / Query
How to view the threat analytics dashboard and interpret its sections?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Access to security.microsoft.com/threatanalytics3

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to security.microsoft.com/threatanalytics3
2. Review the Latest threats section for most recently published or updated threat reports, along with the number of active and resolved alerts
3. Review the High-impact threats section for threats with the highest impact to your organization, listed with the highest number of active and resolved alerts first
4. Review the Highest exposure threats section for threats to which your organization has the highest exposure, calculated using severity of associated vulnerabilities and number of exploitable devices
5. Select a threat from the dashboard to view the full report
6. Use the Search field to key in a keyword related to the threat analytics report you'd like to read

## Validation
1. Open a browser and navigate to https://security.microsoft.com/threatanalytics3. 2. Confirm the dashboard loads and displays the 'Latest threats' section with a list of threat reports, including the number of active and resolved alerts for each. 3. Verify the 'High-impact threats' section shows threats sorted by highest number of active and resolved alerts first. 4. Verify the 'Highest exposure threats' section lists threats based on severity of associated vulnerabilities and number of exploitable devices. 5. Select any threat report and confirm the full report page opens with detailed information. 6. Use the Search field to enter a keyword related to a known threat analytics report and confirm the search returns the expected report.

## Rollback
1. If the dashboard fails to load, verify network connectivity and that the user has the required permissions (e.g., Security Reader, Security Administrator). 2. If a section is missing or data is incorrect, refresh the page after a few minutes and check again. 3. If a selected threat report does not open, try accessing the report directly via the search field or navigate back to the dashboard and select a different report. 4. If the search field does not return results, clear the search box and re-enter the keyword, or use a different keyword. 5. If issues persist, refer to the official documentation at https://learn.microsoft.com/en-us/defender-xdr/threat-analytics for troubleshooting steps.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/threat-analytics>
