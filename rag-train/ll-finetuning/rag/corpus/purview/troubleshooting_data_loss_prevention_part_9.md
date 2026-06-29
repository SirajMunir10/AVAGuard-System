# Troubleshooting: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate a DLP alert using the DLP Alerts dashboard?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP Alerts dashboard

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the DLP Alerts dashboard in standard view
2. Use the DLP Alerts dashboard in Alert Triage Agent (Preview)
3. Use Microsoft Security Copilot

## Validation
1. Navigate to the Microsoft Purview compliance portal (https://compliance.microsoft.com) and go to Data Loss Prevention > Alerts. 2. Confirm the DLP Alerts dashboard loads in standard view and displays recent alerts. 3. If available, switch to Alert Triage Agent (Preview) view and verify the same alerts appear. 4. Optionally, open Microsoft Security Copilot and run a prompt such as 'Show me recent DLP alerts' to confirm integration is working.

## Rollback
1. If the DLP Alerts dashboard fails to load, clear browser cache and cookies, then retry. 2. If the Alert Triage Agent (Preview) view is not available or causes errors, revert to standard view by selecting 'Standard view' from the view switcher. 3. If Microsoft Security Copilot does not return DLP alerts, verify that the Security Copilot license is assigned and that the DLP connector is enabled in the Copilot settings. 4. If issues persist, refer to the official documentation at https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-learn for further troubleshooting steps.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-learn>
