# Troubleshooting: Security Alerts

**Domain:** Defender for Endpoint
**Subdomain:** Security Alerts
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate security alerts in Defender for Cloud when a resource has been deleted but alerts remain?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Defender for Cloud workload protection plans enabled

## Symptoms
- Security alerts are displayed in the portal for 90 days even if the resource related to the alert was deleted

## Error Codes
N/A

## Root Causes
1. Alerts might indicate a potential breach to your organization that needs to be further investigated

## Remediation Steps
1. Review the alert details in the portal
2. Export alerts to CSV format if needed
3. Stream alerts to a SIEM such as Microsoft Sentinel, SOAR, or ITSM solution

## Validation
1. Navigate to Microsoft Defender for Cloud > Security alerts. 2. Locate an alert associated with a deleted resource. 3. Confirm the alert details (e.g., time, severity, description) are still visible. 4. Use the 'Export to CSV' option to download the alert list and verify the alert is included. 5. Check the configured SIEM (e.g., Microsoft Sentinel) to confirm the alert is being streamed and appears in the SIEM's log ingestion.

## Rollback
1. If alerts are missing or not exporting correctly, verify the Defender for Cloud workload protection plans are still enabled under Environment settings. 2. Ensure the SIEM connector (e.g., Sentinel data connector) is active and not throttled. 3. Re-enable any disabled security alert export settings in the continuous export configuration. 4. If alerts were accidentally dismissed, use the 'Filter' option in the alerts page to show 'Dismissed' alerts and reactivate them if needed.

## References
- <https://learn.microsoft.com/en-us/azure/defender-for-cloud/alerts-overview>
