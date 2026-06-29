# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How to configure advanced classification scanning and protection in Endpoint DLP settings?

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
1. Turn on advanced classification scanning and protection in Endpoint DLP settings.
2. If concerned about bandwidth usage, set a limit on how much bandwidth can be used in a rolling 24-hour period.
3. If bandwidth usage is not a concern, select 'Do not limit bandwidth. Unlimited' to allow unlimited bandwidth use.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Endpoint DLP settings. 2. Verify that 'Advanced classification scanning and protection' is toggled to 'On'. 3. Under 'Bandwidth and throttling', confirm the selected option matches the intended configuration (e.g., 'Do not limit bandwidth. Unlimited' or a specific limit in MB per 24-hour period). 4. Run a test file scan on an endpoint to ensure DLP policies are being applied and advanced classification is functioning.

## Rollback
1. In Microsoft Purview compliance portal > Data Loss Prevention > Endpoint DLP settings, set 'Advanced classification scanning and protection' to 'Off'. 2. If a bandwidth limit was configured, revert to the previous setting (e.g., remove the limit or adjust to the original value). 3. Monitor endpoint performance and DLP policy enforcement to confirm the rollback has taken effect.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
