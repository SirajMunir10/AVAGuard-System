# Troubleshooting: Microsoft Defender XDR

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender XDR
**Incident Type:** Troubleshooting

## Scenario / Query
How do I identify system tags and custom tags on alerts in Microsoft Defender XDR?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** Alert tags

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Custom tags use the white background.
2. System tags typically use red or black background colors.

## Validation
1. In Microsoft Defender XDR (https://security.microsoft.com), navigate to Incidents & alerts > Alerts. 2. Select an alert and review the 'Tags' section in the alert details pane. 3. Confirm that custom tags appear with a white background and system tags appear with a red or black background, as described in the documentation. 4. Optionally, use the Microsoft 365 Defender API to retrieve alert tags: GET https://api.security.microsoft.com/api/alerts/{alert_id}. Verify that the 'tags' field contains the expected custom and system tags.

## Rollback
1. If custom tags were incorrectly applied, remove them by editing the alert in the Microsoft Defender XDR portal: select the alert, click 'Edit tags', and delete the unwanted custom tags. 2. If system tags are missing or incorrect, no manual rollback is possible as they are automatically assigned by the system; contact Microsoft support if system tags are not appearing as expected. 3. If the alert investigation was disrupted, re-run the investigation by selecting the alert and clicking 'Start investigation' in the alert details pane.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts>
