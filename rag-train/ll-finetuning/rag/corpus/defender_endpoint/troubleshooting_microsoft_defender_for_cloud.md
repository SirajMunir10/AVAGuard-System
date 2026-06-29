# Troubleshooting: Microsoft Defender for Cloud

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Cloud
**Incident Type:** Troubleshooting

## Scenario / Query
How do I manage and respond to security alerts in Microsoft Defender for Cloud?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Defender for Cloud enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Sign in to the Azure portal.
2. Navigate to Microsoft Defender for Cloud > Security alerts.
3. Optionally, filter the alerts list with any of the relevant filters. You can add extra filters with the Add filter option. The list updates according to the filters selected. For example, you might want to address security alerts that occurred in the last 24 hours because you're investigating a potential breach in the system.

## Validation
1. Sign in to the Azure portal (https://portal.azure.com).
2. Navigate to Microsoft Defender for Cloud > Security alerts.
3. Apply a filter for the last 24 hours (e.g., 'Time range = Last 24 hours').
4. Confirm that the alerts list updates and displays only alerts from the last 24 hours.
5. Verify that the alert count and details match expected activity for the environment.

## Rollback
1. In the Security alerts blade, remove any custom filters by clicking the 'X' next to each filter or selecting 'Reset to default'.
2. If the filtered view is not needed, simply navigate away from the Security alerts blade (e.g., go to Overview or another section).
3. No permanent changes are made by filtering; no further rollback is required.

## References
- <https://learn.microsoft.com/en-us/azure/defender-for-cloud/managing-and-responding-alerts>
