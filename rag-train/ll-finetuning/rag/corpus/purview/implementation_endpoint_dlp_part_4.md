# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How to set a bandwidth usage limit for advanced classification in Endpoint DLP?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP settings

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Configure the limit in Endpoint DLP settings.
2. The limit applies per device.
3. Set the limit on how much bandwidth can be used in a rolling 24-hour period.

## Validation
1. On a test device, open Windows Security > App & browser control > Exploit protection settings. 2. Navigate to Endpoint DLP settings in Microsoft Purview compliance portal: https://compliance.microsoft.com/dlp/endpoint. 3. Verify that the bandwidth limit value (e.g., 500 MB) is set under 'Advanced classification' > 'Bandwidth limit (per device, rolling 24 hours)'. 4. On the device, trigger a DLP policy that uses advanced classification (e.g., a sensitive info type scan). 5. Monitor network usage via Task Manager or Performance Monitor to confirm that bandwidth consumption does not exceed the configured limit over a 24-hour period.

## Rollback
1. In Microsoft Purview compliance portal, go to Endpoint DLP settings: https://compliance.microsoft.com/dlp/endpoint. 2. Under 'Advanced classification', set the 'Bandwidth limit (per device, rolling 24 hours)' to 'No limit' or the previous value. 3. If the limit was causing false positives or blocking legitimate scans, clear the bandwidth limit field entirely. 4. On affected devices, restart the Microsoft Endpoint DLP service (e.g., run 'Restart-Service WdNisSvc' in PowerShell as admin) to apply the change immediately. 5. Verify that advanced classification resumes normal operation without bandwidth throttling.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
