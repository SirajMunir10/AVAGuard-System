# Troubleshooting: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Troubleshooting

## Scenario / Query
What happens when the bandwidth usage limit is exceeded in Endpoint DLP advanced classification?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP settings with bandwidth limit

## Symptoms
- DLP stops sending user content to the cloud.
- Data classification continues locally on the device.
- Classification by using exact data match, named entities, trainable classifiers, and credential classifiers is not available.

## Error Codes
N/A

## Root Causes
1. Bandwidth usage limit set in Endpoint DLP settings is exceeded.

## Remediation Steps
1. Wait until cumulative bandwidth usage drops below the rolling 24-hour limit.
2. Communication with cloud services resumes automatically when the limit is no longer exceeded.

## Validation
1. Check the current bandwidth usage by running Get-DlpEndpointBandwidthUsage in PowerShell. 2. Verify that the usage value is below the configured limit (e.g., 500 MB per 24 hours). 3. Confirm that DLP cloud communication has resumed by checking the DLP agent logs for successful upload events. 4. Test classification by triggering a policy that requires cloud services (e.g., exact data match) and ensure it completes without errors.

## Rollback
1. If the bandwidth limit is too restrictive, increase the limit by modifying the Endpoint DLP settings in the Microsoft Purview compliance portal under Endpoint DLP > Device settings > Bandwidth limit. 2. If cloud communication does not resume, restart the DLP agent service on the device using Restart-Service -Name DlpAgent. 3. If issues persist, temporarily disable the bandwidth limit by setting it to 'Unlimited' in the same settings page. 4. Monitor the device for any classification failures and revert to the original limit if needed.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
