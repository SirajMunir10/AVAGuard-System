# Troubleshooting: Key Vault

**Domain:** Azure
**Subdomain:** Key Vault
**Incident Type:** Troubleshooting

## Scenario / Query
How can I monitor vault availability, service latency periods or other performance metrics for key vault?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Number of requests sent to key vault rises
- Potential increase in latency of requests
- Requests being throttled
- Degraded performance of service

## Error Codes
N/A

## Root Causes
1. Scaling of service leading to increased demand on key vault

## Remediation Steps
1. Monitor key vault performance metrics
2. Get alerted for specific thresholds
3. Follow step-by-step guide to configure monitoring (referenced as 'read more' in source)

## Validation
1. Open Azure portal and navigate to your Key Vault resource. 2. Under 'Monitoring', select 'Metrics'. 3. Add the following metrics: 'Service Api Latency' (average), 'Total Service Api Requests' (count), and 'Saturation Saturated' (average). 4. Set the time range to the last hour. 5. Verify that 'Service Api Latency' is below 5 ms (typical baseline), 'Total Service Api Requests' shows a stable or decreasing trend, and 'Saturation Saturated' is 0 (indicating no throttling). 6. Check 'Alerts' under 'Monitoring' to confirm that alert rules for these metrics are enabled and have triggered no false positives.

## Rollback
1. In Azure portal, go to your Key Vault resource. 2. Under 'Monitoring', select 'Alerts'. 3. Disable any alert rules that were recently created for latency or request count thresholds. 4. Under 'Monitoring', select 'Metrics' and remove any custom metric charts added during remediation. 5. If scaling changes were made (e.g., increasing Key Vault throughput limits via Azure support), revert to the original service limits by contacting Azure support. 6. Verify that no monitoring configurations are interfering with normal operations.

## References
- <https://learn.microsoft.com/en-us/azure/key-vault/general/troubleshooting-access-issues>
