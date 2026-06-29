# Troubleshooting: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Troubleshooting

## Scenario / Query
How to view matched conditions in a DLP event to identify the exact cause for a flagged DLP policy?

## Environment Context
- **Tenant Type:** E3 or E5 license holders
- **Configuration:** Auditing must be enabled; Advanced classification scanning and protection must be enabled; Windows 10 x64 (build 1809 or later) or Windows 11 required

## Symptoms
- DLP policy flags events without clear indication of which condition triggered the alert

## Error Codes
N/A

## Root Causes
1. Matched conditions data may not be visible if auditing is not enabled
2. Matched conditions data may not be visible if Advanced classification scanning and protection is not enabled
3. Insufficient Windows OS build (requires Windows 10 x64 build 1809 or later, or Windows 11)

## Remediation Steps
1. Enable Auditing in Microsoft Purview
2. Enable Advanced classification scanning and protection
3. Ensure Windows OS meets minimum build requirements (Windows 10 x64 build 1809 or later, or Windows 11; see KB5023773 for required builds)

## Validation
Check DLP Alerts console, Activity explorer, or Microsoft Defender for Business portal; in the Events tab, open Details to see Other matched conditions

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-learn>
